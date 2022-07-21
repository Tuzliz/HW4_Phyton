# 3- Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]
# Простые множители положит числа  - это простые числа, которые делят это число нацело без остатка
def num_biger_then_zero(text):

    int_num = True
    while int_num:
        n = input(f"{text}")
        if n.isdigit():
            n = int(n)
            if n <= 0:
                print("Введите число > 0")
            else:
                int_num = False
        else :
            print("Не число, попробуйте еще раз")
    return n
n = num_biger_then_zero("Введите натуральное число n : ") 

def get_prime_factors(n):
    my_lst =[] # список делителей
    i = 2 # чтобы число делилось на делитель нацело(если нет остатка - все ок, если есть остаток- увеличиваем делитель на единицу)
    while(i <= n):
        if(n % i) ==0:
            my_lst.append(i) # добавляем в список, если делится без остатка
            n = n / i #результат от деления записан в число(продолжаем делить новое число)
        else:
            i = i + 1    
    return my_lst        
print(get_prime_factors(n))  
# 180 : 2 = 90 - записали в список 
# 90 : 2 = 45 - записали в список 
# 45 : 3 = 15 (увеличили делитель: i = i + 1)
# 13 : 3 = 5 (записали в список)
# 5 : 5 = 1 (увеличили делитель до следующего простого множителя)