import csv


with open('products.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    answer = list(reader)

    answer[0].append('promocode')
    for i in range(1, len(answer)):
        month = answer[i][2][3:5]
        letters = answer[i][1][-3:-1]
        code = answer[i][1][:2] + answer[i][2][:2] + letters[::-1] + month[::-1]
        answer[i].append(code)

with open('products_promo.csv', 'w', encoding='utf-8-sig', newline='') as file:
    write = csv.writer(file, delimiter=';')
    write.writerows(answer)
    