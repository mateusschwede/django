# Criação/consumo API REST com Django REST Framework

Realizando a criação/consumo de API REST com Django REST Framework e autenticação Serializers. O código fora escrito nos padrões especificados pela documentação oficial do Django REST Framework.

## Preparo:
1. Instalar Django REST Framework (Necessário Django e pip instalados): pip install djangorestframework
2. Criar projeto Django: django-admin startproject projetoApiRest
	2.1. Dentro do projeto criado, criar app Django: python3 manage.py startapp api
3. Em 'settings.py', em INSTALLED_APPS, informar 'api.apps.AppConfig' e 'rest_framework' como últimos elementos do array

## Base do projeto
4. Em 'api/models.py', criar model Task (class Task)
5. Em 'projetoApiRest/urls.py', informar routes (path, informar também include no from)
6. Em 'api/urls.py', informar routes de CRUD
7. Em 'api/views.py', informar view apiOverview (def apiOverview, informar from adicional também)

## Execução
8. Criar migrations: python3 manage.py makemigrations
9. Executar migrations: python3 manage.py migrate
10. Executar projeto: python3 manage.py runserver

## Testes (No browser)
11. Acessar projeto: http://127.0.0.1:8000/api/
12. Listar tasks: http://127.0.0.1:8000/api/task-list/
13. Ver task 2: http://127.0.0.1:8000/api/task-detail/2/
14. Criar task: http://127.0.0.1:8000/api/task-create/
	14.2. Dados para inserir: {"title":"UB Social","completed":"true"}
15. Editar task 2: http://127.0.0.1:8000/api/task-update/2/
	15.2. Dados para inserir: {"id":2,"title":"Task 2 updated","completed":"false"}
16. Excluir task 2: http://127.0.0.1:8000/api/task-delete/2/