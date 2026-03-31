# EngList | Diário de Obras 🏗️

Sistema de gerenciamento de obras desenvolvido com Django, permitindo o cadastro, acompanhamento e revisão de projetos de construção de forma organizada e intuitiva.

## 📋 Sobre o Projeto
O EngList é uma aplicação web para gerenciamento de obras, desenvolvida para facilitar o controle de projetos de construção. O sistema permite organizar as obras em diferentes categorias de status, acompanhar seu progresso e manter um histórico detalhado de cada projeto.

---

## 🚀 Funcionalidades
* **Autenticação de usuários:** Sistema de login seguro para acesso ao sistema.
* **CRUD completo de obras:** Cadastrar, editar, visualizar e excluir obras.
* **Organização por status:** As obras são classificadas em quatro categorias (Não Iniciada, Em Andamento, Concluída, Paralisada).
* **Pesquisa de obras:** Busca rápida por títulos de obras.
* **Upload de imagens:** Cada obra pode ter uma imagem representativa.
* **Visualização detalhada:** Página específica para revisar informações completas de cada obra.

---

## 🛠️ Tecnologias Utilizadas
* **Backend:** Django (Python)
* **Frontend:** HTML5, CSS3, JavaScript
* **Estilização:** CSS personalizado com design responsivo
* **Fontes:** Google Fonts (Roboto)

---

## 📂 Estrutura de Pastas
```plaintext
├── core/                       # Aplicação principal
│   ├── migrations/             # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py               # Configuração do admin Django
│   ├── apps.py                # Configuração da aplicação
│   ├── forms.py               # Formulários do sistema
│   ├── models.py              # Modelos de dados
│   ├── serializers.py         # Serializadores (API)
│   ├── urls_api.py            # Rotas da API
│   └── views.py               # Views do sistema
├── diario_de_obras/           # Configurações do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Configurações do Django
│   ├── urls.py                # Rotas principais
│   └── wsgi.py
├── static/                    # Arquivos estáticos
│   ├── css/                   # Folhas de estilo
│   │   ├── cadastrar_obras.css
│   │   ├── editar_obras.css
│   │   ├── listar_obras.css
│   │   ├── login.css
│   │   └── revisar_obras.css
│   └── img/                   # Imagens e ícones
├── templates/                 # Templates HTML
│   ├── login.html
│   ├── obras_cadastrar.html
│   ├── obras_editar.html
│   ├── obras_excluir.html
│   ├── obras_listar.html
│   └── obras_revisar.html
├── .gitignore
└── manage.py                  # Script de gerenciamento Django
```

---

## ⚙️ Como rodar o projeto localmente

### Pré-requisitos
* **Python 3.8 ou superior**
* **pip (gerenciador de pacotes Python)**
* **Virtualenv (recomendado)**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/englist.git
   cd englist
   ```
   
2. Crie e ative um ambiente virtual:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install django
   ```
   
4. Execute as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crie um superusuário (para acessar o admin)
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento
   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação
   * Abra o navegador e acesse: _http://127.0.0.1:8000_
   * Para acessar o admin: _http://127.0.0.1:8000/admin_

---

## 🔐 Credenciais de Acesso

Após criar o superusuário, utilize as credenciais para fazer login no sistema através da página inicial.

## 📱 Responsividade

O sistema foi desenvolvido com foco em responsividade, adaptando-se a diferentes tamanhos de tela:

* Desktop: Layout com quatro colunas de status
* Tablet: Duas colunas de status
* Mobile: Uma coluna de status

## 🎨 Estilização

* **Paleta de cores:** Azul escuro (#0f0f4c) como cor principal e laranja (#ff6b00) para efeitos de hover.
* **Cards:** Design clean com sombras suaves e bordas arredondadas.
* **Barra de pesquisa:** Funcionalidade de busca com ícone interativo.
* **Efeitos visuais:** Transições suaves e efeitos de hover nos elementos interativos.
