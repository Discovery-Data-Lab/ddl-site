+++
title = "Uma Biblioteca Livre de Detecçao de Comunidades"
date = "2025-02-10T11:00:00+02:00"
tags = ["mineração de dados", "redes complexas", "ciências de dados"]
categories = ["dados", "redes"]
description = "Este trabalho tem como objetivo investigar formulações de otimização multiobjetivo para detecção de comunidades utilizando algoritmos evolutivos multiobjetivos para encontrar soluções eficientes."
banner = "img/banners/community detection.png"
authors = ["Guilherme Oliveira"]
+++


# Disponibilidade

![](/img/banners/remocd.png)

O algoritmo _Rapid Evolutionary Multi-objective Community Detection_ (**re-mocd**) está disponível como um projeto de código livre no [GitHub](https://github.com/0l1ve1r4/mocd), onde você pode escolher compilá-lo a partir do código-fonte ou usar a biblioteca pré-compilada a partir das releases. Ele também está disponível no [PyPI do Python](https://pypi.org/project/rmocd/), permitindo instalação e uso de forma simples. Na data de publicação, a biblioteca possui **48** arquivos e **1.956** linhas de código. A biblioteca suporta dois modos de operação: via interface de linha de comando (CLI) ou por meio de chamadas diretas de funções utilizando a biblioteca PyPI.

## Uso no PyPI

```bash
pip install re-mocd
```

Para a versão em Rust, será necessário construí-la a partir do código-fonte. As instruções para a construção podem ser encontradas no repositório oficial. A função `run_rmocd` pode ser chamada da seguinte forma:

```python
import re_mocd
import networkx as nx

G nx.Graph([
   (0, 1), (0, 3), (0, 7),
   (1, 2), (1, 3), (1, 5), 
   (2, 3), 
   (3, 6), 
   (4, 5), 
   (4, 6), 
   (5, 6), 
   (7, 8)
   ])

partição = re_mocd.from_nx(G)
```
Dado o grafo acima definido pela biblioteca `networkx`, a função gerou a seguinte partição:
```
{0: 4, 1: 4, 2: 4, 3: 4, 4: 1, 5: 1, 6: 1, 7: 3, 8: 3}
```
Nesta representação, cada entrada corresponde a um par `node:id`, indicando a comunidade à qual cada nó pertence.


![](/img/banners/exampleremocd.png)




#  Otimizaçao


O objetivo principal de construir este algoritmo é superar o algoritmo[^shi] em termos de velocidade. O tratamento eficiente de grandes grafos é crucial para muitas aplicações, tornando isso um marco importante para o sucesso.

Abaixo estão algumas comparações de desempenho:

- O algoritmo original não fornece o tempo de execução exato para cada conjunto de dados, apenas o tempo médio por arquivo. Usando a mesma abordagem, o tempo médio de execução do algoritmo proposto em todos os arquivos é de 5,92 segundos, em comparação com 223 segundos. Isso demonstra que o algoritmo proposto é aproximadamente **37,7 vezes mais rápido**.

## Função Objetivo

A parte mais cara do algoritmo em termos computacionais é a função objetivo, que corresponde à Equação (3.4)[^shi]:

$$
Q(C) = \sum_{c \in C} \left[ \frac{|E(c)|}{m} - \left( \frac{\sum_{v \in c} \text{deg}(v)}{2m} \right)^2 \right],
$$

onde $(|E(c)|)$ é o número de arestas dentro da comunidade $\(c\), \(m\)$ é o número total de arestas, $\(\text{deg}(v)\)$ é o grau do nó $\(v\)$, e $\(C\)$ é o conjunto de comunidades. Os dois termos refletem a densidade intra-comunidade e a conectividade inter-comunidade.

Na nossa implementação, a complexidade de computação correspondente pode ser detalhada da seguinte forma:

1. A construção da partição em comunidades envolve iterar por todos os nós e inseri-los em um `HashMap`. Essa operação tem uma complexidade $\(O(V)\)$, onde $\(V\)$ é o número de nós.
2. Para cada comunidade:
   - Iterar por todos os nós da comunidade.
   - Para cada nó, recuperar seu grau pré-computado $(\(O(1)\))$ e iterar sobre seus vizinhos. Para cada vizinho, uma busca binária verifica a associação na comunidade $O(\log |C|)$, onde $\|C|\$ é o tamanho da comunidade).
   - Como os graus do grafo são pré-computados uma vez, a complexidade para processar uma única comunidade é aproximadamente:

