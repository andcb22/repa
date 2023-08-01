# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.
В файле output первой строкой должны быть заголовки столбцов,
такие же как в файле source_log.

Для части пользователей запись только одна и тогда в итоговый файл надо записать
только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_str_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.
Вторая функция convert_datetime_to_str делает обратную операцию - превращает
объект datetime в строку.

Функции convert_str_to_datetime и convert_datetime_to_str использовать не обязательно.

"""

import datetime
import re
import csv


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    

    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")
    
def write_last_log_to_csv(source_log, output):
    with open(source_log, 'r') as fw:
        reader = csv.reader(fw)
#        print(reader)
        headers=next(reader)
        print('Headers are - ',headers)
        print()
        list_reader=list(reader)
        dict_user={}
        for row in list_reader:
            print(row)
            user=row[1]
            logtime=row[2]
            username=row[0]
            print()
            print('user - ',user,'logged at -',logtime,'set name - ',username)
            if not dict_user.get(user):
                print('got new user   :', user)
                print('set username  :', username)
                print('at time :',logtime)
                dict_user[user]=[username,logtime]
            else:
                print('was user ', user, 'username ',dict_user[user][0],'at  ',dict_user[user][1])
                print('time in dict',convert_str_to_datetime(dict_user[user][1]))
                print('time in file',convert_str_to_datetime(logtime))
                if convert_str_to_datetime(dict_user[user][1]) < convert_str_to_datetime(logtime) :
                    print('next this user in file is newer!')
                    dict_user[user]=[username,logtime]
    print(headers)
    for key in dict_user.keys():
        print(key)
                    
    return(dict_user)






if __name__ == "__main__":
    source_log='mail_log.csv'
    output='out.csv'
    out_dict=write_last_log_to_csv(source_log, output)
    
    
    
