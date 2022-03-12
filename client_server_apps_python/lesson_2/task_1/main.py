import csv
import re


def get_data():
    """
    Осуществляет перебор файлов с данными, их открытие и считывание данных
    """

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        file_open = open(f'info_{i}.txt')
        file_data = file_open.read()

        os_prod = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod.findall(file_data)[0].split()[2])

        os_name = re.compile(r'Windows\s\S*')
        os_name_list.append(os_name.findall(file_data)[0])

        os_code = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code.findall(file_data)[0].split()[2])

        os_type = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type.findall(file_data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    j = 1
    for i in range(0, 3):
        row_list = [j, os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(row_list)
        j += 1
    return main_data


def write_to_csv(return_file):
    """
    Получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл
    """

    main_data = get_data()
    with open(return_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            writer.writerow(row)


write_to_csv('csv_data.csv')
