import streamlit as st
 
# --- CSS personalizado ---
st.markdown("""
    <style>
    /* Centrar todo */
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
 
    /* Contenedor */
    .block-container {
        text-align: center;
        max-width: 500px;
        margin: auto;
    }
 
    /* Inputs más grandes */
    input {
        font-size: 20px !important;
        padding: 10px !important;
        text-align: center;
    }
 
    /* Botón más grande */
    button {
        font-size: 18px !important;
        padding: 12px 20px !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)
 
# --- Diccionario de valores por año (2006-2025) ---
valores = {
    "2006-1": {"pregrado": [43000, 60000], "especializacion": [96000]},
    "2006-2": {"pregrado": [46000, 60000], "especializacion": [96000]},
    "2007-1": {"pregrado": [46000, 61000], "especializacion": [97000]},
    "2007-2": {"pregrado": [49000, 61000], "especializacion": [97000]},
    "2008-1": {"pregrado": [52000, 65000], "especializacion": [103000]},
    "2009-1": {"pregrado": [56000, 70000], "especializacion": [111000]},
    "2010-1": {"pregrado": [58000, 72000], "especializacion": [115000]},
    "2011-1": {"pregrado": [60000, 75000], "especializacion": [119000]},
    "2012-1": {"pregrado": [63000, 79000], "especializacion": [126000]},
    "2013-1": {"pregrado": [66000, 82000], "especializacion": [130000]},
    "2014":   {"pregrado": [69000, 87000], "especializacion": [137000]},
    "2015":   {"pregrado": [70000, 90000], "especializacion": [144000], "maestria": [419000]},
    "2016":   {"pregrado": [77000, 84700], "especializacion": [154000], "maestria": [448000]},
    "2017":   {"pregrado": [83000, 91000], "especializacion": [165000], "maestria": [480000]},
    "2018":   {"pregrado": [88000, 97000], "tecnologia": [88000, 97000], "especializacion": [0], "maestria": [508000], "homologacion": [23000]},
    "2019":   {"pregrado": [93000, 102000], "tecnologia": [93000, 102000], "especializacion": [185000], "maestria": [538000], "homologacion": [25000]},
    "2020":   {"pregrado": [98000, 108000], "tecnologia": [98000, 107500], "especializacion": [196000], "maestria": [571000], "homologacion": [26000]},
    "2021":   {"pregrado": [102000, 112000], "tecnologia": [91000, 100000], "especializacion": [203000], "maestria": [591000], "homologacion": [27000]},
    "2022":   {"pregrado": [112000, 123000], "tecnologia": [100000, 110000], "especializacion": [223000], "maestria": [650000], "homologacion": [30000]},
    "2023":   {"pregrado": [123000, 135000], "tecnologia": [110000, 121000], "especializacion": [259000], "maestria": [715000], "homologacion": [35000]},
    "2024":   {"pregrado": [146000, 160000], "tecnologia": [130000, 143000], "especializacion": [290000], "maestria": [715000], "homologacion": [39000]},
    "2025":   {"pregrado": [159000, 175000], "tecnologia": [142000, 157000], "especializacion": [317000], "maestria": [925000], "homologacion": [43000]}
}
 
# --- Diccionario de inscripción pregrado ---
valores_inscripcion = {
    "2006-1": 60000,
    "2006-2": 60000,
    "2007-1": 61000,
    "2007-2": 61000,
    "2008-1": 65000,
    "2009-1": 70000,
    "2010-1": 72000,
    "2011-1": 75000,
    "2012-1": 79000,
    "2013-1": 82000,
    "2014":   87000,
    "2015":   90000,
    "2016":   97000,
    "2017":   103000,
    "2018":   109000,
    "2019":   116000,
    "2020":   123000,
    "2021":   127000,
    "2022":   140000,
    "2023":   162000,
    "2024":   182000,
    "2025":   199000
}
 
# --- Interfaz Streamlit ---
st.title("Calculadora de Créditos y Matrícula")
 
# Entradas
valor_total = st.number_input("Valor total de la matrícula", min_value=0, step=1000)
total_creditos = st.number_input("Número total de créditos", min_value=1, step=1)
 
# Entrada para el año de la matrícula
ano = st.selectbox("Selecciona el año de la matrícula", options=list(valores.keys()))
 
# Selección del tipo de matrícula (Pregrado, Especialización, Maestría, Tecnología)
tipo_estudio = st.selectbox("Selecciona el tipo de estudio", options=["pregrado", "especializacion", "maestria", "tecnologia"])
 
# Obtener los valores correspondientes según el año y el tipo de estudio
valores_ano = valores.get(ano, {"pregrado": [0], "especializacion": [0], "tecnologia": [0], "maestria": [0], "homologacion": [0]})
valor_inscripcion = valores_inscripcion.get(ano, 0)  # Obtener el valor de inscripción según el año
valor_seguro = 9000  # El seguro siempre vale 9000 en todos los años
 
# Mostrar los valores automáticamente según el año y el tipo de estudio
st.write(f"**Valores para el año {ano} y tipo de estudio {tipo_estudio.capitalize()}:**")
 
# Valores del tipo de estudio seleccionado
if tipo_estudio == "pregrado":
    st.write(f"Valor de Créditos de Pregrado: {valores_ano['pregrado']}")
elif tipo_estudio == "especializacion":
    st.write(f"Valor de Créditos de Especialización: {valores_ano['especializacion']}")
elif tipo_estudio == "maestria":
    st.write(f"Valor de Créditos de Maestría: {valores_ano['maestria']}")
elif tipo_estudio == "tecnologia":
    st.write(f"Valor de Créditos de Tecnología: {valores_ano['tecnologia']}")
 
st.write(f"Valor de Inscripción (Pregrado): {valor_inscripcion:,}")
st.write(f"Valor del Seguro: {valor_seguro:,}")
 
if st.button("Calcular"):
    solucion_encontrada = False
    # Ajustamos el cálculo según el tipo de estudio seleccionado
    if tipo_estudio == "pregrado":
        for x in range(total_creditos + 1):
            y = total_creditos - x
            # Verificamos las combinaciones posibles para los créditos de pregrado
            if valores_ano["pregrado"][0] * x + valores_ano["pregrado"][1] * y == valor_total:
                st.success(f"El estudiante matriculó {x} créditos de {valores_ano['pregrado'][0]:,} y {y} créditos de {valores_ano['pregrado'][1]:,}.")
                solucion_encontrada = True
                break
    elif tipo_estudio == "especializacion":
        for x in range(total_creditos + 1):
            y = total_creditos - x
            if valores_ano["especializacion"][0] * x == valor_total:
                st.success(f"El estudiante matriculó {x} créditos de especialización.")
                solucion_encontrada = True
                break
    elif tipo_estudio == "maestria":
        for x in range(total_creditos + 1):
            y = total_creditos - x
            if valores_ano["maestria"][0] * x == valor_total:
                st.success(f"El estudiante matriculó {x} créditos de maestría.")
                solucion_encontrada = True
                break
    elif tipo_estudio == "tecnologia":
        for x in range(total_creditos + 1):
            y = total_creditos - x
            if valores_ano["tecnologia"][0] * x == valor_total:
                st.success(f"El estudiante matriculó {x} créditos de tecnología.")
                solucion_encontrada = True
                break
 
    if not solucion_encontrada:
        st.error("No existe una combinación exacta con esos datos.")
 
    # Mostrar los valores adicionales (inscripción, seguro)
