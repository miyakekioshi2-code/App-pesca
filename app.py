import streamlit as st

def interpretar_valor(entrada):
    """Trabalha com frações, onças (z) e gramas."""
    if not entrada:
        return 0.0
    entrada = entrada.lower().strip().replace(',', '.').replace('g', '')
    multiplicador = 1.0
    if 'z' in entrada:
        multiplicador = 28.35
        entrada = entrada.replace('z', '')
    try:
        if '/' in entrada:
            num, den = map(float, entrada.split('/'))
            return (num / den) * multiplicador
        return float(entrada) * multiplicador
    except:
        return 0.0

st.set_page_config(page_title="Miyake Pro Fishing", page_icon="🎣")

st.title("🎣 MIYAKE PRO FISHING")
st.subheader("Analisador de Equilíbrio de Material")

st.markdown("---")

v_acao = st.text_input("Ação da Vara (Ex: Rápida, Média)")

col1, col2 = st.columns(2)
with col1:
    v_cast_min = st.text_input("Casting MÍNIMO (ex: 1/4z ou 7g)")
with col2:
    v_cast_max = st.text_input("Casting MÁXIMO (ex: 1z ou 28g)")

v_lib_max = st.number_input("Libragem MÁXIMA da Vara (lb)", min_value=0.0, step=1.0)
peso_isca = st.text_input("Peso da ISCA Atual (ex: 3/8z ou 10g)")
res_linha = st.number_input("Libragem da LINHA Usada (lb)", min_value=0.0, step=1.0)

st.markdown("---")

if st.button("🔍 ANALISAR CONJUNTO", use_container_width=True):
    c_min = interpretar_valor(v_cast_min)
    c_max = interpretar_valor(v_cast_max)
    p_isca = interpretar_valor(peso_isca)
    
    # Lógica de Casting
    st.markdown("### 🎯 Equilíbrio de Arremesso")
    if p_isca == 0:
        st.error("❌ ERRO: Informe um peso de isca válido.")
    elif c_min <= p_isca <= c_max:
        st.success(f"✅ CONJUNTO EM HARMONIA\nIsca ({p_isca:.1f}g) está dentro do limite recomendado ({c_min:.1f}g a {c_max:.1f}g).")
    elif p_isca < c_min:
        st.warning(f"⚠️ ALERTA: ISCA LEVE ({p_isca:.1f}g)\nPerda de precisão e alcance de arremesso.")
    else:
        st.error(f"❌ PERIGO: SOBRECARGA NO BLANK!\nIsca ({p_isca:.1f}g) está acima do limite máximo ({c_max:.1f}g).")
        
    # Lógica de Linha
    st.markdown("### 🛡️ Segurança do Equipamento")
    if res_linha == 0 or v_lib_max == 0:
        st.info("Informe a libragem da vara e da linha para testar a segurança.")
    elif res_linha <= v_lib_max:
        st.success(f"✅ SETUP SEGURO\nLinha ({res_linha:.0f}lb) é adequada para o limite da vara ({v_lib_max:.0f}lb).")
    else:
        st.error(f"❌ RISCO CRÍTICO DE QUEBRA!\nA linha ({res_linha:.0f}lb) é mais resistente que a vara ({v_lib_max:.0f}lb).\nEm caso de enrosco, a vara pode quebrar antes da linha romper!")
