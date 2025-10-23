with open('.input', 'r', encoding = 'utf-8') as input_txt:
    input_list = input_txt.readlines()

left = []
right = []

print(len(input_list))

for item in input_list:
    if item == '':
        continue
    item = item.replace('\n', '').split('   ')
    left.append(int(item[0]))
    right.append(int(item[1]))

left.sort()
right.sort()

difference = 0

for i, item in enumerate(left):
    cD = item - right[i]
    if cD <= 0:
        cD *= -1
    difference += cD

print(difference)