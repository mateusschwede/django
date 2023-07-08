# Criação do projeto passo a passo:

Criação do projeto:
1. Criar e entrar no projeto: django-admin startproject escola && cd escola
2. Criar app: django-admin startapp cursos

Configurar projeto (escola/escola/settings.py):
1. Array 'INSTALED_APPS', adicionar itens no final do array

Criar Models (escola/cursos/models.py):
1. Criar model 'Base()'
2. Criar model 'Curso()'
3. Criar model 'Avaliacao()'

Registrar Models no Admin (escola/cursos/admin.py)

Criar Migrations: python3 manage.py makemigrations
Executar Migrations: python3 manage.py migrate
Criar SuperUser: python3 manage.py createsuperuser
Executar projeto: python3 manage.py runserver
Testar funcionamento (Browser): localhost:8000/admin
(Inserir alguns cursos e avaliações)

--- Criar API REST ---
sudo pip3 install djangorestframework markdown django-filters

Configurar settings.py: No final do arquivo, informar 'REST_FRAMEWORK'
Configurar routes do projeto (escola/escola/urls.py)
Testar funcionamento (Browser): localhost:8000/auth/login (logout)