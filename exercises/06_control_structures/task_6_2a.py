# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip=input('Введите IP-адрес в формате 10.0.1.1 :')

ip_list = ip.split('.')
a_correct=True

if not len(ip_list) == 4:
    a_correct=False
if a_correct:
    if not ip_list[0].isdigit():
        a_correct=False
    if not ip_list[1].isdigit():
        a_correct=False
    if not ip_list[2].isdigit():
        a_correct=False
    if not ip_list[3].isdigit():
        a_correct=False
if a_correct:
    if not (int(ip_list[0]) >= 0 and int(ip_list[0]) <= 255):
        a_correct=False
    if not (int(ip_list[1]) >= 0 and int(ip_list[1]) <= 255):
        a_correct=False
    if not (int(ip_list[2]) >= 0 and  int(ip_list[2]) <= 255):
        a_correct=False
    if not (int(ip_list[3]) >= 0 and  int(ip_list[3]) <= 255):
        a_correct=False

if a_correct:
    if ip == '0.0.0.0':
        print('unassigned')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif int(ip_list[0]) in range(1, 223):
        print('unicast')
    elif int(ip_list[0]) in range(224, 239):
        print('multicast')
    else:
        print('unused')
else:
    print('Неправильный IP-адрес')
