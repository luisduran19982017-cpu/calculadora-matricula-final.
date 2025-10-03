import streamlit as st

# ==============================================================================
# 1. Configuration Data (Mantenida)
# ==============================================================================

# --- Credit values per year and study type ---
VALORES_CREDITO = {
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


# --- Registration (Inscripción) value per year and type ---
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
# 3. Core Deduction Functions
# ==============================================================================

def buscar_distribucion(costo_neto, valores_credito, tipo_estudio):
    """
    Intenta deducir la distribución de créditos (x créditos a v1, y créditos a v2)
    que coincide exactamente con el costo neto.
    Retorna (es_solucion, detalles, total_creditos) o (False, None, 0).
    """
    
    # Caso 1: Dos Tipos de Crédito (Pregrado/Tecnologia)
    if tipo_estudio in ["pregrado", "tecnologia"] and len(valores_credito) == 2:
        v1, v2 = sorted(valores_credito)
        
        # Optimización: solo buscar en un rango razonable
        max_creditos_v2 = int(costo_neto / v2) + 1
        max_creditos_v2 = min(max_creditos_v2, 30) 
        
        for x in range(max_creditos_v2 + 1):
            costo_v2 = v2 * x
            resto = costo_neto - costo_v2
            
            if resto < 0:
                continue 

            if resto % v1 == 0:
                y = resto // v1 
                
                if y == int(y):
                    creditos_v1 = int(y)
                    creditos_v2 = x
                    total_creditos = creditos_v1 + creditos_v2
                    
                    detalles = {
                        "v1": v1, "c1": creditos_v1, 
                        "v2": v2, "c2": creditos_v2
                    }
                    return (True, detalles, total_creditos)

    # Caso 2: Un Solo Tipo de Crédito (Especializacion/Maestria/Homologacion)
    elif len(valores_credito) >= 1 and valores_credito[0] > 0:
        v1 = valores_credito[0]
        
        if costo_neto % v1 == 0:
            total_creditos = costo_neto // v1
            
            detalles = {"v1": v1, "c1": total_creditos}
            return (True, detalles, total_creditos)
            
    return (False, None, 0)


def buscar_ano_inverso(costo_neto, tipo_estudio):
    """
    Busca el primer año donde el costo_neto puede ser explicado por la tarifa
    del tipo_estudio seleccionado.
    """
    resultados = []
    
    # 1. Recorrer todos los años
    for ano in VALORES_CREDITO.keys():
        
        valores_ano = VALORES_CREDITO.get(ano, {})
        
        # 2. Verificar que el tipo de estudio exista para el año
        if tipo_estudio not in valores_ano:
            continue
            
        valores_credito = valores_ano[tipo_estudio]
        
        # 3. Intentar deducir la distribución para este año
        es_solucion, detalles_creditos, total_creditos = buscar_distribucion(
            costo_neto, 
            valores_credito, 
            tipo_estudio
        )
        
        if es_solucion:
            # Si encuentra una solución, obtén los costos fijos para el resultado
            tipo_estudio_key = tipo_estudio if tipo_estudio != "homologacion" else "pregrado"
            
            valores_inscripcion_por_ano = VALORES_INSCRIPCION_POR_TIPO.get(ano, {})
            valor_inscripcion = valores_inscripcion_por_ano.get(tipo_estudio_key, 0)
            
            valor_seguro = VALOR_SEGURO_FIJO
            
            resultados.append({
                "ano": ano,
                "costo_neto": costo_neto,
                "total_creditos": total_creditos,
                "inscripcion": valor_inscripcion,
                "seguro": valor_seguro,
                "detalles_creditos": detalles_creditos
            })
            
            # Devolvemos el primer resultado que encontramos (asumiendo unicidad)
            return resultados

    return resultados

# ==============================================================================
# 4. Main Application Interface
# ==============================================================================

def main_app():
    """Main function to run the Streamlit calculator interface."""
    
    st.title("Calculadora de Matrícula (Búsqueda Inversa) 🕵️")
    st.header("Luis Emir Guerrero Duran")

    # --- Available Study Types (Simplification) ---
    tipos_totales = ["pregrado", "tecnologia", "especializacion", "maestria", "homologacion"]
    
    # --- User Inputs ---
    col1, col2 = st.columns(2)
    
    with col1:
        valor_creditos_neto = st.number_input("Valor NETO de los Créditos ($)", min_value=0, step=1000, format="%d", 
                                     help="Ingrese el costo total que cubren solo los créditos académicos.")
    
    with col2:
        # Establece 'pregrado' como valor inicial
        default_index = tipos_totales.index("pregrado")
        tipo_estudio = st.selectbox(
            "Selecciona el tipo de estudio", 
            options=tipos_totales, 
            index=default_index
        )
    
    st.markdown("---")

    # --- Calculation Trigger ---
    if st.button("Buscar Año y Distribución"):
        
        if valor_creditos_neto <= 0:
            st.warning("⚠️ Por favor, ingrese un Valor Neto de Créditos válido (mayor que cero).")
            return
            
        with st.spinner(f"Buscando año y distribución para {tipo_estudio.capitalize()} y ${valor_creditos_neto:,}..."):
            
            # Ejecutar la búsqueda inversa
            resultados = buscar_ano_inverso(valor_creditos_neto, tipo_estudio)
            
            if resultados:
                st.subheader("✅ Resultado Encontrado: Distribución y Año Deducido ✅")
                
                # Mostrar solo el primer (y más probable) resultado
                res = resultados[0]
                
                # --- Secciones de Resultado ---
                st.markdown(f"## 📅 Año Deducido: **{res['ano']}**")
                
                st.info(f"**Tipo de Estudio:** {tipo_estudio.capitalize()}")
                
                st.markdown("#### Detalle de la Distribución de Créditos:")
                
                detalles = res['detalles_creditos']
                
                if 'v2' in detalles:
                    # Dos tipos de créditos
                    costo1 = detalles['v1'] * detalles['c1']
                    costo2 = detalles['v2'] * detalles['c2']
                    st.write(f"- **{detalles['c1']}** créditos a **${detalles['v1']:,}** cada uno (Total: **${costo1:,}**)")
                    st.write(f"- **{detalles['c2']}** créditos a **${detalles['v2']:,}** cada uno (Total: **${costo2:,}**)")
                    
                    st.markdown(f"**TOTAL DE CRÉDITOS MATRICULADOS:** **{res['total_creditos']}**")
                else:
                    # Un solo tipo de crédito
                    costo1 = detalles['v1'] * detalles['c1']
                    st.write(f"- **{detalles['c1']}** créditos a **${detalles['v1']:,}** cada uno (Total: **${costo1:,}**)")
                    
                    st.markdown(f"**TOTAL DE CRÉDITOS MATRICULADOS:** **{res['total_creditos']}**")

                st.markdown("---")
                st.markdown("#### Costos Fijos de Referencia (Año Deducido):")
                st.write(f"📝 **Costo de Inscripción ({res['ano']}):** ${res['inscripcion']:,}")
                st.write(f"🛡️ **Costo del Seguro (Fijo):** ${res['seguro']:,}")
                
                st.markdown(f'<div class="stTotalCreditos">VALOR NETO DE CRÉDITOS CONFIRMADO: ${res["costo_neto"]:,}</div>', unsafe_allow_html=True)
                
            else:
                st.error(f"❌ No se encontró un **Año** donde el valor neto de **${valor_creditos_neto:,}** sea una combinación exacta de créditos para el tipo de estudio **{tipo_estudio.capitalize()}**.")


# ==============================================================================
# 5. Execution
# ==============================================================================

if __name__ == "__main__":
    apply_custom_css()
    main_app()
