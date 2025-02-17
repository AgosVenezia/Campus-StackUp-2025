# -*- coding: utf-8 -*-
"""PyTorch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l_L48VsB6DEtmkt8bx27DrpfCzQoJQM2

Tensors
"""

import torch
x = torch.tensor([1.0, 2.0, 3.0])
print(x)

"""Neural Networks"""

import torch
from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

"""Loading Pre-Trained Models"""

import torchvision.models as models
model = models.mobilenet_v3_small(pretrained=True)

"""Training and Inference"""

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(10):  # Train for 10 epochs
    outputs = model(inputs)
    loss = loss_fn(outputs, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()