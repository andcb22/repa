# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress

#ip_list=['10.1.1.1']
#ip_list=['10.0.0.1','10.1.1.1-10']
#ip_list=['172.21.41.128-172.21.41.132']
#ip_list=['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
ip_list=["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]



def convert_ranges_to_ip_list(ip_list):
    ip_list_out=[]
    for ip in ip_list:
        
        if len(ip.split('.')) == 4:
            if ip.split('.')[3].isdigit():
                #alone ip
                ip_list_out.append(str(ipaddress.ip_address(ip)))
#                print('alone digit!')
            else:
                for i in range(int(ip.split('.')[3].split('-')[0]),int(ip.split('.')[3].split('-')[1])+1):
                  ipi=(ip.split('.')[0]+'.'+ip.split('.')[1]+'.'+ip.split('.')[2]+'.'+str(i))  
                  ip_list_out.append(ipi)
#                  print(i)
        elif len(ip.split('.')) == 7:
            net=ip.split('.')[0]+'.'+ip.split('.')[1]+'.'+ip.split('.')[2]
            diap=ip.split('.')[3]
            ip1=int(diap.split('-')[0])
            ip2=int(ip.split('.')[6])
            for ips in range(ip1,ip2+1):
                ipi=net+'.'+str(ips)
                ip_list_out.append(ipi)
            
    return(ip_list_out)




if __name__ == "__main__":
    print(convert_ranges_to_ip_list(ip_list))

