# Criação do projeto6 passo a passo:
Autenticação via session fará autenticação direta, via Browser
Autenticação via token fará autenticação remota
Podem haver várias autenticações para a mesma API REST

## Configurar autenticação via token:
- Em 'escola6/escola/settings.py':
-- Adicionar item em INSTALLED_APPS
-- Modificar DEFAULT_AUTHENTICATION_CLASSES
- Executar migrations: python3 manage.py migrate
- Testar acesso:

## Criar token:
- Abrir shell: python3 manage.py shell
-- from rest_framework.authtoken.models import Token
-- from django.contrib.auth.models import User
-- nomeUserDjango = User.objects.get(id=1)
-- token = Token.objects.create(user=nomeUserDjango)
-- Ver token (copiá-lo a guardá-lo): token.key
(Meu caso gerou '91adb4ad757616050cf0a5c81c60d66431e8103b')
(Ou pode-se criar o token via painel GUI admin do DRF)

## Testar token:
- Executar servidor Django: python3 manage.py runserver

1. No Postman, criar Request:
- Method: GET
- URL: http://localhost:8000/api/v2/cursos/
- Clicar em Send (retornará JSON com listagem de cursos)

2. No Postman, criar Request:
- Method: POST
- URL: http://localhost:8000/api/v2/cursos/
- Body: raw (JSON) e informar:
{
    "titulo": "drf ubsocial",
    "url": "https://ubdrfteste1.com"
}
- Clicar em Send (bloqueará, pois não há autenticação há métodos POST,PUT,DELETE)

3. No Postman, criar Request:
- Method: POST
- URL: http://localhost:8000/api/v2/cursos/
- Header:
key: Authorization
value: Token numToken
- Body: raw (JSON) e informar:
{
    "titulo": "drf ubsocial",
    "url": "https://ubdrfteste1.com"
}
- Clicar em Send (Criará novo curso)
