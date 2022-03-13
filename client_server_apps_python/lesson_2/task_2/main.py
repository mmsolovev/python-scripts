import json


def write_order_to_json(item, quantity, price, buyer, date):
    """
    Запись данных в виде словаря в файл orders.json
    """

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        file_data = json.load(f_out)
        
    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = file_data['orders']
        order_data = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_data)
        json.dump(file_data, f_in, indent=4, ensure_ascii=False)


write_order_to_json('хлеб', '2', '50.00', 'Соловьев', '12.12.2012')
