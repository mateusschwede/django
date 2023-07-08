# Criação do projeto7 passo a passo:
Uso de permissões (authorization)

AllowAny: Permissão total
IsAuthenticated: Somente se autenticado
IsAdminUser: Permissão para acessar página Django Admin
DjangoModelPermissions: Somente se autenticado (para funções de model)
Autenticação local sobrescreve global

Objetivo: Alterar permissões locais para determinada view

## Criar novo user:
- Iniciar servidor: python3 manage.py runserver
- Entrar painel Django Admin: localhost:8000/admin
- Criar user:
-- Nome: ubsocial
-- Senha: 123ub456
- Após criado, no Django Admin, permissões do usuário, incluir 'Can add Curso' (salvar) (Permissões de adição permitem, por consequência, visualização)
- Em 'Tokens', gerar token para user:
-- Selecionar user 'ubsocial' (salvar), copiar e guardar token
(token mateus (91adb4ad757616050cf0a5c81c60d66431e8103b))
(token ubsocial (6a192de3bb41380ba44d477ecce73d377ebfba1a))

## Alterar views para autorizações:
- Em 'escola7/cursos/views.py', inserir import 'permissions'
-- Em 'CursoViewSet', inserir trecho de permisssion_classes (Linha 1)

### Testar permission (Postman):
- Criar request para listar Cursos (user anônimo):
-- Method: GET
-- URL: http://localhost:8000/api/v2/cursos/
(send, bloqueará acesso)

- Criar request para listar Avaliações (user anônimo):
-- Method: GET
-- URL: http://localhost:8000/api/v2/avaliacoes/4
(send, mostrará dados)

- Criar request para listar Cursos (user ubsocial):
-- Method: GET
-- URL: http://localhost:8000/api/v2/cursos/
-- Header:
--- Key: Authorization
--- Value: Token numTokenUbsocial
(send, mostrará dados)

- Criar request para atualizar Cursos (user ubsocial):
-- Method: PUT
-- URL: http://localhost:8000/api/v2/cursos/1/
-- Header:
--- Key: Authorization
--- Value: Token numTokenUbsocial
(send, bloqueará acesso - não possui permissão)

## Criar classe personalizada de permissão:
Objetivo: Criar permissão para somente super usuário deletar itens
- Em 'escola7/cursos/', criar arquivo 'permissions.py', com seu conteúdo
- Em 'escola7/cursos/views.py':
-- Adicionar import 'EhSuperUser'
-- Adicionar 'EhSuperUser' em permisssion_classes de 'CursoViewSet'

### Testar permission (Postman):
- Criar request para deletar Cursos (user ubsocial, não é superuser):
-- Method: DELETE
-- URL: http://localhost:8000/api/v2/cursos/2/
-- Header:
--- Key: Authorization
--- Value: Token numTokenUbsocial
(send, bloqueará acesso - não possui permissão)

- Em página Django Admin, marcar 'ubsocial' como superuser
- Criar request para deletar Cursos (user ubsocial):
-- Method: DELETE
-- URL: http://localhost:8000/api/v2/cursos/2/
-- Header:
--- Key: Authorization
--- Value: Token numTokenUbsocial
(send, deletará com sucesso)


=====> VER 28