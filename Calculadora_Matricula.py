import streamlit as st

# --- CSS personalizado ---
st.markdown("""
    <style>
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .block-container {
        text-align: center;
        max-width: 500px;
        margin: auto;
    }
    input {
        font-size: 20px !important;
        padding: 10px !important;
        text-align: center;
    }
    button {
        font-size: 18px !important;
        padding: 12px 20px !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Valores por año ---
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

# --- Inscripción por año ---
valores_inscripcion = {
    "2006-1": 60000, "2006-2": 60000, "2007-1": 61000, "2007-2": 61000,
    "2008-1": 65000, "2009-1": 70000, "2010-1": 72000, "2011-1": 75000,
    "2012-1": 79000, "2013-1": 82000, "2014": 87000, "2015": 90000,
    "2016": 97000, "2017": 103000, "2018": 109000, "2019": 116000,
    "2020": 123000, "2021": 127000, "2022": 140000, "2023": 162000,
    "2024": 182000, "2025": 199000
}

# --- Interfaz principal ---
st.title("Calculadora de Créditos y Matrícula")

valor_total = st.number_input("Valor total de la matrícula", min_value=0, step=1000)
total_creditos = st.number_input("Número total de créditos", min_value=1, step=1)

options_anos = list(valores.keys())
ano = st.selectbox("Selecciona el año de la matrícula", options=options_anos)

valores_ano = valores.get(ano, {})
tipos_disponibles = sorted([
    t for t in ["pregrado", "especializacion", "maestria", "tecnologia"]
    if t in valores_ano and valores_ano.get(t, [0])[0] > 0
])

if not tipos_disponibles:
    tipos_disponibles = ["pregrado"]

tipo_estudio = st.selectbox("Selecciona el tipo de estudio", options=tipos_disponibles)

valor_inscripcion = valores_inscripcion.get(ano, 0)
valor_seguro = 9000

valores_credito = valores_ano.get(tipo_estudio, [0])

st.write(f"**Valores de referencia para {ano} y {tipo_estudio.capitalize()}:**")
if tipo_estudio in ["pregrado", "tecnologia"]:
    if len(valores_credito) == 2:
        st.write(f"Crédito Tipo 1: ${valores_credito[0]:,}, Crédito Tipo 2: ${valores_credito[1]:,}")
    else:
        st.write(f"Valor de Crédito único: ${valores_credito[0]:,}")
else:
    st.write(f"Valor de Crédito: ${valores_credito[0]:,}")

st.write(f"Valor de Inscripción (Referencia): ${valor_inscripcion:,}")
st.write(f"Valor del Seguro (Fijo): ${valor_seguro:,}")

# --- Cálculo de créditos ---
if st.button("Calcular"):
    solucion_encontrada = False

    if not valores_credito or valores_credito[0] == 0:
        st.error(f"No hay valores de crédito definidos para '{tipo_estudio}' en '{ano}'.")

    elif tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
        v1, v2 = valores_credito
        for x in range(total_creditos + 1):
            y = total_creditos - x
            if v1 * x + v2 * y == valor_total:
                st.success(f"El estudiante matriculó {x} créditos de **${v1:,}** y {y} créditos de **${v2:,}**.")
                solucion_encontrada = True
                break

    elif tipo_estudio in ["especializacion", "maestria"] and len(valores_credito) >= 1:
        v1 = valores_credito[0]
        calculado = total_creditos * v1

        if calculado == valor_total:
            st.success(f"El estudiante matriculó **{total_creditos}** créditos, todos valorados en **${v1:,}**.")
            solucion_encontrada = True

        elif valor_total > 0 and v1 > 0 and valor_total % v1 == 0:
            creditos_calculados = valor_total // v1
            st.success(f"Según el valor total (${valor_total:,}) y el costo del crédito (${v1:,}), se calcularon **{creditos_calculados}** créditos.")
            st.info(f"El número de créditos introducido fue **{total_creditos}**, lo cual no coincide con el cálculo. La matrícula corresponde a {creditos_calculados} créditos.")
            solucion_encontrada = True

        elif abs(calculado - valor_total) <= 1000:
            st.warning(f"El valor ingresado (${valor_total:,}) está muy cerca de lo esperado (${calculado:,}), puede haber un pequeño error de redondeo o digitación.")
            solucion_encontrada = True

        else:
            st.error(f"El valor total ingresado no coincide con el costo por crédito. Revísalo.")

    if not solucion_encontrada:
        st.error("No existe una combinación exacta de créditos que sume el valor total ingresado.")

       

