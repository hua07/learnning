y_pred = {}
aid = {}
for i in 'MTAV':
    for j in range(6):
        aid[j] = []
    y_pred = aid
print(y_pred)


for m in 'MTAV':
    for j in range(6):
        print(m, j)
        y_pred[m][j].append([[1], [2]])
print(y_pred)