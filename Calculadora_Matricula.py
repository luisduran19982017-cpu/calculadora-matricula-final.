import streamlit as st

# ==============================================================================
# 1. Configuration Data
#    
#    Valores de Crédito (no modificados, se mantienen los anteriores).
#    ¡Nuevos Valores de Inscripción según la imagen proporcionada!
# ==============================================================================

# --- Credit values per year and study type (MAINTAINED FROM PREVIOUS VERSION) ---
VALORES_CREDITO = {
    # Valores de Crédito (VLR CREDITO)
    "2006-1": {"pregrado": [43000, 60000], "especializacion": [170000]},
    "2006-2": {"pregrado": [46000, 60000], "especializacion": [170000]},
    "2007-1": {"pregrado": [46000, 61000], "especializacion": [171000]},
    "2007-2": {"pregrado": [49000, 61000], "especializacion": [182000]},
    "2008-1": {"pregrado": [52000, 65000], "especializacion": [194000]},
    "2009-1": {"pregrado": [56000, 70000], "especializacion": [209000]},
    "2010-1": {"pregrado": [58000, 72000], "especializacion": [216000]},
    "2011-1": {"pregrado": [60000, 75000], "especializacion": [225000]},
    "2012-1": {"pregrado": [63000, 79000], "especializacion": [238000]},
    "2013-1": {"pregrado": [66000, 82000], "especializacion": [248000]},
    "2014":   {"pregrado": [69000, 87000], "especializacion": [259000]},
    
    # Valores de 2015 en adelante (Crédito Especialización y Maestría)
    "2015":   {"pregrado": [70000, 90000], "especializacion": [271000], "maestria": [419000]},
    "2016":   {"pregrado": [77000, 84700], "especializacion": [290000], "maestria": [448000]},
    "2017":   {"pregrado": [83000, 91000], "especializacion": [310000], "maestria": [480000]},
    "2018":   {"pregrado": [88000, 97000], "tecnologia": [88000, 97000], "especializacion": [328000], "maestria": [508000], "homologacion": [23000]},
    "2019":   {"pregrado": [93000, 102000], "tecnologia": [93000, 102000], "especializacion": [348000], "maestria": [538000], "homologacion": [25000]},
    "2020":   {"pregrado": [98000, 108000], "tecnologia": [98000, 107500], "especializacion": [369000], "maestria": [571000], "homologacion": [26000]},
    "2021":   {"pregrado": [102000, 112000], "tecnologia": [91000, 100000], "especializacion": [382000], "maestria": [591000], "homologacion": [27000]},
    "2022":   {"pregrado": [112000, 123000], "tecnologia": [100000, 110000], "especializacion": [420000], "maestria": [650000], "homologacion": [30000]},
    "2023":   {"pregrado": [123000, 135000], "tecnologia": [110000, 121000], "especializacion": [462000], "maestria": [715000], "homologacion": [35000]},
    "2024":   {"pregrado": [146000, 160000], "tecnologia": [130000, 143000], "especializacion": [462000], "maestria": [715000], "homologacion": [39000]},
    "2025":   {"pregrado": [159000, 175000], "tecnologia": [142000, 157000], "especializacion": [598000], "maestria": [925000], "homologacion": [43000]}
}


