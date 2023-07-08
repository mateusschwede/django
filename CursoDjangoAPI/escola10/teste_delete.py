import requests

headers = {'Authorization': 'Token 6a192de3bb41380ba44d477ecce73d377ebfba1a'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

#curso = requests.get(url=f'{url_base_cursos}3/', headers=headers)
#print(curso.json())

resultado = requests.delete(url=f'{url_base_cursos}3/', headers=headers)
assert resultado.status_code == 204
assert len(resultado.text) == 0