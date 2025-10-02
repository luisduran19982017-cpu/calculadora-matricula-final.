#!/bin/bash

# --- PASO 1: Definir las rutas ---
# RUTA DEL ENTORNO VIRTUAL
VENV_ACTIVATE_PATH="/Users/macbookproi9/Documents/programar/.venv/bin/activate"

# RUTA DEL DIRECTORIO DEL PROYECTO (DONDE ESTÁ Calculadora_Matricula.py)
PROJECT_DIR="/Users/macbookproi9/Documents/programacion nueva" 

# --- PASO 2: Navegar al directorio del proyecto ---
cd "$PROJECT_DIR" || { echo "Error: No se puede cambiar al directorio del proyecto. Revisa la ruta PROJECT_DIR."; exit 1; }

# --- PASO 3: Activar el entorno virtual ---
echo "Activando entorno virtual..."
source "$VENV_ACTIVATE_PATH" || { echo "Error: No se puede activar el entorno virtual. Revisa la ruta VENV_ACTIVATE_PATH."; exit 1; }

# --- PASO 4: Ejecutar la aplicación Streamlit con el nombre de archivo correcto ---
echo "Iniciando Calculadora de Matrícula (Streamlit)..."
# *** CAMBIO A: streamlit run Calculadora_Matricula.py ***
streamlit run Calculadora_Matricula.py

# El entorno permanecerá activo en la ventana de terminal hasta que se cierre.