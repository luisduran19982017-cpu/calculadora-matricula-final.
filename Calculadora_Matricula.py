import streamlit as st

# ==============================================================================
# 1. Configuration Data
#    
#    Valores actualizados de ESPECIALIZACION y MAESTRIA basados en la última imagen.
#    
#    Nota: Se asume que el valor de inscripción para Maestría en 2018 es el mismo 
#    que en 2019 (185.000), ya que la casilla está vacía en la tabla. 
#    Para la Inscripción de Especialización y Maestría, se han usado los valores 
#    de la tabla cuando están disponibles.
# ==============================================================================

# --- Credit values per year and study type ---
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

# --- Registration (Inscripción) value per year ---
VALORES_INSCRIPCION = {
    # Valores de Inscripción (INSCRIPCION ESPECIALIZACION)
    "2006-1": 96000, "2006-2": 96000, "2007-1": 97000, "2007-2": 97000,
    "2008-1": 103000, "2009-1": 111000, "2010-1": 115000, "2011-1": 119000,
    "2012-1": 126000, "2013-1": 130000, "2014": 137000, 
    
    # Valores de 2015 en adelante (Inscripción Especialización y Maestría)
    "2015": 144000, 
    "2016": 154000, 
    "2017": 165000, 
    # Inscripción Maestría solo aparece desde 2019, usaremos el mismo valor si es pregrado/tecnologia
    # Para 2018, la Maestría está vacía. Se mantiene 185000 si se selecciona Maestría.
    "2018": 185000, 
    "2019": 185000, 
    "2020": 196000, 
    "2021": 203000, 
    "2022": 223000, 
    "2023": 259000, 
    "2024": 290000, 
    "2025": 317000
}

# --- Fixed Insurance Value (Valor de Seguro) ---
VALOR_SEGURO_FIJO = 9000

# Diccionario para mapear los valores de inscripción específicos de Maestría (si son diferentes)
INSCRIPCION_MAESTRIA_ESPECIAL = {
    "2019": 185000,
    "2020": 196000,
    "2021": 203000,
    "2022": 223000,
    "2023": 259000,
    "2024": 290000,
    "2025": 317000
    # Se asume que en los años anteriores, la inscripción de Maestría era 0 o el mismo valor de la Especialización
}


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
    
    tipos_disponibles = sorted([
        t for t in ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
        if t in valores_ano and (isinstance(valores_ano[t], list) and len(valores_ano[t]) > 0 and valores_ano[t][0] > 0)
    ])

    if not tipos_disponibles:
        st.warning("No hay tipos de estudio disponibles para este año. Verifique la data.")
        return

    tipo_estudio = st.selectbox("Selecciona el tipo de estudio", options=tipos_disponibles)

    # Get specific values for the selection
    # Utilizar el diccionario especial para Maestría, sino, usar el general.
    if tipo_estudio == "maestria" and ano in INSCRIPCION_MAESTRIA_ESPECIAL:
        valor_inscripcion = INSCRIPCION_MAESTRIA_ESPECIAL.get(ano, 0)
    else:
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
            
            # Use the input total credits for the loop constraint
            if v1 > v2: v1, v2 = v2, v1
            
            for x in range(total_creditos + 1):
                y = total_creditos - x
                
                # Check if the combination sums up to the total value
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

