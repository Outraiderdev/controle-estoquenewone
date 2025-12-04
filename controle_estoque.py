import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime

# Arquivos JSON
ARQUIVO_ESTOQUE = "estoque.json"
ARQUIVO_HISTORICO = "historico.json"

# -------------------------------------------
# FUNÇÕES
# -------------------------------------------
def carregar_json(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f)
    return {}

def salvar_json(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

# Carrega estoque e histórico
estoque = carregar_json(ARQUIVO_ESTOQUE)
historico = carregar_json(ARQUIVO_HISTORICO)

def registrar_historico(acao, item, quantidade):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historico[now] = {"acao": acao, "item": item, "quantidade": quantidade}
    salvar_json(ARQUIVO_HISTORICO, historico)

# -------------------------------------------
# CSS MODERNO
# -------------------------------------------
st.markdown("""
    <style>
        .main-title { font-size: 32px; font-weight: bold; color: #4f8bf9; text-align: center; margin-bottom: 20px; }
        .card { background-color: #f0f2f6; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 10px rgba(0,0,0,0.10); margin-bottom: 20px; }
        .btn-add { background-color: #4CAF50 !important; color: white !important; }
        .btn-remove { background-color: #E53935 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------
# TÍTULO
# -------------------------------------------
st.markdown("<h1 class='main-title'>📦 Controle de Estoque</h1>", unsafe_allow_html=True)

# -------------------------------------------
# MENU LATERAL
# -------------------------------------------
menu = st.sidebar.radio(
    "Menu",
    ["Adicionar item", "Remover/Atualizar item", "Listar estoque", "Histórico"],
    index=0
)

# -------------------------------------------
