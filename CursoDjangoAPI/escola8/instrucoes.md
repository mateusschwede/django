# Criação do projeto8 passo a passo:
Limitar requisições ao servidor com Throttling
Objetivo: Usuários autenticados podem realizar 3 requisições por minuto. Usuários anônimos somente 2 requisições por minuto. Throttling global.

- Em 'escola7/escola/settings.py', em REST_FRAMEWORK, inserir DEFAULT_THROTTLE_CLASSES e DEFAULT_THROTTLE_RATES
- Em 'escola7/cursos/views.py', adicionar 'mixins.ListModelMixin' em AvaliacaoViewSet

- Criar requisição (usuário anônimo):
-- Method: GET
-- URL: http://localhost:8000/api/v2/avaliacoes/
(send, aceitará 2 vezes, a 3ª bloqueará)

- Criar requisição (usuário autenticado):
-- Method: GET
-- URL: http://localhost:8000/api/v2/avaliacoes/
-- HEAD:
--- Key: Authorization
--- Value: Token numToken (Exemplo: Token 6a192de3bb41380ba44d477ecce73d377ebfba1a)
(send, aceitará 3 vezes, a 4ª bloqueará)


============> VER 29