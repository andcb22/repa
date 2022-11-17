# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import csv
import re

def write_dhcp_snooping_to_csv(filenames, output):
    headers=['switch','mac','ip','vlan','interface']
   #regex=(r'^(?P<MAC>\S+)\s+(?P<IP>[\d.]+)\s.+\s(?P<INT>[a-zA-Z0-9/]+\d+)$')
    regex=(r'^(?P<MAC>\S+)\s+(?P<IP>[\d.]+)\s.+\s+(?P<VLAN>\d+)\s+(?P<INT>[a-zA-Z0-9/]+\d+)$')
    with open(output,'w') as fw:
        writer = csv.writer(fw)
        writer.writerow(headers)
        for file in filenames:
#           print(file)
            with open(file,'r') as f:
                switchname=file.split('_')[0]
                for line in f:
#                   print(line)
                    match=re.search(regex,line)
                    if match:
#print(match.group('INT'))
#                       print(match.group('IP'))
#                       print(match.group('VLAN'))
                        to_csv=(switchname,match.group('MAC'),match.group('IP'),match.group('VLAN'),match.group('INT'))
                        writer.writerow(to_csv)
    pass


if __name__ == "__main__":
    filenames=['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']
    output='out.csv'
    write_dhcp_snooping_to_csv(filenames, output)

