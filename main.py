import sys
import os
import math
import csv


aux = ''
soma_sl = 0
soma_sw = 0
soma_pl = 0
soma_pw = 0
var = 0
n = 0
lines = []
centroids = []
dist_centroid = 0

with open("iris.csv", newline = '') as file:
    reader = csv.reader(file)
    lines = list(reader)

aux = str(lines[1]).split(',')[4].replace("'", '').replace(']', '').strip()

for i in range(1, len(lines)):
  
  line = str(lines[i]).strip().split(',')
  
  line = str(line).replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(' ','')
  
  
  soma_sl+= float(str(line).split(',')[0])
  soma_sw+= float(str(line).split(',')[1])
  soma_pl+= float(str(line).split(',')[2])
  soma_pw+= float(str(line).split(',')[3])
  n+= 1
  
  if str(line).split(',')[4] != aux or i == len(lines)-1:
   
    centroids.append(
      str(round(soma_sl / n, 3)) + ','  
      + str(round(soma_sw / n, 3)) + ','
      + str(round(soma_pl / n, 3)) + ','
      + str(round(soma_pw / n, 3)) + ','
      + str(aux))

    soma_sl = float(str(line).split(',')[0])
    soma_sw = float(str(line).split(',')[1])
    soma_pl = float(str(line).split(',')[2])
    soma_pw = float(str(line).split(',')[3])
    n = 1
    
    aux = str(line).split(',')[4].strip()


#os.system('clear')
print(centroids)
print('\nNº de Centroides: ' + str(len(centroids)))
print('\n')

#Gerando vetores de testes. Aqui são feitos os testes.
point_sl_test = 2.3
point_sw_test = 3.4
point_pl_test = 2.7
point_pw_test = 4.3

for j in range(0, len(centroids)):
  line_centroid = str(centroids[j])

  dist_centroid = math.sqrt((float(point_sl_test) - float(line_centroid.split(',')[0]))**2 + (float(point_sw_test) - float(line_centroid.split(',')[1]))**2 + (float(point_pl_test) - float(line_centroid.split(',')[2]))**2 + (float(point_pw_test) - float(line_centroid.split(',')[3]))**2)
  
  print("Distância do 'point_test' ao Centroide {} = {}".format(j+1, round(dist_centroid, 3)))
