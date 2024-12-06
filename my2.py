n = int(input())
students = []
for _ in range(n):
    m = int(input())
    temp = []
    for _ in range(m):
        surname, mark = input().split()
        temp.append((surname, int(mark)))
    students.append(temp)

result = all(map(lambda x: any(map(lambda y: y[1] == 5, x)), students))
print('YES' if result else 'NO')