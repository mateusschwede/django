# Criação do projeto9 passo a passo:

## Validações customizadas:
Objetivo: Limitar nota de avaliação para máximo 5.

- Em 'escola9/cursos/serializers.py', em AvaliacaoSerializer, criar função 'validate_avaliacao'
- Criar request para inserir avaliação:
-- Method: POST
-- URL: http://localhost:8000/api/v2/avaliacoes/
-- Head:
--- Key: Authorization
--- Value: Token numToken
-- Body raw (JSON):
{
    "curso": 3,
    "nome": "fulana",
    "email": "fulanaa@email.com",
    "avaliacao": 9
}
(send, bloqueará - avaliação maior que 5)

## Validação de dados serializers:
Objetivo: Mostrar média das avaliações para cada curso

- Em 'escola9/cursos/serializers.py', em CursoSerializer:
-- Adicionar import 'Avg'
-- Criar 'media_avaliacoes'
-- Inserí-lo no array 'fields'
-- Criar def 'get_media_avaliacoes'

- Criar request para listar cursos:
-- Method: GET
-- URL: http://localhost:8000/api/v2/cursos/
-- Head:
--- Key: Authorization
--- Value: Token numToken
(send, mostrará cursos e média das respectivas avaliações)

Obs: Essa função não é performática, pois realiza cálculo a toda requisição. Ideal é criar campo em Model (signals) e, toda vez que nova avaliação é criada, o campo é atualizado.