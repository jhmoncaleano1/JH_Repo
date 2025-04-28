import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import os
import sqlite3
from matplotlib.backends.backend_pdf import PdfPages

# Configuración de visualización
plt.style.use('ggplot')
sns.set(style="whitegrid")

# Crear conexión a base de datos SQLite (opcional pero útil para persistencia)
conn = sqlite3.connect("data\\ventas_analisis.db")
cursor = conn.cursor()

# Crear las tablas necesarias si no existen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        cod_cliente INTEGER PRIMARY KEY,
        nombre_cliente TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS facturas (
        num_fact TEXT PRIMARY KEY,
        cod_cliente INTEGER,
        fecha_facturacion DATE,
        fecha_vcto DATE,
        valor REAL,
        FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        num_fact TEXT,
        cod_cliente INTEGER,
        fecha_pago DATE,
        vr_pago REAL,
        FOREIGN KEY (num_fact) REFERENCES facturas(num_fact),
        FOREIGN KEY (cod_cliente) REFERENCES clientes(cod_cliente)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rango_edad (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        min INTEGER,
        max INTEGER,
        edad TEXT,
        orden INTEGER
    )
''')

conn.commit()

class ModeloAnalisisVentas:
    def __init__(self):
        self.clientes_df = None
        self.facturas_df = None
        self.pagos_df = None
        self.rango_edad_df = None
        self.conn = conn
        self.cursor = cursor
        
    def cargar_desde_excel(self, ruta_clientes, ruta_facturas, ruta_pagos, ruta_rango_edad):
        """Carga datos desde archivos Excel"""
        # Carga de datos
        self.clientes_df = pd.read_excel(ruta_clientes)
        self.facturas_df = pd.read_excel(ruta_facturas)
        self.pagos_df = pd.read_excel(ruta_pagos)
        self.rango_edad_df = pd.read_excel(ruta_rango_edad, encoding='latin1')
        
        # Limpieza y conversión de datos
        self.limpiar_datos()
        
        # Guardar en SQLite
        self.guardar_en_db()
        
        print("Datos cargados con éxito")
        
    def limpiar_datos(self):
        """Limpia y formatea los datos"""
        # Convertir fechas
        self.facturas_df['Fecha Facturación'] = pd.to_datetime(self.facturas_df['Fecha Facturación'], dayfirst=True)
        self.facturas_df['Fecha Vcto'] = pd.to_datetime(self.facturas_df['Fecha Vcto'], dayfirst=True)
        self.pagos_df['FECHA PAGO'] = pd.to_datetime(self.pagos_df['FECHA PAGO'], dayfirst=True)
        
        # Asegurar tipos correctos
        self.facturas_df['Valor'] = self.facturas_df['Valor'].astype(float)
        self.pagos_df['VR PAGO'] = self.pagos_df['VR PAGO'].astype(float)
        self.clientes_df['COD CLIENTE'] = self.clientes_df['COD CLIENTE'].astype(int)
        self.facturas_df['CodCliente'] = self.facturas_df['CodCliente'].astype(int)
        self.pagos_df['COD CLIENTE'] = self.pagos_df['COD CLIENTE'].astype(int)
        
        # Eliminar columnas vacías si las hay
        self.clientes_df = self.clientes_df.dropna(axis=1, how='all')
        
    def guardar_en_db(self):
        """Guarda los datos en la base de datos SQLite"""
        # Eliminar datos existentes
        self.cursor.execute("DELETE FROM clientes")
        self.cursor.execute("DELETE FROM facturas")
        self.cursor.execute("DELETE FROM pagos")
        self.cursor.execute("DELETE FROM rango_edad")
        
        # Insertar nuevos datos
        self.clientes_df.to_sql('clientes', self.conn, if_exists='append', index=False)
        
        # Formatear fechas para SQLite
        facturas_to_sql = self.facturas_df.copy()
        facturas_to_sql['Fecha Facturación'] = facturas_to_sql['Fecha Facturación'].dt.strftime('%Y-%m-%d')
        facturas_to_sql['Fecha Vcto'] = facturas_to_sql['Fecha Vcto'].dt.strftime('%Y-%m-%d')
        facturas_to_sql.to_sql('facturas', self.conn, if_exists='append', index=False)
        
        pagos_to_sql = self.pagos_df.copy()
        pagos_to_sql['FECHA PAGO'] = pagos_to_sql['FECHA PAGO'].dt.strftime('%Y-%m-%d')
        pagos_to_sql.to_sql('pagos', self.conn, if_exists='append', index=False)
        
        self.rango_edad_df.to_sql('rango_edad', self.conn, if_exists='append', index=False)
        
        self.conn.commit()
        
    def cargar_desde_db(self):
        """Carga datos desde la base de datos SQLite"""
        self.clientes_df = pd.read_sql("SELECT * FROM clientes", self.conn)
        self.facturas_df = pd.read_sql("SELECT * FROM facturas", self.conn)
        self.pagos_df = pd.read_sql("SELECT * FROM pagos", self.conn)
        self.rango_edad_df = pd.read_sql("SELECT * FROM rango_edad", self.conn)
        
        # Convertir fechas
        self.facturas_df['Fecha Facturación'] = pd.to_datetime(self.facturas_df['fecha_facturacion'])
        self.facturas_df['Fecha Vcto'] = pd.to_datetime(self.facturas_df['fecha_vcto'])
        self.pagos_df['FECHA PAGO'] = pd.to_datetime(self.pagos_df['fecha_pago'])
        
        print("Datos cargados desde base de datos con éxito")
    
    def calcular_metricas(self):
        """Calcula métricas clave del modelo"""
        # Cálculos base
        total_facturado = self.facturas_df['Valor'].sum()
        total_pagado = self.pagos_df['VR PAGO'].sum()
        total_pendiente = total_facturado - total_pagado
        
        # Facturas pagadas y pendientes
        facturas_pagadas = self.pagos_df.groupby('NUM FACT')['VR PAGO'].sum().reset_index()
        facturas_pagadas.columns = ['NUMFACT', 'Total_Pagado']
        
        # Unir con facturas
        analisis_df = self.facturas_df.merge(facturas_pagadas, on='NUMFACT', how='left')
        analisis_df['Total_Pagado'] = analisis_df['Total_Pagado'].fillna(0)
        analisis_df['Pendiente'] = analisis_df['Valor'] - analisis_df['Total_Pagado']
        
        # Calcular estado y días de vencimiento
        hoy = datetime.now()
        analisis_df['Dias_Vencimiento'] = (hoy - analisis_df['Fecha Vcto']).dt.days
        
        analisis_df['Estado'] = 'Por vencer'
        analisis_df.loc[analisis_df['Pendiente'] <= 0, 'Estado'] = 'Pagada'
        analisis_df.loc[(analisis_df['Dias_Vencimiento'] > 0) & (analisis_df['Pendiente'] > 0), 'Estado'] = 'Vencida'
        analisis_df.loc[(analisis_df['Dias_Vencimiento'] <= 30) & (analisis_df['Dias_Vencimiento'] > 0) & (analisis_df['Pendiente'] > 0), 'Estado'] = 'Próxima a vencer'
        
        # Calcular cartera por rangos de edad
        analisis_df['Rango_Edad'] = None
        for _, row in self.rango_edad_df.iterrows():
            mask = (analisis_df['Dias_Vencimiento'] >= row['Min']) & (analisis_df['Dias_Vencimiento'] <= row['Max'])
            analisis_df.loc[mask, 'Rango_Edad'] = row['Edad']
            
        # Agregar nombres de clientes
        analisis_df = analisis_df.merge(self.clientes_df, left_on='CodCliente', right_on='COD CLIENTE', how='left')
        
        # Calcular porcentaje de cartera vencida
        cartera_vencida = analisis_df[analisis_df['Estado'] == 'Vencida']['Pendiente'].sum()
        pct_cartera_vencida = (cartera_vencida / total_pendiente * 100) if total_pendiente > 0 else 0
        
        # Almacenar resultados
        self.analisis_df = analisis_df
        self.metricas = {
            'total_facturado': total_facturado,
            'total_pagado': total_pagado,
            'total_pendiente': total_pendiente,
            'pct_cartera_vencida': pct_cartera_vencida
        }
        
        return self.metricas
    
    def generar_dashboard(self, ruta_salida='dashboard_ventas.pdf'):
        """Genera un dashboard completo con todas las visualizaciones"""
        if not hasattr(self, 'analisis_df'):
            self.calcular_metricas()
            
        # Crear PDF con múltiples páginas
        with PdfPages(ruta_salida) as pdf:
            # Página 1: KPIs y gráficos principales
            fig = plt.figure(figsize=(11, 8.5))
            fig.suptitle('Dashboard de Análisis de Facturas y Cartera', fontsize=16, y=0.98)
            
            # KPIs
            ax1 = plt.subplot2grid((4, 6), (0, 0), colspan=2)
            ax1.text(0.5, 0.5, f"Total Facturado\n${self.metricas['total_facturado']:,.2f}", 
                    horizontalalignment='center', verticalalignment='center', fontsize=12)
            ax1.axis('off')
            
            ax2 = plt.subplot2grid((4, 6), (0, 2), colspan=2)
            ax2.text(0.5, 0.5, f"Total Pagado\n${self.metricas['total_pagado']:,.2f}", 
                    horizontalalignment='center', verticalalignment='center', fontsize=12)
            ax2.axis('off')
            
            ax3 = plt.subplot2grid((4, 6), (0, 4), colspan=2)
            ax3.text(0.5, 0.5, f"Total Pendiente\n${self.metricas['total_pendiente']:,.2f}", 
                    horizontalalignment='center', verticalalignment='center', fontsize=12)
            ax3.axis('off')
            
            # Evolución mensual de facturación
            ax4 = plt.subplot2grid((4, 6), (1, 0), colspan=3, rowspan=2)
            self.facturas_df['Mes'] = self.facturas_df['Fecha Facturación'].dt.strftime('%b-%y')
            evolucion = self.facturas_df.groupby('Mes')['Valor'].sum().reset_index()
            # Ordenar por fecha
            meses_orden = pd.to_datetime(self.facturas_df['Fecha Facturación']).dt.to_period('M').unique()
            meses_orden = [str(m).replace('M', 'b-').lower() for m in meses_orden]
            evolucion['Mes'] = pd.Categorical(evolucion['Mes'], categories=meses_orden, ordered=True)
            evolucion = evolucion.sort_values('Mes')
            
            ax4.plot(evolucion['Mes'], evolucion['Valor'], 'o-', linewidth=2)
            ax4.set_title('Evolución Mensual de Facturación')
            plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)
            ax4.set_ylabel('Valor Facturado ($)')
            
            # Estado de cartera (pastel)
            ax5 = plt.subplot2grid((4, 6), (1, 3), colspan=3, rowspan=2)
            estado_cartera = self.analisis_df.groupby('Estado')['Pendiente'].sum().reset_index()
            colores = {'Pagada': 'green', 'Por vencer': 'blue', 'Próxima a vencer': 'orange', 'Vencida': 'red'}
            colores_grafico = [colores[estado] for estado in estado_cartera['Estado']]
            ax5.pie(estado_cartera['Pendiente'], labels=estado_cartera['Estado'], autopct='%1.1f%%', 
                   shadow=True, startangle=90, colors=colores_grafico)
            ax5.set_title('Estado de Cartera')
            ax5.axis('equal')  # Para asegurar que el pastel es circular
            
            # Top clientes
            ax6 = plt.subplot2grid((4, 6), (3, 0), colspan=3)
            top_clientes = self.analisis_df.groupby('NOMBRE CLIENTE')['Valor'].sum().sort_values(ascending=False).head(5)
            top_clientes.plot(kind='barh', ax=ax6, color='darkblue')
            ax6.set_title('Top 5 Clientes por Valor Facturado')
            ax6.set_xlabel('Valor Facturado ($)')
            
            # Antigüedad de cartera
            ax7 = plt.subplot2grid((4, 6), (3, 3), colspan=3)
            antiguedad = self.analisis_df[self.analisis_df['Pendiente'] > 0].groupby('Rango_Edad')['Pendiente'].sum().reset_index()
            # Ordenar por rango de edad
            orden_rangos = self.rango_edad_df.sort_values('Orden')['Edad'].tolist()
            antiguedad['Rango_Edad'] = pd.Categorical(antiguedad['Rango_Edad'], categories=orden_rangos, ordered=True)
            antiguedad = antiguedad.sort_values('Rango_Edad')
            
            colores_antiguedad = plt.cm.YlOrRd(np.linspace(0.2, 0.8, len(antiguedad)))
            ax7.bar(antiguedad['Rango_Edad'], antiguedad['Pendiente'], color=colores_antiguedad)
            ax7.set_title('Antigüedad de Cartera')
            ax7.set_ylabel('Valor Pendiente ($)')
            plt.setp(ax7.xaxis.get_majorticklabels(), rotation=45)
            
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            pdf.savefig(fig)
            plt.close()
            
            # Página 2: Análisis detallado de cartera
            fig = plt.figure(figsize=(11, 8.5))
            fig.suptitle('Análisis Detallado de Cartera', fontsize=16, y=0.98)
            
            # Facturas por estado
            ax1 = plt.subplot2grid((2, 2), (0, 0))
            conteo_estados = self.analisis_df['Estado'].value_counts()
            ax1.bar(conteo_estados.index, conteo_estados.values, color=['green', 'blue', 'orange', 'red'])
            ax1.set_title('Número de Facturas por Estado')
            ax1.set_ylabel('Cantidad de Facturas')
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
            
            # Distribución de días de vencimiento
            ax2 = plt.subplot2grid((2, 2), (0, 1))
            sns.histplot(self.analisis_df['Dias_Vencimiento'].clip(-60, 120), bins=12, kde=True, ax=ax2)
            ax2.set_title('Distribución de Días de Vencimiento')
            ax2.set_xlabel('Días (valores negativos = por vencer)')
            
            # Tabla de antigüedad
            ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
            ax3.axis('tight')
            ax3.axis('off')
            
            # Crear tabla de antigüedad
            antiguedad_data = self.analisis_df[self.analisis_df['Pendiente'] > 0].groupby('Rango_Edad').agg(
                Valor=('Pendiente', 'sum'),
                Porcentaje=('Pendiente', lambda x: x.sum() / self.metricas['total_pendiente'] * 100 if self.metricas['total_pendiente'] > 0 else 0),
                Facturas=('NUMFACT', 'count')
            ).reset_index()
            
            antiguedad_data['Rango_Edad'] = pd.Categorical(antiguedad_data['Rango_Edad'], categories=orden_rangos, ordered=True)
            antiguedad_data = antiguedad_data.sort_values('Rango_Edad')
            
            tabla_data = []
            for _, row in antiguedad_data.iterrows():
                tabla_data.append([
                    row['Rango_Edad'],
                    f"${row['Valor']:,.2f}",
                    f"{row['Porcentaje']:.1f}%",
                    int(row['Facturas'])
                ])
            
            tabla = ax3.table(
                cellText=tabla_data,
                colLabels=['Rango de Antigüedad', 'Valor Pendiente', '% del Total', '# Facturas'],
                loc='center',
                cellLoc='center'
            )
            
            tabla.auto_set_font_size(False)
            tabla.set_fontsize(9)
            tabla.scale(1, 1.5)
            
            for (i, j), cell in tabla.get_celld().items():
                if i == 0:  # Encabezados
                    cell.set_text_props(fontproperties=dict(weight='bold'))
                if j == 2:  # Porcentaje
                    cell.set_text_props(ha='right')
                if j == 1:  # Valores
                    cell.set_text_props(ha='right')
            
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            pdf.savefig(fig)
            plt.close()
            
            # Página 3: Análisis por Cliente
            fig = plt.figure(figsize=(11, 8.5))
            fig.suptitle('Análisis por Cliente', fontsize=16, y=0.98)
            
            # Estado de facturas por cliente (top 10)
            ax1 = plt.subplot2grid((2, 1), (0, 0))
            top10_clientes = self.analisis_df.groupby('NOMBRE CLIENTE')['Valor'].sum().sort_values(ascending=False).head(10).index
            df_top10 = self.analisis_df[self.analisis_df['NOMBRE CLIENTE'].isin(top10_clientes)]
            
            estado_por_cliente = pd.crosstab(df_top10['NOMBRE CLIENTE'], df_top10['Estado'])
            estado_por_cliente = estado_por_cliente.reindex(columns=['Pagada', 'Por vencer', 'Próxima a vencer', 'Vencida'], fill_value=0)
            
            estado_por_cliente.plot(kind='bar', stacked=True, ax=ax1, 
                                   color=[colores[c] for c in estado_por_cliente.columns])
            ax1.set_title('Estado de Facturas por Cliente (Top 10)')
            ax1.set_ylabel('Número de Facturas')
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
            ax1.legend(title='Estado')
            
            # Cartera pendiente por cliente
            ax2 = plt.subplot2grid((2, 1), (1, 0))
            pendiente_por_cliente = self.analisis_df[self.analisis_df['Pendiente'] > 0].groupby('NOMBRE CLIENTE')['Pendiente'].sum().sort_values(ascending=False).head(10)
            pendiente_por_cliente.plot(kind='bar', ax=ax2, color='darkred')
            ax2.set_title('Top 10 Clientes con Mayor Cartera Pendiente')
            ax2.set_ylabel('Valor Pendiente ($)')
            plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
            
            for i, v in enumerate(pendiente_por_cliente):
                ax2.text(i, v * 1.01, f"${v:,.0f}", ha='center', va='bottom', fontsize=8)
            
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            pdf.savefig(fig)
            plt.close()
            
        print(f"Dashboard generado en: {ruta_salida}")
        return ruta_salida

    def exportar_excel(self, ruta_salida='analisis_ventas.xlsx'):
        """Exporta todos los datos a Excel con múltiples hojas"""
        if not hasattr(self, 'analisis_df'):
            self.calcular_metricas()
            
        # Crear writer
        writer = pd.ExcelWriter(ruta_salida, engine='xlsxwriter')
        
        # Exportar datos originales
        self.clientes_df.to_excel(writer, sheet_name='Clientes', index=False)
        self.facturas_df.to_excel(writer, sheet_name='Facturas', index=False)
        self.pagos_df.to_excel(writer, sheet_name='Pagos', index=False)
        
        # Exportar análisis
        self.analisis_df.to_excel(writer, sheet_name='Análisis Completo', index=False)
        
        # Crear resumen de métricas
        metricas_df = pd.DataFrame({
            'Métrica': ['Total Facturado', 'Total Pagado', 'Total Pendiente', '% Cartera Vencida'],
            'Valor': [
                f"${self.metricas['total_facturado']:,.2f}",
                f"${self.metricas['total_pagado']:,.2f}",
                f"${self.metricas['total_pendiente']:,.2f}",
                f"{self.metricas['pct_cartera_vencida']:.2f}%"
            ]
        })
        metricas_df.to_excel(writer, sheet_name='Resumen', index=False)
        
        # Exportar tablas de resumen
        # Estado de cartera
        estado_cartera = self.analisis_df.groupby('Estado').agg(
            Valor=('Pendiente', 'sum'),
            Porcentaje=('Pendiente', lambda x: x.sum() / self.metricas['total_pendiente'] * 100 if self.metricas['total_pendiente'] > 0 else 0),
            Facturas=('NUMFACT', 'count')
        ).reset_index()
        estado_cartera.to_excel(writer, sheet_name='Estado Cartera', index=False)
        
        # Antigüedad de cartera
        antiguedad = self.analisis_df[self.analisis_df['Pendiente'] > 0].groupby('Rango_Edad').agg(
            Valor=('Pendiente', 'sum'),
            Porcentaje=('Pendiente', lambda x: x.sum() / self.metricas['total_pendiente'] * 100 if self.metricas['total_pendiente'] > 0 else 0),
            Facturas=('NUMFACT', 'count')
        ).reset_index()
        orden_rangos = self.rango_edad_df.sort_values('Orden')['Edad'].tolist()
        antiguedad['Rango_Edad'] = pd.Categorical(antiguedad['Rango_Edad'], categories=orden_rangos, ordered=True)
        antiguedad = antiguedad.sort_values('Rango_Edad')
        antiguedad.to_excel(writer, sheet_name='Antigüedad Cartera', index=False)
        
        # Top clientes
        top_clientes = self.analisis_df.groupby('NOMBRE CLIENTE').agg(
            Total_Facturado=('Valor', 'sum'),
            Total_Pagado=('Total_Pagado', 'sum'),
            Total_Pendiente=('Pendiente', 'sum'),
            Facturas=('NUMFACT', 'count')
        ).reset_index()
        top_clientes = top_clientes.sort_values('Total_Facturado', ascending=False)
        top_clientes.to_excel(writer, sheet_name='Top Clientes', index=False)
        
        # Guardar y cerrar
        writer.close()
        print(f"Análisis exportado a Excel en: {ruta_salida}")
        return ruta_salida

# Función para ejecutar el modelo completo
def ejecutar_modelo(ruta_clientes, ruta_facturas, ruta_pagos, ruta_rango_edad, ruta_output='resultados'):
    """Ejecuta el modelo completo de análisis"""
    # Crear carpeta de resultados si no existe
    if not os.path.exists(ruta_output):
        os.makedirs(ruta_output)
    
    # Inicializar el modelo
    modelo = ModeloAnalisisVentas()
    
    # Cargar datos
    modelo.cargar_desde_excel(ruta_clientes, ruta_facturas, ruta_pagos, ruta_rango_edad)
    
    # Calcular métricas
    metricas = modelo.calcular_metricas()
    print("\n== Métricas del Análisis ==")
    print(f"Total Facturado: ${metricas['total_facturado']:,.2f}")
    print(f"Total Pagado: ${metricas['total_pagado']:,.2f}")
    print(f"Total Pendiente: ${metricas['total_pendiente']:,.2f}")
    print(f"% Cartera Vencida: {metricas['pct_cartera_vencida']:.2f}%")
    
    # Generar dashboard
    ruta_dashboard = os.path.join(ruta_output, 'dashboard_ventas.pdf')
    modelo.generar_dashboard(ruta_dashboard)
    
    # Exportar a Excel
    ruta_excel = os.path.join(ruta_output, 'analisis_ventas.xlsx')
    modelo.exportar_excel(ruta_excel)
    
    return {
        'metricas': metricas,
        'ruta_dashboard': ruta_dashboard,
        'ruta_excel': ruta_excel
    }

# Ejemplo de uso
if __name__ == "__main__":
    # Definir rutas de archivos
    ruta_clientes = "data\\Clientess.xlsx"
    ruta_facturas = "Facturas.xlsx"
    ruta_pagos = "Facturas Pagos.xlsx"
    ruta_rango_edad = "Rango Edad.xlsx"
    
    # Ejecutar modelo
    resultados = ejecutar_modelo(
        ruta_clientes=ruta_clientes,
        ruta_facturas=ruta_facturas,
        ruta_pagos=ruta_pagos,
        ruta_rango_edad=ruta_rango_edad
    )
    
    print("\n== Análisis completado ==")
    print(f"Dashboard generado en: {resultados['ruta_dashboard']}")
    print(f"Excel con análisis en: {resultados['ruta_excel']}")