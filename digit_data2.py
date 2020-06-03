import os
import pandas as pd

DIRETORIO_DIGITOS = 'digitos'

possible_outs = [[1,0,0,0,0,0,0,0,0,0], # 0
                [0,1,0,0,0,0,0,0,0,0],  # 1
                [0,0,1,0,0,0,0,0,0,0],  # 2
                [0,0,0,1,0,0,0,0,0,0],  # 3
                [0,0,0,0,1,0,0,0,0,0],  # 4
                [0,0,0,0,0,1,0,0,0,0],  # 5
                [0,0,0,0,0,0,1,0,0,0],  # 6
                [0,0,0,0,0,0,0,1,0,0],  # 7
                [0,0,0,0,0,0,0,0,1,0],  # 8
                [0,0,0,0,0,0,0,0,0,1]]  # 9

def read_train_data():
  global possible_outs

  input_data  = []
  output_data = []

  for i in range(0, 10):
    diretorio = os.path.join(DIRETORIO_DIGITOS, str(i))
    for fname in os.listdir(diretorio):
      imagem = os.path.join(diretorio, fname)
      input_data.append(pd.read_csv(imagem, header=None).transpose().squeeze().values)
      output_data.append(possible_outs[i])
  
  return (input_data, output_data)