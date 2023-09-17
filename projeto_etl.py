import csv
from csv import reader

''' -----
Extract:

Ler arquivo .csv e organizando as informações em lista.
----- '''
arquivo = open('investidores.csv', 'r')
dados = list(csv.reader(arquivo,delimiter=','))
''' -----
Transform: 
     
  Verificar o perfil do cliente com base nas preferências de volatidade e 
  apresentar o cálculo do investimento de cada ação:
     baixa -> perfil conservador: oferecer carteira de investimento 100% renda fixa
     média -> perfil Moderado: oferecer investimentos 60% renda fixa e 40% ações
     alta -> arrojado: oferecer investimentos 70% ações e 30% renda fixa
       
  criar um novo item ('ação') na primeira lista (cabeçalho) para guardar
  as orientações
  
  criar uma lista (tabela) para guardar as listas tratadas (matriz)
------ '''
tabela = list()	

for dado in dados:
     if dado[3] == 'baixa':
          valores = dado[2]
          dado.append(f'Seu perfil é conservador. O ideal seria investir R$ {valores} em renda fixa')
          tabela.append(dado)
     
     elif dado[3] == 'media':
          valores = dado[2]
          fixa = float(valores) * 0.60
          acoes = float(valores) - fixa
          dado.append(f'Seu perfil é moderado. O ideal seria investir R${fixa: .2f} em renda fixa e R${acoes: .2f} em ações')
          tabela.append(dado)
     
     elif dado[3] == 'alta':
          valores = dado[2]
          fixa = float(valores) * 0.30
          acoes = float(valores) - fixa
          dado.append(f'Seu perfil é arrojado. O ideal seria investir R${fixa: .2f} em renda fixa e R${acoes: .2f} em ações')
          tabela.append(dado)
     else:
          dado.append('analise')
          tabela.append(dado)

novo_arquivo =  open('solucoes.csv', 'w', newline='')
solucoes = csv.writer(novo_arquivo, delimiter=',')
solucoes.writerows(tabela)

arquivo.close()
novo_arquivo.close()
