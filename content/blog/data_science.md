---
title: "Ciência de Dados: Um Guia Completo"
date: 2025-02-06T09:48:00.000-03:00
tags:
  - ciências de dados
  - análise
  - estatística
  - aprendizado de máquina
  - python
categories:
  - dados
description: "A ciência de dados é o processo de analisar grandes conjuntos de dados para descobrir padrões. Combina estatísticas, programação e conhecimento do domínio. Aqui, iremos trazer um guia completo sobre este tema para ajudar novas pessoas na área."
banner: /img/banners/11042_2020_8700_fig1_html.png
authors:
  - Guilherme Oliveira
  - Carlos Henrique G. Ferreira
---



<!--more-->

# Agradecimentos

Gostaria de expressar minha profunda gratidão ao [Prof. Dr. Carlos Henrique G. Ferreira](https://www.researchgate.net/profile/Carlos-G-Ferreira). Parte do material apresentado neste curso foi desenvolvido com base em seus ensinamentos do curso **Projeto e Análise de Experimentos**, ministrado no **[ICEA](https://icea20anos.ufop.br/)**. Sua expertise e dedicação foram fundamentais para a construção deste conteúdo, que tem como objetivo auxiliar estudantes e profissionais no aprimoramento de suas habilidades.

- - -

# Introdução a Python

Python é uma das linguagens de programação mais populares para análise de dados e computação científica devido à sua simplicidade, versatilidade e uma comunidade extremamente ativa. Com um vasto ecossistema de bibliotecas de código aberto, como [re_mocd](https://pypi.org/project/re-mocd/), [Pandas](https://pandas.pydata.org/) e [Scikit-learn](https://scikit-learn.org/), tornou-se uma escolha dominante para cientistas de dados e pesquisadores.


## Limitações do Python

Embora seja extremamente versátil, Python pode ser menos eficiente para algumas aplicações devido ao **Global Interpreter Lock (GIL)**, que pode ser definido da seguinte maneira:

> "O **GIL** é um bloqueio único no próprio interpretador que adiciona uma regra de que a execução de qualquer bytecode Python requer a aquisição do bloqueio do interpretador. Isso evita deadlocks (pois há apenas um bloqueio) e não introduz muita sobrecarga de desempenho. Mas efetivamente torna qualquer programa Python vinculado à CPU single-threaded." - **[RealPython](https://realpython.com/python-gil/)**.

##   "Solução"

Extensões em C/C++ ou Rust utilizam código compilado para otimizar a execução. Just-In-Time (**JIT**) Ferramentas como `Numba` ou `PyPy` permitem compilar partes do código em tempo real, melhorando significativamente a performance. O módulo `multiprocessing` cria processos independentes, cada um com seu próprio interpretador Python e espaço de memória. (e.g.), veja o exemplo abaixo 

```python
# Se você não esta entendendo nada, não tem problema. 
# Aqui queremos demonstrar apenas a diferença de tempo  ;)
from multiprocessing import Pool
import time

USE_MULTIPROCESSING = True

COUNT = 50000000
def countdown(n):
   while n>0:
      n -= 1

if __name__ == '__main__':
   start_time = time.time()
   
   if USE_MULTIPROCESSING:
      with Pool(processes=4) as pool:
         # Split work into 4 equal chunks
         chunk_size = COUNT // 4
         pool.map(countdown, [chunk_size] * 4)
   else:
      countdown(COUNT)

   elapsed_time = time.time() - start_time
   print(f'Time taken: {elapsed_time:.2f} seconds')

```

A tabela abaixo apresenta a média (`μ`) dos tempos de execução ao longo de 10 gerações, acompanhada do respectivo desvio padrão (`dP`).  

| **Linguagem**                     | **μ**               | **dP** |
|------------------------------------|-----------------------------|------------------------|
| Rust                               | 0.10ms                      | ± 0.1                  |
| C (gcc -O0)                        | 0.19ms                      | ± 0.1                  |
| Python                             | **3.17**ms                  | ± 0.1                  |
| Rust (Threading + --release)       | 0.03ms                      | ± 0.1                  |
| C (Threading + gcc -O3)            | 0.04ms                      | ± 0.2                  |
| Python (Multiprocessing)           | **0.77**ms                  | ± 0.2                  |
| Python (Multiprocessing + PyPy)    | **0.09** ms                 | ± 0.2                  |

Os resultados demonstram que a performance pode variar significativamente, especialmente no Python. No entanto, observa-se que o uso de paralelismo e otimizações como `PyPy` podem reduzir consideravelmente esse impacto. Ainda assim, linguagens compiladas continuam a apresentar desempenho superior em termos de velocidade.  

---

## Ambientes de Execução

Para começar a programar em Python, faça o download da versão mais recente no site oficial ([python.org](https://www.python.org)) e instale-a em sua máquina. Se você está usando um sistema baseado em **GNU/Linux**, muito provavelmente `python` ou `python3` está instalado por padrão em sua máquina.

Você pode testar se o Python foi instalado corretamente e/ou ja se encontra na sua maquina usando o seguindo comando no terminal:

```bash
python --version | python3 --version
```

E você pode testar o ambiente via terminal usando:

```bash
python3
```

Outras opções incluem:

![](/img/banners/envs.png)


- **VSCodium**: É uma versão open-source do Visual Studio Code (VSCode), sem os rastreadores de telemetria da Microsoft. Ele mantém todas as funcionalidades do VSCode, incluindo suporte a extensões, depuração e desenvolvimento para várias linguagens de programação, sendo uma excelente opção para quem busca mais privacidade e software livre.  

- **PyCharm**: Um ambiente de desenvolvimento integrado (IDE) voltado para Python, desenvolvido pela JetBrains. Ele oferece ferramentas avançadas, como depuração inteligente, refatoração de código, suporte a frameworks como Django e integração com bancos de dados. Existem versões gratuitas (Community) e pagas (Professional), sendo muito utilizado por desenvolvedores Python profissionais.  

- **Spyder**: Um IDE voltado para ciência de dados e computação científica, amplamente utilizado por usuários do Python. Ele é integrado ao Anaconda e oferece funcionalidades como um console interativo, visualização de variáveis e depuração, tornando-se uma escolha popular entre pesquisadores e analistas de dados.  

- **Atom**: Atom era um editor de texto open-source desenvolvido pelo GitHub, conhecido por sua personalização e suporte a pacotes. No entanto, o desenvolvimento **foi descontinuado em 2022**, mas muitas pessoas ainda usam. 

- **Jupyter Notebook**: Um ambiente web interativo que permite escrever e executar código Python em células, tornando-se muito popular em análise de dados, aprendizado de máquina e pesquisa científica. Ele permite a combinação de código, visualizações de dados e documentação em um só documento, facilitando a reprodutibilidade e compartilhamento de projetos.  

# Conceitos Essenciais

O Python é uma linguagem que prioriza a legibilidade do código, com ênfase na simplicidade e clareza, fazendo com que se assemelhe a um "pseudocódigo" real. Em vez de usar chaves, a linguagem utiliza a indentação para organizar o código. Blocos de código são definidos por indentação e dois pontos, tornando a estrutura mais limpa e fácil de entender. Além disso, Python não exige ponto e vírgula no final das instruções, embora seja possível usá-lo para separar múltiplas declarações na mesma linha. Neste artigo, exploraremos alguns dos conceitos essenciais dessa linguagem.

## Comentários

Comentários são anotados utilizando o caractere `#`, sendo ignorados pelo interpretador do Python.

```python
results = []
for line in file:
   # if len(line) == 0:
   #  break
   results.append(line.replace("foo", "bar"))
print("Done.")
```

## Funções e Métodos

Em Python, funções são invocadas por meio de parênteses e podem aceitar tanto argumentos posicionais quanto argumentos por palavra-chave. Métodos, por sua vez, são funções associadas a objetos e são chamados utilizando a notação de ponto. Quase todos os objetos em Python possuem métodos, que são funções vinculadas aos dados internos do objeto e são acessadas de forma específica.

As funções podem aceitar argumentos de diferentes tipos, oferecendo flexibilidade na passagem de dados.

Exemplo de função:

```python
def exemplo_funcao(x, y=10):
    return x + y
```

## Variáveis  

Ao atribuir uma variável em Python, você está, na verdade, criando uma referência ao objeto à direita do sinal de igual. Por exemplo, ao trabalhar com uma lista de inteiros, você está fazendo referência à lista, não criando uma cópia dela.  

```python
a = [1, 2, 3]
b = a  # 'b' agora referencia a mesma lista que 'a'
b.append(4)  
print(a)  # Saída: [1, 2, 3, 4]  
```  

Isso significa que, ao passar objetos como argumentos para uma função, novas variáveis locais são criadas, apontando para os objetos originais, sem realizar cópias.  

```python
def modificar_lista(lista):
    lista.append(99)

valores = [10, 20, 30]
modificar_lista(valores)
print(valores)  # Saída: [10, 20, 30, 99]  
```  

Se você vincular um novo objeto a uma variável dentro de uma função, isso não sobrescreverá a variável com o mesmo nome no escopo externo à função (escopo pai).  

```python
def redefinir_lista(lista):
    lista = [0, 0, 0]  # Criando uma nova lista dentro da função
    print("Dentro da função:", lista)

valores = [1, 2, 3]
redefinir_lista(valores)
print("Fora da função:", valores)  # Saída: [1, 2, 3]
```  

Isso acontece porque a variável `lista` dentro da função passa a apontar para um novo objeto, sem modificar o original.  

Outro ponto importante é que as variáveis em Python são dinâmicas e não possuem um tipo fixo. Isso significa que uma variável pode se referir a objetos de tipos diferentes ao longo do tempo, bastando realizar uma nova atribuição.  

```python
x = 10
print(type(x))  # Saída: <class 'int'>

x = "Python"
print(type(x))  # Saída: <class 'str'>
```  

Verificar o tipo de um objeto é essencial, especialmente ao escrever funções flexíveis que lidam com diferentes tipos de entrada. Para isso, a função `isinstance()` pode ser utilizada para confirmar a classe ou tipo de um objeto.  

```python
num = 42

if isinstance(num, int):
    print("É um número inteiro!")
else:
    print("Não é um número inteiro.")
# Saída: É um número inteiro!
```  

---

## Objetos  

Em Python, os objetos geralmente possuem atributos e métodos. Atributos são objetos armazenados dentro de outro objeto, enquanto métodos são funções associadas a um objeto, permitindo o acesso e a manipulação dos dados internos.  

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo
    
    def descricao(self):  # Método
        return f"Carro: {self.marca} {self.modelo}"

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla")

print(meu_carro.marca)  # Saída: Toyota
print(meu_carro.descricao())  # Saída: Carro: Toyota Corolla
```  

Aqui, `marca` e `modelo` são atributos do objeto `meu_carro`, enquanto `descricao()` é um método que retorna uma string formatada.  


## Módulos

Módulos são arquivos contendo código Python, identificados pela extensão `.py`. Eles permitem que você organize e reutilize código, facilitando a manutenção e o desenvolvimento de programas mais complexos.

```python
import exemplo_modulo
```

### Operadores 

São bastante familiares com os das outras linguagens

|                                   |                             | 
|-----------------------------------|-----------------------------|
| ![](/img/banners/operators_1.png) | ![](/img/banners/operators_2.png)                        |


## Strings 

As strings em Python podem ser delimitadas por aspas simples (`'`) ou duplas (`"`). Se uma string contiver o mesmo tipo de aspas usadas para delimitá-la, essas aspas internas devem ser escapadas com uma barra invertida (`\`).  

```python
frase = "Ele disse: \"Python é incrível!\""
print(frase)  # Saída: Ele disse: "Python é incrível!"
```  

Alternativamente, podemos usar aspas diferentes para evitar a necessidade de escape:  

```python
frase = 'Ele disse: "Python é incrível!"'
print(frase)  # Saída: Ele disse: "Python é incrível!"
```

### Concatenação de Strings  

Duas strings podem ser concatenadas usando o operador `+`, resultando em uma nova string.  

```python
saudacao = "Olá, "
nome = "Maria"
mensagem = saudacao + nome  
print(mensagem)  # Saída: Olá, Maria
```  

Também podemos repetir uma string utilizando o operador `*`:  

```python
linha = "-" * 10  
print(linha)  # Saída: ----------
```

### `format()`  

O método `.format()` permite substituir argumentos formatados dentro de uma string, produzindo um novo valor formatado.  

```python
nome = "Carlos"
idade = 30
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)  # Saída: Meu nome é Carlos e eu tenho 30 anos.
```  

Podemos também utilizar índices para referenciar os argumentos:  

```python
mensagem = "Meu nome é {0} e eu tenho {1} anos.".format("Ana", 25)
print(mensagem)  # Saída: Meu nome é Ana e eu tenho 25 anos.
```  

### Especificação de Formato  

Podemos definir como os valores serão formatados dentro da string:  

```python
valor = 12.3456
print("Valor formatado: {:.2f}".format(valor))  # Saída: Valor formatado: 12.35
```

Aqui, `{:.2f}` indica que queremos exibir o número com duas casas decimais.  

Outro exemplo formatando diferentes tipos de dados:  

```python
nome = "Lucas"
idade = 28
altura = 1.75

mensagem = "Nome: {:s}, Idade: {:d}, Altura: {:.2f}m".format(nome, idade, altura)
print(mensagem)  # Saída: Nome: Lucas, Idade: 28, Altura: 1.75m
```

### `F-Strings`

O Python 3.6 introduziu as **f-strings** (formatted string literals), que tornam a formatação de strings mais intuitiva. Para utilizá-las, basta prefixar a string com `f` e incluir expressões Python dentro de chaves `{}`.  

```python
nome = "Mariana"
idade = 22
print(f"Meu nome é {nome} e eu tenho {idade} anos.")  
# Saída: Meu nome é Mariana e eu tenho 22 anos.
```  

As f-strings também suportam formatação avançada:  

```python
valor = 123.456
print(f"Valor formatado: {valor:.2f}")  # Saída: Valor formatado: 123.46
```  

Além disso, podemos realizar cálculos dentro da f-string:  

```python
a = 5
b = 3
print(f"A soma de {a} e {b} é {a + b}.")  # Saída: A soma de 5 e 3 é 8.
```  

## Outros Tipos

### Booleanos   

Em Python, os dois valores booleanos são escritos como `True` (verdadeiro) e `False` (falso). Esses valores podem ser combinados usando as palavras-chave `and` (e) e `or` (ou).  

```python
x = True
y = False
print(x and y)  # Saída: False
print(x or y)   # Saída: True
```  

Se um valor booleano for convertido para um número inteiro, `False` se torna `0` e `True` se torna `1`:  

```python
print(int(True))   # Saída: 1
print(int(False))  # Saída: 0
```  

### None  

Em Python, `None` é um valor especial que representa a ausência de valor. Ele é frequentemente utilizado para indicar que uma variável não tem valor definido ou que uma função não retorna nada.  

```python
x = None
if x is None:
    print("x não tem valor definido.")
# Saída: x não tem valor definido.
```  

## Data e Tempo  

O módulo `datetime` fornece tipos de dados para trabalhar com data e hora, como `datetime`, `date` e `time`. O tipo `datetime` combina informações de `date` (data) e `time` (hora) em um único objeto.  

```python
import datetime
agora = datetime.datetime.now()
print(agora)  # Saída: 2025-02-07 12:34:56.789123
```  

### `datetime`  

Você pode extrair a parte da data ou hora de um objeto `datetime` chamando métodos específicos. O método `date()` retorna a data, e o método `time()` retorna a hora.  

```python
data = agora.date()
hora = agora.time()
print(data)  # Saída: 2025-02-07
print(hora)  # Saída: 12:34:56.789123
```  

O método `strftime()` é usado para formatar um objeto `datetime` como uma string, permitindo a personalização do formato da data e hora.  

```python
formato = agora.strftime("%d/%m/%Y %H:%M:%S")
print(formato)  # Saída: 07/02/2025 12:34:56
```  

### Strings para `datetime`  

Você pode converter uma string em um objeto `datetime` usando a função `strptime()`. Isso é útil quando você tem uma data em formato de string e deseja manipulá-la como um objeto `datetime`.  

```python
data_str = "07/02/2025 12:34:56"
data_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print(data_obj)  # Saída: 2025-02-07 12:34:56
```  

### Modificando Objetos `datetime`  

Como o tipo `datetime` é imutável, qualquer operação que modifique um objeto `datetime` retornará um novo objeto, sem alterar o original. Por exemplo, o método `replace()` pode ser usado para substituir valores específicos, como ano, mês ou dia.  

```python
novo_dt = agora.replace(year=2024)
print(novo_dt)  # Saída: 2024-02-07 12:34:56.789123
```  

Note que o objeto original `agora` não é modificado.  

### `timedelta` 

A diferença entre dois objetos `datetime` resulta em um objeto do tipo `datetime.timedelta`, que representa a diferença entre os dois pontos no tempo.  

```python
delta = agora - novo_dt
print(delta)  # Saída: 366 days, 0:00:00
```

Adicionar um objeto `timedelta` a um `datetime` resulta em um novo `datetime`, deslocado pela quantidade especificada. Isso é útil para realizar cálculos com datas, como adicionar dias ou horas a uma data.  

```python
um_dia = datetime.timedelta(days=1)
nova_data = agora + um_dia
print(nova_data)  # Saída: 2025-02-08 12:34:56.789123
```  

### Operações Com `timedelta`  

As operações com `timedelta` são úteis para manipular dados temporais, como calcular a diferença entre eventos ou adicionar/subtrair tempo de um `datetime`.  

```python
dez_dias = datetime.timedelta(days=10)
data_futura = agora + dez_dias
print(data_futura)  # Saída: 2025-02-17 12:34:56.789123
```  


## Controles de Fluxos 

### `if`, `elif`, e `else`  

Uma instrução `if` pode ser seguida por um ou mais blocos `elif` (abreviação de "else if"), e um bloco `else` opcional, caso todas as condições anteriores sejam avaliadas como **falsas**.  

```python
x = 10
if x > 20:
    print("x é maior que 20")
elif x == 10:
    print("x é igual a 10")
else:
    print("x é menor que 10")
# Saída: x é igual a 10
```  

### `for`  

Laços `for` são usados para iterar sobre uma coleção (como uma lista, tupla, ou dicionário) ou um iterador.  

```python
nomes = ["Ana", "Carlos", "Maria"]
for nome in nomes:
    print(nome)
# Saída:
# Ana
# Carlos
# Maria
```  

Você pode avançar para a próxima iteração de um laço `for`, pulando o restante do bloco, usando a palavra-chave `continue`.  

```python
for i in range(5):
    if i == 2:
        continue  # Pula o restante do código quando i é 2
    print(i)
# Saída:
# 0
# 1
# 3
# 4
```  

### `break`  

Um laço `for` pode ser encerrado completamente com a palavra-chave `break`. Ela interrompe o laço imediatamente, independentemente de onde esteja no bloco de código. Note que, se houver um laço `for` externo, ele não será interrompido — apenas o laço mais interno.  

```python
for i in range(5):
    if i == 3:
        break  # Interrompe o laço quando i é 3
    print(i)
# Saída:
# 0
# 1
# 2
```  

### `while`  

O laço `while` executa um bloco de código enquanto uma condição for **verdadeira**. O laço pode ser interrompido de duas maneiras: até que a condição se torne falsa ou até que o laço seja explicitamente encerrado com a palavra-chave `break`.  

```python
contador = 0
while contador < 3:
    print(contador)
    contador += 1
# Saída:
# 0
# 1
# 2
```  

Se quisermos encerrar o laço antes que a condição seja falsa, podemos usar `break`:  

```python
contador = 0
while True:
    if contador == 2:
        break  # Interrompe o laço quando contador for igual a 2
    print(contador)
    contador += 1
# Saída:
# 0
# 1
```  

### `pass`  

A palavra-chave `pass` é a instrução de "não fazer nada" em Python. Ela pode ser usada em blocos onde nenhuma ação deve ser executada, ou como um espaço reservado para código ainda não implementado.  

```python
def funcao_incompleta():
    pass  # Função ainda não implementada
```  

A palavra-chave `pass` é necessária em Python porque a linguagem usa a indentação para delimitar blocos de código, e um bloco não pode ser deixado vazio.  

### `range`  

A função `range()` gera uma sequência de números inteiros igualmente espaçados, que pode ser convertida em uma lista. Ela pode ter um início, fim e passo (que pode ser negativo).  

```python
for i in range(1, 10, 2):  # Começa em 1, vai até 10, com um passo de 2
    print(i)
# Saída:
# 1
# 3
# 5
# 7
# 9
```  

Por padrão, `range` exclui o valor final, ou seja, ele gera números até, mas **não incluindo** o número final.  

```python
for i in range(5):  # Vai de 0 até 4
    print(i)
# Saída:
# 0
# 1
# 2
# 3
# 4
```  

Um uso comum do `range` é para iterar através de sequências pelo índice:  

```python
nomes = ["Ana", "Carlos", "Maria"]
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}")
# Saída:
# Índice 0: Ana
# Índice 1: Carlos
# Índice 2: Maria
```  


- - -



# Estrutura de Dados

- - -

# Aplicações e Desenvolvimento de Funçõe

- - -

# Módulo Numpy

- - -

# Módulo Pandas

- - -

# Outros Modulos Interessantes

- - -

# Plotagem e Visualização

- - -

# Paralelismo

- - -

# Otimizações (PyPy/Numba/Ctypes)
