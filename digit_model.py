# coding: utf-8
# Reconhecimento de dígitos manuscritos
import torch
import torch.nn as nn
import torch.nn.functional as F

# Criação da rede neural
class DigitosModel(nn.Module):
    def __init__(self):
        super(DigitosModel, self).__init__()
        # Duas camadas
        self.fc1 = nn.Linear(16 * 16, 64 * 64)
        self.fc2 = nn.Linear(64 * 64, 4 * 4)
        self.fc3 = nn.Linear(4 * 4, 10)

    def forward(self, x):
        # As camadas são conectadas por uma função de ativação (ReLU)
        return self.fc3(F.relu(self.fc2(F.relu(self.fc1(x)))))

net = DigitosModel() # Criamos uma instância da rede neural
