# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
net=input('Введите сеть в формате: 10.1.1.0/24 :')
#net="10.0.1.1/24"
#0b1010 00000001 00000001 00000000
ip=net.split('/')[0].split('.')
mask=net.split('/')[1]
bin_mask='1'*int(mask)+'0'*(32-int(mask))
#print(ip)

bin_ip=str(bin(int(ip[0])*2**24+int(ip[1])*2**16+int(ip[2])*2**8+int(ip[3])))[2:]
bin_ip='0'*(32-len(bin_ip))+bin_ip
bin_ip_net=bin_ip[:-(32-int(mask))]+'0'*(32-int(mask))
ip_net=str(int(bin_ip_net[0:8],base=2))+'.'+str(int(bin_ip_net[8:16],base=2))+'.'+str(int(bin_ip_net[16:24],base=2))+'.'+str(int(bin_ip_net[24:32],base=2))

network_template='''
Network:
{:10}{:10}{:10}{:10}
{:8}  {:8}  {:8}  {:8}
'''
mask_template='''
Mask:
/{}
{:<10}{:<10}{:<10}{:<10}
{}  {}  {}  {}
'''
print(network_template.format(str(int(bin_ip_net[0:8],base=2)),str(int(bin_ip_net[8:16],base=2)),
str(int(bin_ip_net[16:24],base=2)),str(int(bin_ip_net[24:32],base=2)),
bin_ip_net[0:8],
bin_ip_net[8:16],
bin_ip_net[16:24],
bin_ip_net[24:32]))

print(mask_template.format(mask,int(bin_mask[0:8],base=2),int(bin_mask[8:16],base=2),int(bin_mask[16:24],base=2),int(bin_mask[24:32],base=2),bin_mask[:8],bin_mask[8:16],bin_mask[16:24],bin_mask[24:32]))