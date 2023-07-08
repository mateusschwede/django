# Criação do projeto5 passo a passo:

## Relacionamento entre models:
Relacionamento entre models.
Nesse caso 1-N (1 curso possui N avaliações).
Objetivo: Mostrar curso específico e também suas respectivas avaliações.

### 1.Nested Relationship:
Registros relacionados são incluídos dentro de recurso particular.
Forma pouco performática, ideal para casos com poucos registros e relações, como 1-1

- Em 'escola5/cursos/serializers.py', modificar CursoSerializer
- Testar no Browser (Listar cursos e respectivas avaliações): localhost:8000/api/v2/cursos
- Testar no Browser (Ver curso e respectivas avaliações): localhost:8000/api/v2/cursos/2

### 2.HyperLinked Related Field:
Registros, em links, dos elementos relacionados.
Forma performática, recomendada para APIs REST.

- Em 'escola5/cursos/serializers.py', modificar CursoSerializer novamente
- Testar no Browser (Listar cursos e respectivas avaliações): localhost:8000/api/v2/cursos
- Testar no Browser (Ver curso e respectivas avaliações): localhost:8000/api/v2/cursos/2

### 3.Primary Key Related Field:
Registros, em PK, dos elementos relacionados.
Forma mais performática, ideal para casos de extremo número de registros.

- Em 'escola5/cursos/serializers.py', modificar CursoSerializer novamente
- Testar no Browser (Listar cursos e respectivas avaliações): localhost:8000/api/v2/cursos
- Testar no Browser (Ver curso e respectivas avaliações): localhost:8000/api/v2/cursos/2


## Paginação:
Limitar quantidade de registros por página.

### Paginar listagem de cursos (global):
- Em 'escola5/escola/settings.py', inserir 2 novos elementos em 'REST_FRAMEWORK'
- Testar no Browser (dados não orenados): localhost:8000/api/v2/cursos
- Em 'escola5/cursos/models.py', adicionar 'ordering' na classe 'Meta' de Curso e Avaliacao
- Testar no Browser (dados orenados): localhost:8000/api/v2/cursos

### Paginar listagem de avaliações de curso (local):
- Em 'escola5/cursos/views.py', em CursoViewSet e class avaliacoes:
-- Informar pagination_class
-- Informar condição de paginação
-- Remover 'curso = self.get_object()' e modificar 2 últimas linhas
- Testar no Browser: localhost:8000/api/v2/cursos/2/avaliacoes


======> VER 26