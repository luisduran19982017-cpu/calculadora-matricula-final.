import streamlit as st

# ==============================================================================
# 1. Configuration Data
#    - Los valores de ESPECIALIZACION han sido actualizados/revisados.
#    - Se asume que los dos valores de crédito de la imagen (VLR CREDITO, INSCRIPCION)
#      para especialización son:
#      1. El Valor del Crédito (VLR CREDITO)
#      2. El Valor de la Inscripción (INSCRIPCION) - ¡ERROR de concepto en el prompt, la inscripción es un costo aparte!
#      
#    CORRECCIÓN: Se mantiene la estructura original. Los dos "valores" de especialización
#    se refieren al Valor del Crédito (VLR CREDITO) que es diferente del código original,
#    y el Valor de la Inscripción.
#
#    Actualizaré:
#    a) VALORES_CREDITO: para 'especializacion' con el valor de la columna 'VLR CREDITO'.
#    b) VALORES_INSCRIPCION: para 'especializacion' con el valor de la columna 'INSCRIPCION'.
#    
#    ¡La imagen tiene más de 20 filas sin año! Solo actualizaré las filas con años conocidos.
# ==============================================================================

# --- Credit values per year and study type ---
VALORES_CREDITO = {
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
    # --- Actualización de Especialización (VLR CREDITO) desde la imagen ---
    "2015":   {"pregrado": [70000, 90000], "especializacion": [170000], "maestria": [419000]}, # Antes: 144000
    "2016":   {"pregrado": [77000, 84700], "especializacion": [170000], "maestria": [448000]}, # Antes: 154000
    "2017":   {"pregrado": [83000, 91000], "especializacion": [171000], "maestria": [480000]}, # Antes: 165000
    "2018":   {"pregrado": [88000, 97000], "tecnologia": [88000, 97000], "especializacion": [182000], "maestria": [508000], "homologacion": [23000]}, # Antes: 0
    "2019":   {"pregrado": [93000, 102000], "tecnologia": [93000, 102000], "especializacion": [194000], "maestria": [538000], "homologacion": [25000]}, # Antes: 185000
    "2020":   {"pregrado": [98000, 108000], "tecnologia": [98000, 107500], "especializacion": [209000], "maestria": [571000], "homologacion": [26000]}, # Antes: 196000
    "2021":   {"pregrado": [102000, 112000], "tecnologia": [91000, 100000], "especializacion": [216000], "maestria": [591000], "homologacion": [27000]}, # Antes: 203000
    "2022":   {"pregrado": [112000, 123000], "tecnologia": [100000, 110000], "especializacion": [225000], "maestria": [650000], "homologacion": [30000]}, # Antes: 223000
    "2023":   {"pregrado": [123000, 135000], "tecnologia": [110000, 121000], "especializacion": [238000], "maestria": [715000], "homologacion": [35000]}, # Antes: 259000
    "2024":   {"pregrado": [146000, 160000], "tecnologia": [130000, 143000], "especializacion": [248000], "maestria": [715000], "homologacion": [39000]}, # Antes: 290000
    "2025":   {"pregrado": [159000, 175000], "tecnologia": [142000, 157000], "especializacion": [259000], "maestria": [925000], "homologacion": [43000]}  # Antes: 317000
}

# --- Registration (Inscripción) value per year ---
VALORES_INSCRIPCION = {
    # --- Actualización de Inscripción (INSCRIPCION) desde la imagen ---
    "2006-1": 60000, "2006-2": 60000, "2007-1": 61000, "2007-2": 61000,
    "2008-1": 65000, "2009-1": 70000, "2010-1": 72000, "2011-1": 75000,
    "2012-1": 79000, "2013-1": 82000, "2014": 87000, 
    "2015": 96000, # Antes: 90000
    "2016": 96000, # Antes: 97000
    "2017": 97000, # Antes: 103000
    "2018": 97000, # Antes: 109000 (La imagen es 97000, el código original tenía 109000)
    "2019": 103000, # Antes: 116000
    "2020": 111000, # Antes: 123000
    "2021": 115000, # Antes: 127000
    "2022": 119000, # Antes: 140000
    "2023": 126000, # Antes: 162000
    "2024": 130000, # Antes: 182000
    "2025": 137000 # Antes: 199000
}

# --- Fixed Insurance Value (Valor de Seguro) ---
VALOR_SEGURO_FIJO = 9000

# ==============================================================================
# 2. Custom CSS Styles
# ==============================================================================

