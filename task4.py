# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.



from importlib.resources import path

file = open('Text.txt' , "w",encoding='utf-8') #записыаем и создаем файл
file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")
file.close()

path = 'Text.txt'
file = open('Text.txt' , "r",encoding='utf-8') #считываем из файла строку
data = file.read()
file.close()
def delete_num(path:str): # Функия удаления слов с цифрой в строке
    list_of_words = data.split() # разбиваем строку на отдельные символы через запятую
    my_list =[] # создвем новый список для записи результата выполнения функкции
    for i in list_of_words:
        delete_word = False
        for num in i:
            if num.isdigit(): #проверяем есть ли число
                delete_word = True
                break
        else:
            delete_word == False
            my_list.append(i)       #добавляем в список только слова     
    return my_list       
delete_num(path) # получаем резултат работы функции (наш новый список)
result_string = "" # преобразуем в строку
for i in delete_num(path):
    result_string += str(i)+ ' ' # добавляем пробелы
print(f'Результат: {result_string}')    