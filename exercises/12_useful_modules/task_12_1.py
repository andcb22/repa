# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
#import ipaddress
import subprocess

ip_list=['8.8.8.8','8.8.4.4','a']

def ping_ip_addresses(ip_list):
    ip_list_good=[]
    ip_list_bad=[]
    for ip in ip_list:
        reply=subprocess.run(['ping','-c','3',ip])
        if reply.returncode == 0:
            ip_list_good.append(ip)
        else:
            ip_list_bad.append(ip)
    pass
    return(ip_list_good,ip_list_bad)

if __name__ == "__main__":
    result=ping_ip_addresses(ip_list)
    print(type(result))
    print(result)

