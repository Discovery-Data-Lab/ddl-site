---
title: "Introduction to Neural Networks in C: Building from Scratch"
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
Neural Networks (NN) have gained popularity due to their ability to model complex problems in areas like image recognition, natural language processing, and autonomous systems. Understanding how neural networks work internally can be beneficial, especially for those in computer science and cybersecurity, where you may need to work with efficient, low-level implementations of AI systems.

In this post, we'll introduce you to building a basic neural network from scratch using the C programming language. C is ideal for this because it allows us to manage memory and computation efficiently. This guide assumes you're familiar with basic C programming concepts such as arrays, loops, and functions.

### 1. **What is a Neural Network?**

A neural network is composed of neurons, inspired by biological neurons, arranged in layers:

* **Input Layer**: Accepts inputs (e.g., image pixels).
* **Hidden Layers**: Process input data through weighted connections.
* **Output Layer**: Produces the final output (e.g., classifying an image).

Each neuron has a value, calculated using the weighted sum of its inputs followed by a non-linear function (called an activation function). The network adjusts these weights during training to minimize errors using a process called backpropagation.

### 2. **Key Concepts**

Before diving into the implementation, it’s important to clarify a few key terms:

* **Weights**: Values that adjust the strength of connections between neurons.
* **Bias**: An extra value added to the weighted sum of inputs to allow the model to fit data better.
* **Activation Function**: Non-linear function applied to the neuron output, enabling the network to solve complex problems. Common functions include Sigmoid, ReLU (Rectified Linear Unit), and Tanh.
* **Forward Propagation**: Process of calculating the outputs of neurons layer by layer from input to output.
* **Backpropagation**: The training algorithm used to minimize errors by adjusting weights and biases using gradient descent.

### 3. **Setting Up the Structure**

In C, we can represent the neural network using arrays and structures. Let's first define a basic structure for a neural network layer.

#### Define the Neuron and Layer Structures:

```c
typedef struct {
    int num_inputs;
    float *weights;   // Array to store weights
    float bias;       // Bias value for the neuron
} Neuron;

typedef struct {
    int num_neurons;
    Neuron *neurons;  // Array of neurons
} Layer;
```

Here, each neuron stores its own weights and bias. Each layer has a number of neurons.

#### Initialize the Neurons and Layers:

```c
Neuron create_neuron(int num_inputs) {
    Neuron neuron;
    neuron.num_inputs = num_inputs;
    neuron.weights = (float *)malloc(sizeof(float) * num_inputs);

    // Initialize weights and bias with random values
    for (int i = 0; i < num_inputs; i++) {
        neuron.weights[i] = ((float) rand()) / RAND_MAX;  // Random float [0,1]
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

This code sets up a basic layer with random weights and biases. Every neuron in the layer will have a weight associated with each input.

### 4. **Forward Propagation**

The next step is to implement the forward propagation, where we calculate the output of each neuron in the layer by applying the weights to the inputs and passing the result through an activation function (e.g., Sigmoid).

#### Activation Function (Sigmoid):

```c
float sigmoid(float x) {
    return 1.0f / (1.0f + expf(-x));
}
```

#### Compute Output for a Neuron:

```c
float compute_neuron_output(Neuron neuron, float *inputs) {
    float output = 0.0f;
    for (int i = 0; i < neuron.num_inputs; i++) {
        output += neuron.weights[i] * inputs[i];
    }
    output += neuron.bias;
    return sigmoid(output);  // Apply activation function
}
```

#### Forward Propagation for a Layer:

```c
void forward(Layer layer, float *inputs, float *outputs) {
    for (int i = 0; i < layer.num_neurons; i++) {
        outputs[i] = compute_neuron_output(layer.neurons[i], inputs);
    }
}
```

This performs forward propagation through a layer, computing the output for each neuron based on the inputs.

### 5. **Creating the Neural Network**

We can define a network as an array of layers. For simplicity, we'll assume our network has one hidden layer and one output layer.

```c
typedef struct {
    int num_layers;
    Layer *layers;  // Array of layers
} NeuralNetwork;

NeuralNetwork create_network(int num_inputs, int num_hidden_neurons, int num_output_neurons) {
    NeuralNetwork network;
    network.num_layers = 2;  // One hidden layer, one output layer
    network.layers = (Layer *)malloc(sizeof(Layer) * network.num_layers);

    network.layers[0] = create_layer(num_hidden_neurons, num_inputs);     // Hidden layer
    network.layers[1] = create_layer(num_output_neurons, num_hidden_neurons);  // Output layer

    return network;
}

void forward_network(NeuralNetwork network, float *inputs, float *outputs) {
    float *hidden_outputs = (float *)malloc(sizeof(float) * network.layers[0].num_neurons);
    forward(network.layers[0], inputs, hidden_outputs);  // Forward pass through hidden layer

    forward(network.layers[1], hidden_outputs, outputs);  // Forward pass through output layer
    free(hidden_outputs);
}
```

This code defines the structure of the neural network and how to propagate inputs through it. You can create a network with a specified number of hidden and output neurons and use `forward_network` to process an input.

### 6. **Training the Network: Backpropagation (Overview)**

Backpropagation is used to adjust the weights and biases based on the error in the output. In this simple introduction, we won’t implement backpropagation, but the idea is to:

1. **Compute the error** between the predicted output and the actual output.
2. **Calculate the gradient** of the loss function with respect to each weight and bias.
3. **Update weights** using gradient descent.

Training involves repeatedly feeding inputs through the network, computing the error, and updating the weights until the network can accurately predict outputs.

### Conclusion

In this post, we've covered the basics of building a neural network from scratch in C, focusing on setting up the structure and forward propagation. This fundamental understanding of neural networks in C will give you insight into how machine learning models work behind the scenes and prepare you to explore more advanced concepts like backpropagation and optimization.

Further improvements could include implementing different activation functions, adding more layers, or experimenting with backpropagation for training the network.
