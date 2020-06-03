# coding: utf-8
# Reconhecimento de dígitos manuscritos
import os
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from digit_model import net
from digit_data import read_train_data

ARQUIVO_REDE = 'digitos.pth'

def treina(input, output, iteracoes=1000):
    # Critério de erros
    criterion = nn.MSELoss()
    # Otimizador - gradiente descendente
    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.5)

    for epoch in range(iteracoes):
        for i, input_data in enumerate(input): # para cada dado de teste
            I = Variable(torch.FloatTensor(input_data), requires_grad=True)
            O = Variable(torch.FloatTensor(output[i]), requires_grad=True)
            optimizer.zero_grad() # zera o gradiente de erro
            outputs = net(I) # calcula a saída
            loss = criterion(outputs, O) # calcula o erro
            loss.backward() # popula o gradiente
            optimizer.step() # modifica os pesos baseado no gradiente
            if (i % 10 == 0): # a cada 10 iterações, exibe o erro
                print("Iteração {} - Erro: {}".format(epoch, loss.item()))

if __name__ == '__main__':
    if not os.path.exists(ARQUIVO_REDE):
        print('Treinando a rede ...')
        train_data = read_train_data() # lê os dados de treinamento
        treina(train_data[0], train_data[1])
        print('Salvando o arquivo da rede')
        torch.save(net.state_dict(), ARQUIVO_REDE)
        print('Pronto')
    else:
        print('A rede já está treinada')