# --- Registration (Inscripción) value per year and type (UPDATED WITH NEW IMAGE DATA) ---
VALORES_INSCRIPCION_POR_TIPO = {
    "2006-1": {"pregrado": 60000, "especializacion": 96000, "maestria": 0, "tecnologia": 0},
    "2006-2": {"pregrado": 60000, "especializacion": 96000, "maestria": 0, "tecnologia": 0},
    "2007-1": {"pregrado": 61000, "especializacion": 97000, "maestria": 0, "tecnologia": 0},
    "2007-2": {"pregrado": 61000, "especializacion": 97000, "maestria": 0, "tecnologia": 0},
    "2008-1": {"pregrado": 65000, "especializacion": 103000, "maestria": 0, "tecnologia": 0},
    "2009-1": {"pregrado": 70000, "especializacion": 111000, "maestria": 0, "tecnologia": 0},
    "2010-1": {"pregrado": 72000, "especializacion": 115000, "maestria": 0, "tecnologia": 0},
    "2011-1": {"pregrado": 75000, "especializacion": 119000, "maestria": 0, "tecnologia": 0},
    "2012-1": {"pregrado": 79000, "especializacion": 126000, "maestria": 0, "tecnologia": 0},
    "2013-1": {"pregrado": 82000, "especializacion": 130000, "maestria": 0, "tecnologia": 0},
    "2014":   {"pregrado": 87000, "especializacion": 137000, "maestria": 0, "tecnologia": 0},
    "2015":   {"pregrado": 90000, "especializacion": 144000, "maestria": 0, "tecnologia": 0},
    "2016":   {"pregrado": 97000, "especializacion": 154000, "maestria": 0, "tecnologia": 0},
    "2017":   {"pregrado": 103000, "especializacion": 165000, "maestria": 0, "tecnologia": 0},
    "2018":   {"pregrado": 109000, "especializacion": 185000, "maestria": 0, "tecnologia": 109000},
    "2019":   {"pregrado": 116000, "especializacion": 196000, "maestria": 185000, "tecnologia": 116000},
    "2020":   {"pregrado": 123000, "especializacion": 203000, "maestria": 196000, "tecnologia": 123000},
    "2021":   {"pregrado": 127000, "especializacion": 223000, "maestria": 203000, "tecnologia": 127000},
    "2022":   {"pregrado": 140000, "especializacion": 259000, "maestria": 223000, "tecnologia": 140000},
    "2023":   {"pregrado": 162000, "especializacion": 290000, "maestria": 259000, "tecnologia": 162000},
    "2024":   {"pregrado": 182000, "especializacion": 317000, "maestria": 290000, "tecnologia": 182000},
    "2025":   {"pregrado": 199000, "especializacion": 0, "maestria": 317000, "tecnologia": 199000}
}
# Nota: Si Especialización 2025 está vacío en la tabla, se usa 0.

