text = input("Enter your text: ")
columns = int(input("Enter the number of columns: "))

text = text.replace(" ", "")

rows = -(-len(text) // columns)

matrix = [[' ' for _ in range(columns)] for _ in range(rows)]

index = 0

for j in range(columns):
    for i in range(rows):
        if index < len(text):
            matrix[i][j] = text[index]
            index += 1

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()

for row in matrix:
    print(''.join(row), end=' ')
