# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно,
чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии,
но и удалять "дублирующиеся" соединения (их лучше всего видно на схеме, которую
генерирует функция draw_topology из файла draw_network_graph.py).
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Из-за того что один и тот же линк описывается дважды, на схеме будут лишние соединения.
Задача оставить только один из этих линков в итоговом словаре, не важно какой.

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии
с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть "дублирующихся" линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
import re
import yaml
from pprint import pprint
from draw_network_graph import draw_topology

def transform_topology(yaml_file):
    print('In func!')
    with open(yaml_file,'r') as fr:
        topology_data=yaml.safe_load(fr)
    pprint(topology_data)
    main_dict={}
    for sw_key in  topology_data.keys():
        print(sw_key)
        for ln_key in topology_data[sw_key]:
            print(ln_key)
            link=topology_data[sw_key][ln_key]
            print('last element - ')
            #print(link)
            for key in link.keys():
                link_tuple=(key,link[key])
                source_tuple=(sw_key,ln_key)
            print(source_tuple)
            print(link_tuple)
            main_dict[source_tuple]=link_tuple
            
    dup_keys=list(main_dict.keys())
    dup_values=list(main_dict.values())
    for kk in dup_keys:
        if kk in dup_values:
            if main_dict.get(kk) in dup_keys:
                value=main_dict[kk]
                del(main_dict[value])
             
         
        
   
    print(main_dict)
   
    
    return(main_dict)   
    
    
    pass
    
if __name__ == "__main__":
    yaml_file='topology.yaml'
    topology=transform_topology(yaml_file)
    #draw_topology(topology)
    
    
    
