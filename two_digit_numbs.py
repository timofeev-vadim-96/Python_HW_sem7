# Доп.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности 
# оставшихся чисел в одну строчку через пробел.

def two_digit_numbs(input_list):
    two_digit_list = list(filter(lambda x: 10<=abs(x)<100,input_list))
    return two_digit_list

basic_list = [1,45,7,34,2,56,9, 10, 100, -99]
print(basic_list)
print(two_digit_numbs(basic_list))