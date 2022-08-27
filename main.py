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


with open("iris.csv", newline='') as file:
    reader = csv.reader(file)
    lines = list(reader)

lines.__delitem__(0)
aux = lines[0][4]

for i in range(len(lines)):
    line = lines[i]

    soma_sl += float(line[0])
    soma_sw += float(line[1])
    soma_pl += float(line[2])
    soma_pw += float(line[3])
    n += 1

    if line[4] != aux or i == len(lines) - 1:

        centroids.append(
            str(round(soma_sl / n, 3)) + ',' + str(round(soma_sw / n, 3)) +
            ',' + str(round(soma_pl / n, 3)) + ',' +
            str(round(soma_pw / n, 3)) + ',' + aux)

        soma_sl = float(line[0])
        soma_sw = float(line[1])
        soma_pl = float(line[2])
        soma_pw = float(line[3])
        n = 1

        aux = str(line[4])

print(centroids)
print('\nNº de Centroides: ' + str(len(centroids)))
print('\n')

#Gerando vetores de testes. Aqui são feitos os testes.
point_sl_test = 2.3
point_sw_test = 3.4
point_pl_test = 2.7
point_pw_test = 4.3

for j in range(len(centroids)):
    line_centroid = str(centroids[j]).split(',')

    dist_centroid = math.sqrt(
        (point_sl_test - float(line_centroid[0]))**2 +
        (point_sw_test - float(line_centroid[1]))**2 +
        (point_pl_test - float(line_centroid[2]))**2 +
        (point_pw_test - float(line_centroid[3]))**2
    )

    print("Distância do 'point_test' ao Centroide {} = {}".format(
        j + 1, round(dist_centroid, 3)))
  