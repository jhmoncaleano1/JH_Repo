import streamlit as st

def mostrar_factura_en_streamlit(factura):
    st.title(f"Factura #{factura.factura_id}")
    st.write(f"Fecha: {factura.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(factura.cliente_empleado.datos_completos())

    st.subheader("Productos")
    total = 0
    for producto, cantidad in factura.items:
        subtotal = producto.precio * cantidad
        st.write(f"{producto.nombre} x{cantidad} = ${subtotal:.2f}")
        total += subtotal

    st.write("---")
    st.success(f"Total a pagar: ${total:.2f}")
