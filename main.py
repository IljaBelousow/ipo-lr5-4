kolvo = int(input("введите количество слов"))
a = []
b = ""
for i in range(kolvo):#выводит слова и доабвчялет в a[]
    slovo = str(input("ваше слово "))
    a += [slovo]
string = [x[0] for x in a]#первая буква добавялется в b""
for i in string:
    b += i
print(b)
