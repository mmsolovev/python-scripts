import yaml


data_dict = {'items': ['хлеб', 'молоко', 'колбаса'],
             'quantity': 4,
             'price': {'хлеб': '50.00\u00a3',
                       'молоко': '100.00\u00a3',
                       'колбаса': '200.00\u00a3',
                       },
             }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data_dict, f_in, allow_unicode=True, default_flow_style=False)

with open('file.yaml', 'r', encoding='utf-8') as f_out:
    out_dict = yaml.load(f_out, Loader=yaml.SafeLoader)


print(out_dict == data_dict)
