---
title: "Introdução a Redes Neurais em C: Construindo do ZERO!"
date: 2024-10-10T12:04:00.000Z
tags:
  - inteligência artificial
  - aprendizado de máquina
  - redes neurais
categories:
  - inteligência artificial
description: Um guia introdutório sobre redes neurais artificiais, cobrindo
  conceitos como neurônios, camadas, e o processo de aprendizado.
banner: img/banners/ann-banner.png
authors:
  - Guilherme Oliveira
---

**Redes Neurais (NN)** têm ganhado popularidade devido à sua capacidade de modelar problemas complexos em áreas como reconhecimento de imagens, processamento de linguagem natural e sistemas autônomos. Compreender como as redes neurais funcionam internamente pode ser benéfico, especialmente para aqueles na ciência da computação e segurança cibernética, onde você pode precisar trabalhar com implementações eficientes e de baixo nível de sistemas de IA.

Neste post, apresentaremos como construir uma rede neural básica do zero usando a linguagem de programação C. O C é ideal para isso porque permite gerenciar memória e computação de forma eficiente. Este guia assume que você está familiarizado com conceitos básicos de programação em C, como arrays, loops e funções.

### 1. **O que é uma Rede Neural?**

Uma rede neural é composta de neurônios, inspirados pelos neurônios biológicos, organizados em camadas:

* **Camada de Entrada**: Aceita entradas (por exemplo, pixels de uma imagem).
* **Camadas Ocultas**: Processam os dados de entrada por meio de conexões ponderadas.
* **Camada de Saída**: Produz a saída final (por exemplo, classificação de uma imagem).

Cada neurônio tem um valor, calculado usando a soma ponderada de suas entradas seguida de uma função não-linear (chamada função de ativação). A rede ajusta esses pesos durante o treinamento para minimizar erros por meio de um processo chamado backpropagation (retropropagação).

### 2. **Conceitos-chave**

Antes de mergulhar na implementação, é importante esclarecer alguns termos-chave:

* **Pesos**: Valores que ajustam a força das conexões entre neurônios.
* **Bias (Viés)**: Um valor extra adicionado à soma ponderada das entradas para permitir que o modelo se ajuste melhor aos dados.
* **Função de Ativação**: Função não-linear aplicada à saída do neurônio, permitindo que a rede resolva problemas complexos. Funções comuns incluem Sigmoid, ReLU (Unidade Linear Retificada) e Tanh.
* **Propagação Direta**: Processo de calcular as saídas dos neurônios camada por camada, da entrada à saída.
* **Backpropagation**: O algoritmo de treinamento usado para minimizar erros ajustando pesos e vieses utilizando descida do gradiente.

### 3. **Configurando a Estrutura**

Em C, podemos representar a rede neural usando arrays e estruturas. Primeiro, vamos definir uma estrutura básica para uma camada de rede neural.

#### Definir as Estruturas do Neurônio e da Camada:

```c
typedef struct {
    int num_inputs;
    float *weights;   // Array para armazenar os pesos
    float bias;       // Valor de viés para o neurônio
} Neuron;

typedef struct {
    int num_neurons;
    Neuron *neurons;  // Array de neurônios
} Layer;
```

Aqui, cada neurônio armazena seus próprios pesos e viés. Cada camada tem um número de neurônios.

#### Inicializar os Neurônios e Camadas:

```c
Neuron create_neuron(int num_inputs) {
    Neuron neuron;
    neuron.num_inputs = num_inputs;
    neuron.weights = (float *)malloc(sizeof(float) * num_inputs);

    // Inicializa os pesos e o viés com valores aleatórios
    for (int i = 0; i < num_inputs; i++) {
        neuron.weights[i] = ((float) rand()) / RAND_MAX;  // Float aleatório [0,1]
    }
    neuron.bias = ((float) rand()) / RAND_MAX;
    return neuron;
}

Layer create_layer(int num_neurons, int num_inputs) {
    Layer layer;
    layer.num_neurons = num_neurons;
    layer.neurons = (Neuron *)malloc(sizeof(Neuron) * num_neurons);

    for (int i = 0; i < num_neurons; i++) {
        layer.neurons[i] = create_neuron(num_inputs);
    }
    return layer;
}
```

