def show_matriz_transposta(matriz: list) -> None:
    rows = len(matriz)
    columns = len(matriz[0])

    print("Matriz:")
    for i in range(rows):
        for j in range(columns):
            print(matriz[i][j], end=" ")
        print()

    print("\nMatriz Transposta:", )
    for i in range(rows):
        for j in range(columns):
            print(matriz[j][i], end=" ")
        print()

matriz = [
    [1,2,3,4],
    [4,3,2,1],
    [5,6,7,8],
    [8,7,6,5]
]

show_matriz_transposta(matriz)