import os

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

  input_data = []
  output_data = []

  for i in range(0, 10):
    diretorio = os.path.join(DIRETORIO_DIGITOS, str(i))
    for fname in os.listdir(diretorio):
      arquivo = open(os.path.join(diretorio, fname), 'r')
      linha = arquivo.readline()
      input_data.append(list(map(lambda x: int(x), linha.split(','))))
      output_data.append(possible_outs[i])
      arquivo.close()
  
  return (input_data, output_data)