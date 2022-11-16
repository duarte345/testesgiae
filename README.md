# Testes no Giae
## IMPORTANTE!! Antes de executar o programa `giae.c run` rode `giae.c config` para criar as configurações
># [Indice](#indice)
><ul>
>    <li><a href="#indice">Indice</a></li>
>    <li><a href="#uso">Uso</a></li>
>    <li><a href="#importação">Importação</a></li>
>    <li><a href="#como-usar">Como usar</a></li>
>    <li><a href="#utilizador">Utilizador</a></li>
>    <li><a href="#desenvolvedor">Desenvolvedor</a></li>
>    <li><a href="#ficheiros">Ficheiros</a></li>
></ul>

## [Uso](#uso)
👨‍💻 Esta ferramenta foi criada no âmbito de sincronizar o calendário da google com os testes do giae, de maneira a que os alunos interessados possam ter acesso aos testes sem ter de ir ao giae.
Espero que gostes da ferramenta e fica á vontade para fazer as tuas alterações 😄

## [Importação](#importação)
A importação desta ferramenta é simples, basta clonares este repositório e usares no teu projeto como quiseres. Esta ferramenta foi criada só para testes, se tiveres algo que descobrieste em relação a segurança contacta os responsaveis sobre o problema.

## [Utilizador](#utilizador)
Caso sejas um aluno e desejas executar o programa no teu *computador* então faz o download do repositório e se disponível executa o ficheiro binário executável.
1. Clonar o repositório
2. executar o programa giae.c
## [Desenvolvedor](#desenvolvedor)
1. clonar o repositório.
```bash
git clone https://github.com/bener07/testesgiae.git
```
2. Criar um ficheiro á parte.
```bash
touch new_file.py
```
3. Importar a class *Testes* 
```python
from calendario import Testes
```
4. Iniciar um objeto com nome do utilizador e password como no exemplo
```python
objeto = Testes('a1234', 'qwerty')
```
5. E apartir daqui podes utilizar todas as caracteristicas.
### Nota
O nome do utilizador e password não são apresentados. Sendo aconselhado utilizá-las como variáveis de ambiente, mas não hardcoded. Estas credenciais não são usadas para mais nada sem ser o login para obter os cookies para aceder ao painel dos testes.

## [Ficheiros](#ficheiros)
- calendario.py
    - Contém o código utilizado para a API do google calendar.
- giae.py
    - Contém o código utilizado para conectar ao giae e contém as classes Testes e Login.
- discord.py
    - Contém o Bot de discord.
- testes_giae.c
    - Este programa em C não compilado é usado para faciliar a eperiência de utilizador com configurações e adiante 
