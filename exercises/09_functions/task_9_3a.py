# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
  access_dict={}
  trunk_dict={}
  with (open(config_filename,'r')) as f:
      for line in f:
        line=line.rstrip()
        if line and line.rstrip() != '!':

          if line.startswith('interface'):
            intf=line.split(' ')[-1]

          if line.startswith(' switchport mode access'):
              vlan=1
              access_dict[intf]=vlan
          if line.startswith(' switchport access vlan'):
              vlan = int(line.lstrip().split(' ')[3])
              access_dict[intf]=vlan

          if line.startswith(' switchport trunk allowed'):
            vlans = line.lstrip().split(' ')[4].split(',')
            vlans_int=[]
            for item in vlans:
                vlans_int.append(int(item))
            trunk_dict[intf]=vlans_int

  pass
  return (access_dict,trunk_dict)

print(get_int_vlan_map('config_sw2.txt'))

