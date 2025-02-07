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
banner: /img/banners/11042_2020_8700_fig1_html.png
authors:
  - Guilherme Oliveira
  - Carlos Henrique G. Ferreira
---

A ciência de dados é o processo de analisar grandes conjuntos de dados para descobrir padrões. Combina estatísticas, programação e conhecimento do domínio. Aqui, iremos trazer um guia completo sobre este tema para ajudar novas pessoas na área.

<!--more-->

# Agradecimentos

Gostaria de expressar minha profunda gratidão ao [Prof. Dr. Carlos Henrique G. Ferreira](https://www.researchgate.net/profile/Carlos-G-Ferreira). Parte do material apresentado neste curso foi desenvolvido com base em seus ensinamentos do curso **Projeto e Análise de Experimentos**, ministrado no **[ICEA](https://icea20anos.ufop.br/)**. Sua expertise e dedicação foram fundamentais para a construção deste conteúdo, que tem como objetivo auxiliar estudantes e profissionais no aprimoramento de suas habilidades.

- - -

# Introdução a Python

Python é uma das linguagens de programação mais populares para análise de dados e computação científica devido à sua simplicidade, versatilidade e uma comunidade extremamente ativa. Com um vasto ecossistema de bibliotecas de código aberto, como [Pandas](https://pandas.pydata.org/) e [Scikit-learn](https://scikit-learn.org/), tornou-se uma escolha dominante para cientistas de dados e pesquisadores.


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
| Rust                               | 0,10                        | ± 0,1                  |
| C                                  | 0,19                        | ± 0,1                  |
| Python                             | **3,17**                    | ± 0,1                  |
| Rust (Threading)                   | 0,03                        | ± 0,1                  |
| C (Threading)                      | 0,11                        | ± 0,2                  |
| Python (Multiprocessing)           | **0,77**                    | ± 0,2                  |
| Python (Multiprocessing + PyPy)    | **0,09**                    | ± 0,2                  |

Os resultados demonstram que a performance pode variar significativamente, especialmente no Python. No entanto, observa-se que o uso de paralelismo e otimizações como `PyPy` podem reduzir consideravelmente esse impacto. Ainda assim, linguagens compiladas continuam a apresentar desempenho superior em termos de velocidade.  

---

## Ambientes de Execução

Para começar a programar em Python, faça o download da versão mais recente no site oficial ([python.org](https://www.python.org)) e instale-a em sua máquina.

Python pode ser executado diretamente no terminal com o comando:
```
python
```

Outras opções incluem:

- **IPython**: Um interpretador interativo que oferece funcionalidades avançadas.
- **Jupyter Notebook**: Um ambiente baseado na web para código interativo, muito utilizado em análise de dados e pesquisa científica.

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
