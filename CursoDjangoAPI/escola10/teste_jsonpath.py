import requests, jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
print(resultados)

primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeiro)

nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)

nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
print(nota)

nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome') #Todos nomes
print(nomes)

notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)