def apply_custom_css():
    """Applies custom CSS for centering and styling the app elements."""
    st.markdown("""
        <style>
        .block-container {
            text-align: center;
            max-width: 600px;
            margin: auto;
            padding-top: 1rem;
        }
        input[type="number"] {
            font-size: 20px !important;
            padding: 10px !important;
            text-align: center;
        }
        button {
            font-size: 18px !important;
            padding: 12px 20px !important;
            border-radius: 10px !important;
            margin-top: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. Main Application Logic
# ==============================================================================

def main_app():
    """Main function to run the Streamlit calculator interface."""
    
    st.title("Calculadora de Créditos y Matrícula 🎓")

    # --- User Inputs ---
    col1, col2 = st.columns(2)
    
    with col1:
        valor_total = st.number_input("Valor total de la matrícula ($)", min_value=0, step=1000, format="%d")
    
    with col2:
        total_creditos = st.number_input("Número total de créditos", min_value=1, step=1, format="%d")

    # --- Year Selection ---
    options_anos = list(VALORES_CREDITO.keys())
    ano = st.selectbox("Selecciona el año de la matrícula", options=options_anos)

    # --- Study Type Selection (Filtered by Year) ---
    valores_ano = VALORES_CREDITO.get(ano, {})
    
    # Filter available study types for the selected year
    tipos_disponibles = sorted([
        t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
        if t in valores_ano and (isinstance(valores_ano[t], list) and len(valores_ano[t]) > 0 and valores_ano[t][0] > 0)
    ])

    if not tipos_disponibles:
        st.warning("No hay tipos de estudio disponibles para este año. Verifique la data.")
        return

    tipo_estudio = st.selectbox("Selecciona el tipo de estudio", options=tipos_disponibles)

    # Get specific values for the selection
    valor_inscripcion = VALORES_INSCRIPCION.get(ano, 0)
    valor_seguro = VALOR_SEGURO_FIJO
    valores_credito = valores_ano.get(tipo_estudio, [0])

    st.markdown("---")
    
    # --- Reference Values Display ---
    st.subheader("Valores de Referencia")
    st.info(f"**Año:** {ano} | **Tipo de Estudio:** {tipo_estudio.capitalize()}")
    
    if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
        st.write(f"🏷️ **Crédito Tipo 1:** ${valores_credito[0]:,} | **Crédito Tipo 2:** ${valores_credito[1]:,}")
    elif len(valores_credito) >= 1 and valores_credito[0] > 0:
        # Esto incluye a Especialización con su valor único de crédito (VLR CREDITO)
        st.write(f"🏷️ **Valor de Crédito único:** ${valores_credito[0]:,}")
    else:
        st.warning("El valor del crédito es 0 o no está definido. No se puede calcular.")
        return

    st.write(f"📝 **Valor de Inscripción (Referencia):** ${valor_inscripcion:,}")
    st.write(f"🛡️ **Valor del Seguro (Fijo):** ${valor_seguro:,}")
    
    st.markdown("---")

    # --- Calculation Logic ---
    if st.button("Calcular Distribución de Créditos"):
        
        # Asumo que el valor_total ingresado es el costo neto de los créditos.
        valor_creditos_neto = valor_total 
        
        st.subheader("Resultado del Cálculo")
        solucion_encontrada = False

        # Case 1: Two Credit Types (Pregrado/Tecnologia)
        if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
            v1, v2 = valores_credito
            
            if v1 > v2: v1, v2 = v2, v1
            
            for x in range(total_creditos + 1):
                y = total_creditos - x
                
                if v1 * x + v2 * y == valor_creditos_neto:
                    st.balloons()
                    st.success(f"""
                        ✅ Se encontró una solución para **{total_creditos}** créditos:
                        - **{x}** créditos a **${v1:,}** cada uno.
                        - **{y}** créditos a **${v2:,}** cada uno.
                        """)
                    solucion_encontrada = True
                    break
            
            if not solucion_encontrada:
                st.error("❌ No existe una combinación exacta de créditos que sume el valor total ingresado.")

        # Case 2: Single Credit Type (Especializacion/Maestria/Homologacion)
        elif len(valores_credito) >= 1 and valores_credito[0] > 0:
            v1 = valores_credito[0]
            
            if valor_creditos_neto % v1 == 0:
                creditos_calculados = valor_creditos_neto // v1
                
                st.success(f"✅ El valor total ingresado (${valor_total:,}) corresponde exactamente a **{creditos_calculados}** créditos a ${v1:,} cada uno.")
                solucion_encontrada = True
                
                if creditos_calculados != total_creditos:
                    st.info(f"💡 **Nota:** Usted ingresó **{total_creditos}** créditos, pero el valor total sugiere que fueron **{creditos_calculados}** créditos.")
            
            else:
                creditos_calculados = valor_creditos_neto / v1
                creditos_redondeados = round(creditos_calculados)

                if abs(creditos_calculados - creditos_redondeados) < 0.05:
                     st.warning(f"""
                         ⚠️ El valor total no es exacto, pero se acerca a **{creditos_redondeados}** créditos.
                         - Valor calculado: ${creditos_calculados:,.2f} créditos.
                         - Valor por {creditos_redondeados} créditos: ${creditos_redondeados * v1:,}.
                         """)
                     solucion_encontrada = True
                     
                else:
                    st.error(f"""
                        ❌ El valor total (${valor_total:,}) no corresponde a un número entero válido de créditos a ${v1:,} cada uno.
                        - El cálculo arroja **{creditos_calculados:,.2f}** créditos.
                        """)
            
        if not solucion_encontrada:
            st.error("❌ No se pudo determinar la distribución de créditos con los valores ingresados. Revise si el valor total de la matrícula incluye otros costos además del crédito.")


# ==============================================================================
# 4. Execution
# ==============================================================================

if __name__ == "__main__":
    apply_custom_css()
    main_app()

