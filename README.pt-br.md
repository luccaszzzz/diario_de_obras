# EngList

Sistema de gerenciamento de obras construído com Django, com um board estilo Kanban para acompanhamento de status, upload de imagem por obra e uma API REST disponível junto à interface web tradicional.

O projeto usa um único app `core` que serve tanto as views web quanto os endpoints da API em namespaces de URL separados — `/` para os templates Django e `/api/v1/` para os endpoints DRF. As URLs de imagem na API são retornadas como URIs absolutas, deixando o endpoint pronto para consumo externo.

---

## Funcionalidades

| Funcionalidade   | Descrição                                                                               |
| ---------------- | --------------------------------------------------------------------------------------- |
| Board Kanban     | Obras organizadas em quatro colunas: Não Iniciada, Em Andamento, Concluída e Paralisada |
| CRUD de Obras    | Cadastrar, editar, revisar e excluir obras com título, descrição, data, imagem e status |
| Upload de Imagem | Imagem por obra armazenada no diretório `media/` via Pillow                             |
| Revisão de Obra  | Página de detalhe dedicada para cada obra com exibição completa da imagem               |
| API REST         | Endpoints DRF para listar, adicionar, atualizar e remover obras                         |
| Autenticação     | Login obrigatório — apenas superusuários têm acesso ao sistema                          |

---

## Endpoints da API

| Método | Endpoint                        | Descrição                |
| ------ | ------------------------------- | ------------------------ |
| GET    | `/api/v1/obras/listar/`         | Lista todas as obras     |
| PUT    | `/api/v1/obras/adicionar/`      | Adiciona uma nova obra   |
| POST   | `/api/v1/obras/atualizar/<id>/` | Atualiza uma obra por ID |
| DELETE | `/api/v1/obras/remover/<id>/`   | Remove uma obra por ID   |

---

## Screenshots

**Login**
![Login](docs/screenshots/login.png)

**Board Kanban**
![Board Kanban](docs/screenshots/lista.png)

**Cadastrar Obra**
![Cadastrar Obra](docs/screenshots/cadastro.png)

---

## Estrutura do Projeto

```
├── core/                      # App principal
│   ├── models.py              # Model Obra (título, descrição, data, imagem, status)
│   ├── forms.py               # ObraForm com seletor de data e status
│   ├── views.py               # Views web e endpoints da API
│   ├── serializers.py         # Serializer DRF com URL absoluta de imagem
│   └── urls_api.py            # Rotas da API (/api/v1/)
├── diario_de_obras/           # Configuração do projeto Django
│   ├── settings.py
│   └── urls.py
├── templates/                 # Templates HTML
│   ├── login.html
│   ├── obras_listar.html      # Board Kanban
│   ├── obras_cadastrar.html
│   ├── obras_editar.html
│   ├── obras_excluir.html
│   └── obras_revisar.html
├── static/
│   ├── css/                   # Folhas de estilo por página
│   └── img/                   # Ícones e logo
├── media/                     # Imagens de obras enviadas
├── docs/
│   └── screenshots/           # Screenshots do projeto
├── manage.py
└── requirements.txt
```

---

## Tecnologias

**Backend**

- Python
- Django 5.1
- Django REST Framework 3.17
- django-cors-headers 4.9
- Pillow 12.3

**Frontend**

- HTML5
- CSS3 (folhas de estilo por página, sem framework)
- JavaScript (vanilla)

**Banco de Dados**

- SQLite (desenvolvimento local)

---

## Como Executar

**1. Clonar o repositório**

```bash
git clone https://github.com/luccaszzzz/diario_de_obras.git
cd diario_de_obras
```

**2. Criar e ativar o ambiente virtual**

```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate
```

**3. Instalar as dependências**

```bash
pip install -r requirements.txt
```

**4. Aplicar as migrações**

```bash
python manage.py migrate
```

**5. Criar um superusuário**

```bash
python manage.py createsuperuser
```

**6. Iniciar o servidor**

```bash
python manage.py runserver
```

Acesse em `http://127.0.0.1:8000/`

> O login requer uma conta de superusuário. Use as credenciais criadas no passo 5.

---

## Autores

- Lucas Emanoel da Silva Freitas
- Júlia Galvão
- Allan Bezerra
- Thalles Hermínio

---

[Read in English](README.md)
