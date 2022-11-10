text = 'Мыабв постарались изложить материал таабвк, чтобы были понятны и сабвми алгоритмы.'

delet = "абв"
lst = [i for i in text.split() if delet not in i]
print(f'Вывод текста без "абв": {" ".join(lst)}')