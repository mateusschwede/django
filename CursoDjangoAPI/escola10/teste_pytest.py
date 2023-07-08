import requests

class TestCursos:
    headers = {'Authorization': 'Token 6a192de3bb41380ba44d477ecce73d377ebfba1a'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}3/', headers=self.headers)
        assert resposta.status_code == 200
    
    def test_post_curso(self):
        novo = {
            "titulo": "Novo curso1",
            "url": "http://novocurso1.com"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']
    
    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso atualizado1",
            "url": "http://atualizado1.com"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Curso atualizado2",
            "url": "http://atualizado2.com"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)
        assert resposta.json()['titulo'] == atualizado["titulo"]

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}3/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0