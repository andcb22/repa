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
#ip_reachable=['1.1.1.1','1.1.1.2']
ip_reachable=['1.1.1.1','1.1.1.2','1.2.2.2','1.1.5.5']
def print_ip_table(ip_reachable,ip_unreachable):
    list_ip_2=[]
    headers=('Reachable','Unreachable')

    if len(ip_unreachable) >= len(ip_reachable):
        for length in range(len(ip_unreachable)):
            if length >= len(ip_reachable):
                list_ip_2.append(['',ip_unreachable[length]])
            else:
                list_ip_2.append([ip_reachable[length],ip_unreachable[length]])
#            print(list_ip_2)
    else:
        for length in range(len(ip_reachable)):
            if length >= len(ip_unreachable):
                list_ip_2.append(['',ip_reachable[length]])
            else:
                list_ip_2.append([ip_reachable[length],ip_unreachable[length]])
#            print(list_ip_2)





    print(tabulate(list_ip_2,headers=headers))

if __name__ == "__main__":
    print_ip_table(ip_reachable,ip_unreachable)

