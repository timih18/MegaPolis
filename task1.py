import csv


with open('products.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    answer = list(reader)

    answer[0].append('total')
    for i in range(1, len(answer)):
        answer[i].append(str(float(answer[i][4])*float(answer[i][3])))

with open('products_new.csv', 'w', encoding='utf-8-sig', newline='') as file:
    write = csv.writer(file, delimiter=';')
    write.writerows(answer)

summary = 0
for sp in answer:
    if sp[0] == 'Закуски':
        summary += float(sp[5])
print(int(summary))
