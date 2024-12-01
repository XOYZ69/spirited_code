with open('.input', 'r', encoding = 'utf-8') as input_txt:
    input_list = input_txt.readlines()

left = []
right = []

for item in input_list:
    if item == '':
        continue
    item = item.replace('\n', '').split('   ')
    left.append(int(item[0]))
    right.append(int(item[1]))

left.sort()
right.sort()

mulitplie = 0

for i, item in enumerate(left):
    counter = 0
    for x in right:
        if x == item:
            counter += 1
    mulitplie += item * counter
print(mulitplie)