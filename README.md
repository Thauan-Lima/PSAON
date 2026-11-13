# 1. Título do projeto
**PSAON - Plataforma de Avaliações Online**

# 2. Descrição
### Objetivo geral. 
**Desenvolver um software para avaliações online capaz de criar um ambiente seguro e controlado, restringindo a navegação do usuário e registrando comportamentos que possam comprometer a integridade da avaliação.** 

# 3. Objetivos: principais objetivos do projeto.
### Objetivos específicos. 
**Implementar mecanismos que restrinjam a abertura de novas abas e janelas durante a avaliação.**
**Detectar tentativas de alternância entre a página da prova e outros aplicativos ou páginas.**
**Bloquear ou dificultar a realização de capturas de tela, quando suportado pela plataforma utilizada.**
**Registrar eventos de comportamento suspeito para posterior análise pelos professores.**
**Gerar relatórios contendo informações sobre as ocorrências registradas durante a avaliação.**
**Garantir que o aluno permaneça focado no ambiente da prova durante todo o período de realização.** 

# 4. Funcionalidades: descrição das principais funcionalidades implementadas ou previstas (informar caso a funcionalidade não estiver disponível ainda).

# 5. Tecnologias utilizadas [IMPORTANTE PARA A ATIVIDADE 02]
* **Python**
* **Django**
* **HTML e CSS**
* **JavaScript**
* **Bootstrap**
* **SQLite**
* **python-dotenv**

# 6. Pré-requisitos [IMPORTANTE PARA A ATIVIDADE 02]
* **Python (versão 3.10 ou superior):** Linguagem base do projeto.
* Verifique a versão que você está usando com o comando *python --version* 
* **pip:** Gerenciador de pacotes do Python (geralmente já vem instalado com o Python).
* **virtualenv (ou venv):** Para criar um ambiente virtual isolado e evitar conflitos de dependências.
* **Git:** Para clonar o repositório.

# 7. Instalação e execução [IMPORTANTE PARA A ATIVIDADE 02]
## 1. Clone o repositório
    git clone https://github.com/usuario/projeto_tasks.git
    cd projeto_tasks
    
## 2. Crie o ambiente virtual
O ambiente virtual isola as dependências do projeto do resto do sistema:

    python -m venv ./venv
    
Ative o ambiente.

No Windows:

    venv\Scripts\activate
    
No Linux ou Mac:

    source venv/bin/activate
    
## 3. Instale as dependências
    pip install -r requirements.txt
Isso instala o Django e o python-dotenv de uma só vez ( Com a venv ativado, claro).

## 4. Crie o arquivo .env
Copie o arquivo modelo e renomeie para .env:

    cp .env.example .env
    
No Windows, se o comando cp não funcionar:

    copy .env.example .env
    
Abra o .env. Ele contém:

    SECRET_KEY=
    DEBUG=True 

SECRET_KEY está vazia de propósito. Ela precisa ser gerada por cada pessoa, porque nunca é enviada para o GitHub.

## 5. Gere a sua SECRET_KEY
Com o ambiente ativado, execute: 
    
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   
O terminal imprime uma chave aleatória, parecida com esta:

    django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
## 6. Cole a chave no .env
Copie a chave impressa e cole no arquivo, sem aspas e sem espaços:

    SECRET_KEY=django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
    DEBUG=True

Cada pessoa pode usar a sua própria chave. O projeto funciona normalmente com chaves diferentes, pois ela serve apenas para assinar sessões e cookies.

# 8. Estrutura do projeto (opcional)
    PSAON/
    ├── venv/                 # Ambiente virtual (não vai para o GitHub)
    ├── manage.py
    ├── .env                  # Variáveis de ambiente (não vai para o GitHub)
    ├── .env.example          # Modelo do .env (vai para o GitHub)
    ├── .gitignore
    ├── requirements.txt
    ├── setup/                # Configurações do projeto
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── tarefas/              # App de tarefas
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── migrations/
    ├── usuarios/             # App de usuários
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── migrations/
    ├── templates/            # Arquivos HTML
    │   ├── base.html
    │   ├── tarefas/
    │   └── usuarios/
    ├── static/               # CSS, JS e imagens
    │   ├── css/
    │   ├── js/
    │   └── img/         

# 9. Equipe
**Thauan de Oliveira Lima** 

**Maria Caroline Macedo Ribeiro** 

**Jamylle Ariele Macedo Costa** 
