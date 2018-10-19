# 2018.2-metodos-projeto
Parte 1 do projeto da cadeira de métodos numéricos (IF816EC).

## Como rodar o programa
Em uma máquina Linux execute os seguintes comandos no terminal, estando na pasta raiz.

É necessário um arquivo *entradas.txt* com os formatos de entrada dados a seguir, para se executar o programa:


| Método        | Lista de Y's com a quantidade = Ordem           | Y Inicial | T inicial | h | Quantidade de Passos | Função | Ordem |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:| -----:|
| euler | O | X | X | X | X | X | O |
| euler_inverso | O | X | X | X | X | X | O |
| euler_aprimorado | O | X | X | X | X | X | O |
| runge_kutta | O | X | X | X | X | X | O |
| adam_bashforth | X | O | X | X | X | X | X |
| adam_bashforth_by_euler | O | X | X | X | X | X | O |
| adam_bashforth_by_euler_inverso | O | X | X | X | X | X | O |
| adam_bashforth_by_euler_aprimorado | O | X | X | X | X | X | O |
| adam_bashforth_by_runge_kutta | O | X | X | X | X | X | O |
| adam_multon | X | O | X | X | X | X | X |

X - Necessário

O - Desnecessário

Colocar os valores na ordem que apareceram na tabela.
### Exemplo: 

```
euler 0 0 20 1-t+4*y
euler_inverso 0 0 0.1 20 1-t+4*y
adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 5
adam_bashforth_by_euler 0 0 0.1 20 1-t+4*y 6

```

Um arquivo *saida.txt* com os pontos resultantes de cada método será gerado na pasta raiz do projeto.

### Pre-requisitos

Um computador com Linux e Python3 instalado e com seus respectivos caminhos adicionados ao terminal do usuário. O python pode ser proveniente da plataforma para Data Sciente de python, Anaconda.

É necessário instalar alguns pacotes. Para isso, faça:

`sudo ./requirements`

Depois entre no ambiente local com os pacotes instalados utilizando o virtualEnv.

`sudo source RUNME`

### Executar

Com as bibliotecas instaladas agora é só rodar o código principal.

`python main.py`

### Feito com

Python 3.6

## Autor

Thiago Augusto dos Santos Martins - tasm2

## License

MIT