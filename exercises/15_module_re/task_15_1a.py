# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

filename='config_r1.txt'

def get_ip_from_cfg(filename):
#   ip_list=[]
   ip_dict={}
   regex=(r' ip address (?P<IP>\S+) (?P<MASK>\S+)')
   with open(filename) as f:
      for line in f:
         if line.startswith('interface'):
            intf=re.search(r'interface (\S+)',line).group(1)
         match = re.search(regex,line)
         if match:
#            ip_list.append((match.group('IP'),match.group('MASK')))
            ip_dict[intf]=(match.group('IP'),match.group('MASK'))
   return(ip_dict)

result = get_ip_from_cfg(filename)
if result:
   print(result)
else:
   print('...nothing...')

