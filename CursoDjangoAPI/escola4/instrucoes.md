# Criação do projeto4 passo a passo:
Sobrescrever generic views

## Listar avaliações de um curso específico e ver dados específicos da mesma:
(O 'queryset' mostra lista de objetos. O 'get_object' mostra único objeto)
- Informar novas rotas em 'escola4/cursos/urls.py'

Em 'escola4/curso/views.py':
- Adicionar import 404
- Modificar view 'AvaliacoesAPIView'
- Testar no Browser, listar avaliacoes de curso específico: localhost:8000/api/v1/cursos/1/avaliacoes

- Modificar view 'AvaliacaoAPIView'
- Testar no Browser, listar dados específicos de avaliação, de um curso específico: localhost:8000/api/v1/cursos/1/avaliacoes/1

## Utilizar ViewSets e Routers:
Routers automatiza criação de endpoints para model específica.
ViewSet permite agrupar toda lógica de um determinado recurso em única classe (Ex: Única class para endpoints de coleção e indivíduo). Utilizando ViewSets, os endpoints são criados automaticamente com os Routers.
Manter código antigo para API v1, e criar API v2 com os novos códigos.

- Em 'escola4/cursos/views.py' (Informar códigos na API v2):
Informar import viewsets, action, Response e mixins
Informar novas class na API v2

- Em 'escola4/cursos/urls.py':
Informar import SimpleRouter, CursoViewSet e AvaliacaoViewSet
Informar router

- Em 'escola4/escola/urls.py':
Informar import router
Criar rotas para API v2

Testar no Browser:
localhost:8000/api/v1/avaliacoes (cursos)
localhost:8000/api/v2/avaliacoes (cursos)
localhost:8000/api/v2/cursos/1
localhost:8000/api/v2/cursos/1/avaliacoes
localhost:8000/api/v2/cursos/1/avaliacoes/1

## Customizar ViewSets:
- Customizar ViewSet AvaliacaoVewSet para filtrar listagem de avaliações
Em 'escola4/cursos/views.py', comentar AvaliacaoViewSet antiga e criar nova
Testar no Browser:
localhost:8000/api/v2/avaliacoes (Método 'list' não permitido)
localhost:8000/api/v2/avaliacoes/4 (Método 'retrieve' permitido)

===> VER 22