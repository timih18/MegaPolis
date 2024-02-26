import csv

mn = set()
with open('products.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    answer = list(reader)
    answer.pop(0)

    for sp in answer:
        if sp[0] not in mn:
            mn.add(sp[0])

category = input()
while category != 'молоко':
    if category in mn:
        names = []
        cnts = []
        for sp in answer:
            if sp[0] == category:
                if sp[1] in names:
                    cnts[names.index(sp[1])] += int(sp[4][:-2])
                else:
                    names.append(sp[1])
                    cnts.append(int(sp[4][:-2]))
        cnt = int(min(cnts))
        product = names[cnts.index(cnt)]
        print(f'В категории: {category} товар: {product} был куплен {cnt} раз')
    else:
        print('Такой категории не существует в нашей БД')
    category = input()
