import requests
# Class de login que ao ser chamada devolve um valor de cookies depois utilizado ao receber testes
class Login:
        def __init__(self, utilizador, password):
                self.utilizador = utilizador
                self.password = password
        def __call__(self):
                host = "https://csmiguel.giae.pt/cgi-bin/webgiae2.exe/loginv2"
                data = {
                        "modo": "manual",
                        "escola": "380214",
                        "nrcartao": self.utilizador,
                        "codigo": self.password,
                        "urlrecuperacao": "https://csmiguel.giae.pt/"
                }
                login = requests.post(host, json=data)
                return login.cookies['sessao']

# Class da Lista de Testes
class Testes(Login):
        def __init__(self, utilizador, password):
                self.lista = []
                self.cookie = ''
                self.utilizador = utilizador
                self.password = password
        def __len__(self):
                return len(self.lista)
        def __call__(self):
                self.cookie = Login(self.utilizador, self.password).__call__()
                return self.cookie
        def update(self):
                if not self.cookie:
                        self.__call__()
                host = 'https://csmiguel.giae.pt/cgi-bin/webgiae2.exe/turma'
                cookies = {
                        "sessao": self.cookie,
                        "GIAEONLINECOOKIE_V2_ESCOLAS": "380214",
                        "GIAEONLINECOOKIE_V2_LASTAPP": "GIAE"
                }
                data = {
                        "acao": "testes"
                }
                headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
                        "Content-Length": "20"
                }
                r = requests.post(host, headers=headers, json=data, cookies=cookies)
                if 'Acesso negado' not in r.text:
                        self.lista = [teste for teste in r.json().get('testes')]
                        return self.lista
                else:
                        self.cookie = Login(self.utilizador, self.password).__call__()
                        raise accessError("Login failed!")
        def testes(self):
                if not self.lista:
                        self.update()
                return self.lista
        def teste(self, nome_do_teste):
                if not self.lista:
                        self.update()
                testes_de_x = [{
                        "Nome": test.get('descricao'),
                        "Data": test.get('data'),
                        "Inicio": test.get('horainicio'),
                        "Fim": test.get('horafim')
                        } for test in self.lista if nome_do_teste in test.get('descricao')]
                return testes_de_x

# Error handling
class accessError(Exception):
        """Caso tenha sido iniciado sessão noutro dispositivo com as mesmas credenciais este erro irá ser chamado"""
        pass