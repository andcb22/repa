# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate
ip_unreachable=['1.2.3.a','1.2.3.b','1.22.3.c']
ip_reachable=['1.1.1.1','1.1.1.2']
def print_ip_table(ip_reachable,ip_unreachable):
    headers=('Reachable','Unreachable')
    list_ip_2=[]

    if len(ip_unreachable) >= len(ip_reachable):
        print('select len unreachable - ' + str(len(ip_unreachable)))
        length = len(ip_unreachable)
    else:
        length = len(ip_reachable)

    print(length)
    
    while length:
        if ip_unreachable[length]:
            a=ip_unreachable[length]
        else:
            a=''
        if ip_reachable[length]:
            b=ip_reachable[length]
        else:
            b=''
        length -= 1
        list_ip_2.append([a,b])
    print(list_ip_2)






    print(tabulate(zip(ip_reachable,ip_unreachable),headers=headers))

if __name__ == "__main__":
    print_ip_table(ip_reachable,ip_unreachable)

