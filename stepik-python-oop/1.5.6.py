class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def _get_str_data(self):
        return ' '.join(map(str, self.data))

    def show_table(self):
        if self.is_show:
            print(self._get_str_data())
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print(f'Графическое отображение данных: {self._get_str_data()}')
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print(f'Столбчатая диаграмма: {self._get_str_data()}')
        else:
            print('Отображение данных закрыто')

    def set_show(self, show):
        self.is_show = show


data_graph = 'qwerty'
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
