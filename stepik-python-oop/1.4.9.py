lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for field in data:
            self.lst_data.append(dict(zip(self.FIELDS, field.split())))

    def select(self, a, b):
        return self.lst_data[a: b + 1]


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
