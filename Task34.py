text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
text = text.split()
new_text = []
print(text)
for i in range (0, len(text)):
    n = text[i].count('а')
    new_text.append(n)

counter = 0
for i in range (0, len(new_text) - 1):
    if new_text[i] == new_text[i+1]:
        counter += 1
    else:
        counter += 0

if counter == len(text) - 1:
    print('Парам пам-пам')
else:
    print('Пам парам')



