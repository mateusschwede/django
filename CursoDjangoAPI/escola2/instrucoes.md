# Criação do projeto2 passo a passo:
O Model Serializers converte objetos Python para JSON e vice-versa.

Criar arquivo de Serialização (escola2/cursos/serializers.py)

Criar APIViews para o método HTTP GET (escola2/cursos/views.py)
- APIView receberá a request e devolverá a response

Criar arquivo de rotas (escola2/cursos/urls.py)
Informar arquivo de rotas nas rotas globais (escola2/escola/urls.py)

Testar funcionamento (Browser):
localhost:8000/api/v1/cursos
localhost:8000/api/v1/avaliacoes

Criar APIViews para o método HTTP POST (escola2/cursos/views.py)

Testar funcionamento, inserir curso (Browser): localhost:8000/api/v1/cursos
(application/json)
{
    "titulo": "curso teste",
    "url": "http://curso.com"
}