# --- Fixed Insurance Value (Valor de Seguro) ---
VALOR_SEGURO_FIJO = 9000
# Nota: El valor del seguro se mantiene fijo en $9,000, ya que no se proporcionó data nueva.


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
        .stSuccess {
            background-color: #e6ffe6;
            border-left: 5px solid #4CAF50;
            padding: 10px;
            margin-bottom: 15px;
        }
        .stTotalCreditos {
            font-size: 24px;
            font-weight: bold;
            color: #1E90FF;
            padding: 10px;
            border: 2px solid #1E90FF;
            border-radius: 5px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 3. Main Application Logic
# ==============================================================================

def main_app():
    """Main function to run the Streamlit calculator interface."""
    
    st.title("Calculadora de Distribución de Créditos 🛠️")
    st.header("Verificación de Costo Neto por Crédito")

    # --- User Inputs ---
    col1, col2 = st.columns(2)
    
    with col1:
        # Etiqueta clara para el costo de los créditos (clave para la distribución)
        valor_creditos_neto = st.number_input("Valor NETO de los Créditos ($)", min_value=0, step=1000, format="%d", 
                                     help="Ingrese el costo total que cubren solo los créditos académicos.")
    
    with col2:
        total_creditos = st.number_input("Número total de créditos", min_value=1, step=1, format="%d")

    # --- Year Selection ---
    options_anos = list(VALORES_CREDITO.keys())
    ano = st.selectbox("Selecciona el año de la matrícula", options=options_anos)

    # --- Study Type Selection (Filtered by Year) ---
    valores_ano = VALORES_CREDITO.get(ano, {})
    
    # Filtra los tipos de estudio
    tipos_disponibles = sorted([
        t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
        if t in valores_ano and (isinstance(valores_ano[t], list) and len(valores_ano[t]) > 0 and valores_ano[t][0] > 0)
    ])

    if not tipos_disponibles:
        st.warning("No hay tipos de estudio disponibles para este año. Verifique la data.")
        return

    tipo_estudio = st.selectbox("Selecciona el tipo de estudio", options=tipos_disponibles)

    # Get specific values for the selection
    
    # **Ajuste:** Obtener el valor de inscripción del nuevo diccionario
    tipo_estudio_key = tipo_estudio
    if tipo_estudio == "homologacion":
        # Asumimos que la homologación usa el valor de pregrado para la inscripción, si no hay valor
        # específico en la tabla. En la nueva tabla, solo existen 4 categorías.
        tipo_estudio_key = "pregrado" 

    valores_inscripcion_por_ano = VALORES_INSCRIPCION_POR_TIPO.get(ano, {})
    valor_inscripcion = valores_inscripcion_por_ano.get(tipo_estudio_key, 0)
        
    valor_seguro = VALOR_SEGURO_FIJO
    valores_credito = valores_ano.get(tipo_estudio, [0])
    
    st.markdown("---")
    
    # --- Reference Values Display ---
    st.subheader("Valores Fijos y de Referencia por Año")
    st.info(f"**Año:** {ano} | **Tipo de Estudio:** {tipo_estudio.capitalize()}")
    
    if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
        st.write(f"🏷️ **Crédito Tipo 1:** ${valores_credito[0]:,} | **Crédito Tipo 2:** ${valores_credito[1]:,}")
    elif len(valores_credito) >= 1 and valores_credito[0] > 0:
        st.write(f"🏷️ **Valor de Crédito único:** ${valores_credito[0]:,}")
    else:
        st.warning("El valor del crédito es 0 o no está definido. No se puede calcular.")
        return

    # Muestra el valor de inscripción con los nuevos datos (SIN SUMARLOS AL TOTAL)
    if valor_inscripcion > 0:
        st.write(f"📝 **Costo de Inscripción ({tipo_estudio.capitalize()}):** ${valor_inscripcion:,}")
    else:
        st.write(f"📝 **Costo de Inscripción ({tipo_estudio.capitalize()}):** No definido en la tabla para este año/tipo.")

    st.write(f"🛡️ **Costo del Seguro (Fijo):** ${valor_seguro:,}")
    
    st.markdown("---")

    # --- Calculation Logic (NO CHANGES HERE, already correct for distribution) ---
    if st.button("Calcular Distribución de Créditos"):
        
        costo_total_creditos = valor_creditos_neto
        solucion_encontrada = False
        
        detalle_creditos = ""
        total_creditos_usado = total_creditos 

        # Case 1: Two Credit Types (Pregrado/Tecnologia)
        if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
            v1, v2 = sorted(valores_credito)
            
            for x in range(total_creditos + 1):
                y = total_creditos - x
                
                if v1 * x + v2 * y == costo_total_creditos:
                    detalle_creditos = f"""
                        - **{x}** créditos a **${v1:,}** cada uno (Total: ${v1 * x:,})
                        - **{y}** créditos a **${v2:,}** cada uno (Total: ${v2 * y:,})
                        """
                    solucion_encontrada = True
                    break
            
            if not solucion_encontrada:
                st.error(f"❌ No existe una combinación exacta de **{total_creditos}** créditos que sume el valor neto ingresado (${costo_total_creditos:,}).")

        # Case 2: Single Credit Type (Especializacion/Maestria/Homologacion)
        elif len(valores_credito) >= 1 and valores_credito[0] > 0:
            v1 = valores_credito[0]
            
            if costo_total_creditos % v1 == 0:
                creditos_calculados = costo_total_creditos // v1
                
                if creditos_calculados != total_creditos:
                    st.info(f"💡 **Nota:** El valor neto de ${costo_total_creditos:,} sugiere **{creditos_calculados}** créditos, no los {total_creditos} que ingresó. La distribución se basa en el valor neto.")
                    total_creditos_usado = creditos_calculados
                
                detalle_creditos = f"- **{total_creditos_usado}** créditos a **${v1:,}** cada uno (Total: ${costo_total_creditos:,})"
                solucion_encontrada = True
            
            else:
                creditos_calculados = costo_total_creditos / v1
                
                st.error(f"""
                    ❌ El valor neto (${costo_total_creditos:,}) no corresponde a un número entero válido de créditos a ${v1:,} cada uno.
                    - El cálculo arroja **{creditos_calculados:,.2f}** créditos.
                    """)
        
        # --- Final Results Display ---
        if solucion_encontrada:
            st.subheader("✅ Distribución de Créditos Verificada ✅")
            
            st.markdown("#### Detalle de la Distribución:")
            st.markdown(f"**Total de Créditos (Verificado por Costo):** **{total_creditos_usado}**")
            st.markdown(detalle_creditos)
            
            st.markdown("---")

            # Muestra solo la suma de los créditos (sin costos fijos)
            st.markdown(f'<div class="stTotalCreditos">COSTO NETO TOTAL DE CRÉDITOS: ${costo_total_creditos:,}</div>', unsafe_allow_html=True)


# ==============================================================================
# 4. Execution
# ==============================================================================

if __name__ == "__main__":
    apply_custom_css()
    main_app()