$$
O(|C| \cdot \log |C|),
$$

removendo a dependência do grau $d$.

3. A agregação dos resultados para $k$ comunidades resulta em:

$$
O(k \cdot |C| \cdot \log |C|) = O(V \cdot \log (V / k)).
$$

A paralelização foi realizada utilizando o `par_iter()` da biblioteca Rayon, que distribui a carga de trabalho do processamento das comunidades por múltiplos threads. Isso reduz a carga de trabalho efetiva por thread por um fator $p$, onde $p$ é o número de threads. A complexidade resultante por thread é:

$$
O\left(\frac{V \cdot \log (V / k)}{p}\right).
$$

Isso reduz significativamente o tempo de computação para grafos grandes. Abaixo, $N$ representa a complexidade de tempo resultante do algoritmo, e $E$ do algoritmo original:

$$
N = O\left( \frac{G \cdot P^2 \cdot \left( V \cdot \log \left( \frac{V}{k} \right) \right)}{p} \right) \quad \text{e} \quad E = O(gs^2(m + n)).
$$

# Operadores Geneticos

## Limitações dos Operadores Genéticos Tradicionais

### **Desafios do Crossover**

A operação de **crossover** combina segmentos de duas soluções pais para produzir descendentes. Um método comumente utilizado, o crossover uniforme de dois pontos, é descrito da seguinte forma:

> Escolhemos o crossover uniforme de dois pontos porque ele é imparcial em relação à ordem dos genes e pode gerar qualquer combinação de alelos a partir dos dois pais.

Embora seja versátil, essa abordagem é problemática para a detecção de comunidades devido aos seguintes motivos:
- **Falta de percepção estrutural**: Os pontos de crossover são escolhidos sem considerar a partição do grafo ou as propriedades estruturais.
- **Degradação da qualidade**: Os descendentes frequentemente não preservam as características das comunidades bem formadas, levando a soluções subótimas.

### **Desafios da Mutação**
A mutação introduz pequenas mudanças aleatórias nas soluções para manter a diversidade genética. Na implementação tradicional[^shi] explica:

> Na operação de mutação, selecionamos aleatoriamente alguns genes e os atribuímos a outros nós adjacentes selecionados aleatoriamente.

No entanto, essa abordagem apresenta várias desvantagens:
- **Mudanças cegas ao contexto**: Ignora o contexto mais amplo da solução, frequentemente perturbando a integridade estrutural da partição.
- **Ineficácia aleatória**: As mutações podem levar a soluções mal construídas, particularmente quando nós críticos para a estrutura da comunidade são alterados de forma indiscriminada.

### **Desafios da Inicialização**
A população inicial estabelece a base para o progresso evolutivo. descreve o processo tradicional de inicialização:

> No processo de inicialização, geramos indivíduos aleatoriamente. Para cada indivíduo, cada gene $g_i$ escolhe aleatoriamente um dos nós adjacentes ao nó $i$.

Os principais problemas incluem:
- **Pontos de partida de baixa qualidade**: Partições aleatórias provavelmente não refletem estruturas de comunidade significativas.
- **Ineficácia na busca**: Começar muito longe de soluções promissoras dificulta a convergência no vasto espaço de busca.

---

## Operadores Genéticos Otimizados

### **Crossover Inteligente**
   - Garantimos que o segundo ponto nunca esteja muito próximo do primeiro, limitando a extensão do crossover e prevenindo mudanças estruturais drásticas, além de preservar relações chave entre as comunidades, garantindo que as comunidades não sejam divididas ou mescladas arbitrariamente.

#### **Mutação Inteligente**
   - Um cache de frequência é construído para analisar as comunidades dos vizinhos de um nó antes de decidir sua atribuição.
   - Após construir o mapa de frequência das comunidades dos vizinhos de um nó, a função seleciona a comunidade mais frequente.
   - Os nós para mutação são selecionados com base em uma taxa de mutação controlada (0,3), diferente da proposta de 0,6.


### Results and Advantages


## Referencias

[^shi]:Chuan Shi a, Zhenyu Yan, Yanan Cai, Bin Wu. **Multi-objective community detection in complex networks**. *Elsevier*, Beijing University of Posts and Telecommunications, Beijing Key Laboratory of Intelligent Telecommunications Software and Multimedia, Beijing 100876, China. Research Department, Fair Isaac Corporation (FICO), San Rafael, CA 94903, USA.
Available at: [https://www.sciencedirect.com/](https://www.sciencedirect.com/science/article/abs/pii/S1568494611003991)