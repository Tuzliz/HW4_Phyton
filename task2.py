#2- Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

#Вариант без множества:

numbers_lst = [20, 20, 30, 30, 40]
print(f'Исходный заданный список:{numbers_lst}')
def get_unique_numbers(numbers_lst):
    unique_lst = []
    for i in numbers_lst:
        if i not in unique_lst: #если нет числа в уникальном списке, то его нужно добавлять в список
            unique_lst.append(i)
    return unique_lst
print(get_unique_numbers(f'Полученный уникальный список: {numbers_lst}'))

#numbers = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6] #  Есть список чисел numbers.
# Множество SET:
#def get_unique_numbers(numbers): #  Передаем его в функцию get_unique_numbers.
    #list_of_unique_numbers = [] ## Внутри этой функции создается пустой список, который в итоге будет включать все уникальные числа.
    #unique_numbers = set(numbers) #осле этого используется set для получения уникальных чисел из списка numbers.
    #print(set(numbers))

    #for number in unique_numbers:
        #list_of_unique_numbers.append(number) #записываеи уникальные числа в список

    #return list_of_unique_numbers

#print(get_unique_numbers(numbers))