Esse código configura uma camada básica com pesos e vieses aleatórios. Cada neurônio na camada terá um peso associado a cada entrada.

### 4. **Propagação Direta**

O próximo passo é implementar a propagação direta, onde calculamos a saída de cada neurônio na camada aplicando os pesos às entradas e passando o resultado por uma função de ativação (por exemplo, Sigmoid).

#### Função de Ativação (Sigmoid):

```c
float sigmoid(float x) {
    return 1.0f / (1.0f + expf(-x));
}
```

#### Calcular a Saída de um Neurônio:

```c
float compute_neuron_output(Neuron neuron, float *inputs) {
    float output = 0.0f;
    for (int i = 0; i < neuron.num_inputs; i++) {
        output += neuron.weights[i] * inputs[i];
    }
    output += neuron.bias;
    return sigmoid(output);  // Aplica a função de ativação
}
```

#### Propagação Direta para uma Camada:

```c
void forward(Layer layer, float *inputs, float *outputs) {
    for (int i = 0; i < layer.num_neurons; i++) {
        outputs[i] = compute_neuron_output(layer.neurons[i], inputs);
    }
}
```

Isso realiza a propagação direta através de uma camada, calculando a saída para cada neurônio com base nas entradas.

### 5. **Criando a Rede Neural**

Podemos definir uma rede como um array de camadas. Para simplificar, vamos assumir que nossa rede tem uma camada oculta e uma camada de saída.

```c
typedef struct {
    int num_layers;
    Layer *layers;  // Array de camadas
} NeuralNetwork;

NeuralNetwork create_network(int num_inputs, int num_hidden_neurons, int num_output_neurons) {
    NeuralNetwork network;
    network.num_layers = 2;  // Uma camada oculta e uma camada de saída
    network.layers = (Layer *)malloc(sizeof(Layer) * network.num_layers);

    network.layers[0] = create_layer(num_hidden_neurons, num_inputs);     // Camada oculta
    network.layers[1] = create_layer(num_output_neurons, num_hidden_neurons);  // Camada de saída

    return network;
}

void forward_network(NeuralNetwork network, float *inputs, float *outputs) {
    float *hidden_outputs = (float *)malloc(sizeof(float) * network.layers[0].num_neurons);
    forward(network.layers[0], inputs, hidden_outputs);  // Passa pela camada oculta

    forward(network.layers[1], hidden_outputs, outputs);  // Passa pela camada de saída
    free(hidden_outputs);
}
```

Esse código define a estrutura da rede neural e como propagar as entradas através dela. Você pode criar uma rede com um número específico de neurônios ocultos e de saída e usar `forward_network` para processar uma entrada.

### 6. **Treinando a Rede: Backpropagation (Visão Geral)**

Backpropagation é usado para ajustar os pesos e vieses com base no erro da saída. Nesta introdução simples, não implementaremos o backpropagation, mas a ideia é:

1. **Calcular o erro** entre a saída prevista e a saída real.
2. **Calcular o gradiente** da função de perda em relação a cada peso e viés.
3. **Atualizar os pesos** usando a descida do gradiente.

O treinamento envolve alimentar repetidamente entradas na rede, calcular o erro e ajustar os pesos até que a rede possa prever saídas com precisão.

### Conclusão

Neste post, abordamos os fundamentos de como construir uma rede neural do zero em C, focando na configuração da estrutura e na propagação direta. Essa compreensão fundamental de redes neurais em C fornecerá uma visão de como os modelos de aprendizado de máquina funcionam nos bastidores e preparará você para explorar conceitos mais avançados, como backpropagation e otimização.

Melhorias futuras podem incluir a implementação de diferentes funções de ativação, adicionar mais camadas ou experimentar o backpropagation para treinar a rede.
