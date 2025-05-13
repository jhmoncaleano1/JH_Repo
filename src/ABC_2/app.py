#streamlit
import streamlit as st
from procesamiento import cargar_datos

def main():
    st.title("Dashboard de Ventas")
    df = cargar_datos()
    st.dataframe(df)
    st.bar_chart(df.set_index("cliente"))

if __name__ == "__main__":
    main()
