import streamlit as st

# Configuração da página
st.set_page_config(page_title="Login", page_icon="🔒")

# Inicialização das variáveis de estado da sessão
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

def check_password():
    """Retorna `True` se as credenciais estão corretas."""
    return st.session_state["username"].strip() == "admin" and st.session_state["password"] == "admin@123"

def login_form():
    """Exibe o formulário de login."""
    st.title("🔒 Login")
    
    # Formulário de login
    with st.form("login"):
        st.text_input("Usuário", key="username")
        st.text_input("Senha", type="password", key="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            if check_password():
                st.session_state['login_status'] = True
                st.experimental_rerun()
            else:
                st.error("❌ Usuário ou senha incorretos")

def show_report(report_type):
    """Exibe o relatório selecionado."""
    if report_type == "Vendas Mensais":
        st.subheader("📊 Relatório de Vendas Mensais")
        st.write("Aqui será exibido o relatório de vendas mensais...")
        # Exemplo de gráfico
        chart_data = {
            'Mês': ['Jan', 'Fev', 'Mar', 'Abr'],
            'Vendas': [100, 120, 80, 150]
        }
        st.line_chart(chart_data)
    
    elif report_type == "Estoque":
        st.subheader("📦 Relatório de Estoque")
        st.write("Aqui será exibido o relatório de estoque...")
        # Exemplo de tabela
        data = {
            'Produto': ['Produto A', 'Produto B', 'Produto C'],
            'Quantidade': [50, 30, 20]
        }
        st.dataframe(data)
    
    elif report_type == "Financeiro":
        st.subheader("💰 Relatório Financeiro")
        st.write("Aqui será exibido o relatório financeiro...")
        # Exemplo de métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Receita", value="R$ 50.000", delta="+ 8%")
        with col2:
            st.metric(label="Despesas", value="R$ 30.000", delta="- 2%")
        with col3:
            st.metric(label="Lucro", value="R$ 20.000", delta="+ 15%")

def main():
    """Conteúdo principal do aplicativo após o login."""
    st.sidebar.title("Menu de Navegação")
    
    # Menu na barra lateral
    menu_options = ["Dashboard", "Relatórios", "Configurações"]
    selected_menu = st.sidebar.selectbox("Selecione uma opção", menu_options)
    
    if selected_menu == "Dashboard":
        st.title("Dashboard Principal 📊")
        st.write("Bem-vindo(a) ao painel de controle!")
        
    elif selected_menu == "Relatórios":
        st.title("Relatórios �")
        
        # Submenu de relatórios
        report_type = st.selectbox(
            "Selecione o tipo de relatório",
            ["Vendas Mensais", "Estoque", "Financeiro"]
        )
        
        # Exibe o relatório selecionado
        show_report(report_type)
        
    elif selected_menu == "Configurações":
        st.title("Configurações ⚙️")
        st.write("Página de configurações em desenvolvimento...")
    
    # Botão de logout no sidebar
    if st.sidebar.button("Logout"):
        st.session_state['login_status'] = False
        st.experimental_rerun()

# Fluxo principal do aplicativo
if not st.session_state['login_status']:
    login_form()
else:
    main()