# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
prefix=ospf_route.strip().split()[0]
ad=ospf_route.strip().split()[1]
nh=ospf_route.strip().split()[3]
lup=ospf_route.strip().split()[4]
oi=ospf_route.strip().split()[5]
print("{:22}{:22}".format('Prefix', prefix))
print("{:22}{:22}".format('AD/Metric', ad[1:-1]))
print("{:22}{:22}".format('Next-Hop', nh[:-1]))
print("{:22}{:22}".format('Last update', lup[:-1]))
print("{:22}{:22}".format('Outbound Interface', oi))