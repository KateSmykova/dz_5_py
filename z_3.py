p = input("Введите текст: ")

def make_short (text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def make_long(text):
    num = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            num += text[i]
        else:
            res = res + text[i] * int(num)
            num = ''
    return res


print(f"Текст после сжатия: {make_short(p)}")
print(f"Текст после восстановления данных: {make_long(make_short(p))}")