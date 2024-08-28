import random
def mostrar_matriz(a):
    for filas in range(len(matriz)):
        for colum in range(len(matriz[0])):
            print(f"{a[filas][colum] : ^10}", end=" ")
        print()

def promedio_alumnos(b):
    for i in range(1, len(b)):
        notas = 0
        for f in range(1, len(b[0])):
            notas += b[i][f]
        promedio = notas / f
        print(f"LU {b[i][0]} tiene un promedio de {promedio}")
    print()

def promedio_materias(c):
    for i in range(1, len(c[0])):
        notas = 0

        for f in range(1, len(c)):
            notas += c[f][i]

        promedio = notas / f
        print(f"Materia {c[i][0]} tiene un promedio de {promedio}")
    print()        

materias = ["LU", "matematica", "historia", "ingles", "filosofia"]
estudiantes = [1, 2, 3, 4, 5]
matriz = []
for fil in range(len(estudiantes) + 1):
    matriz.append([])
    for col in range(len(materias)):
        matriz[fil].append(0)
flag = -1
for i in range(len(matriz)):
    for f in range(len(matriz[0])):
        if i == 0:
            matriz[i][f] = materias[f]
        else:
            matriz[i][f] = estudiantes[flag]
    flag += 1
for j in range(1, len(matriz)):
    for i in range(1, len(matriz[0]) - 1):
        matriz[j][i] = random.randint(1, 10)

mostrar_matriz(matriz)
promedio_alumnos(matriz)
promedio_materias(matriz)