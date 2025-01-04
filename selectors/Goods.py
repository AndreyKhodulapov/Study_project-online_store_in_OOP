name = "GoodsSelector"

from my_study_projects_2.models import Goods
from GoodType import GoodTypeSelector
from decimal import Decimal


class GoodsSelector:
    """Класс для работы с таблицей Товары ('goods')"""
    @staticmethod
    def add_new_position():
        """Метод для добавления новой позиции в таблицу"""
        good_name = input("Введите название товара и нажмите Enter: ")
        brand = input("Введите бренд или производителя и нажмите Enter: ")
        made_in = input("Введите страну производства и нажмите Enter: ")
        color = input("Введите цвет и нажмите Enter: ")
        size = input("Введите размер товара и нажмите Enter: ")
        keywords = input("""Введите ключевые слова (через пробел, без запятых) 
                для поиска товара и нажмите Enter: """)
        GoodTypeSelector.get_all_rows_type()
        good_type = int(input("Скопируйте цифровой код типа товара из перечня выше и нажмите Enter: "))
        amount = int(input("Введите количество товара и нажмите Enter: "))
        price = Decimal(input("Введите цену товара в формате ХХХХ.ХХ и нажмите Enter: "))
        Goods.create(good_name=good_name, brand=brand, made_in=made_in, color=color,
                     size=size, keywords=keywords, good_type=good_type, amount=amount, price=price)
        print('-------------')
        print('Позиция успешно внесена')

    @staticmethod
    def iterate_query_result(result):
        """Метод выводящий результаты поисковых запросов к таблице Товары
        принимает аргумент result - результат запроса к таблице"""
        for goods in result:
            print(f"Название: '{goods['good_name']}', артикул: {goods['good_id']}, цена: {goods['price']}")
            print(f"          Характеристики: производитель: {goods['brand']}, {goods['made_in']}")
            print(f"                        цвет: {goods['color']}, размер: {goods['size']}")
            print('                        ТОВАР В НАЛИЧИИ' if goods['amount'] > 0 else 'ТОВАР ОТСУТСТВУЕТ')

    @staticmethod
    def return_goods_by_id(goods_id: int):
        """Метод возвращает название товара по его артикулу.
        Принимает целочисленный аргумент goods_id - артикул"""
        query = Goods.select(Goods.good_name).where(Goods.good_id == goods_id)
        result = query.dicts().execute()
        for goods in result:
            return goods['good_name']

    @staticmethod
    def return_price_by_id(goods_id: int):
        """Метод возвращает цену товара по его артикулу.
        Принимает целочисленный аргумент goods_id - артикул"""
        query = Goods.select(Goods.price).where(Goods.good_id == goods_id)
        result = query.dicts().execute()
        for goods in result:
            return goods['price']

    @staticmethod
    def good_exists(good_id: int):
        """Метод, проверяющий наличие товара в таблице"""
        control_query = Goods.select().where(Goods.good_id == good_id)
        return len([goods for goods in control_query.dicts().execute()]) > 0


    @staticmethod
    def see_all_positions(sorting_by: str = 'id', desc=False):
        """Метод, выводящий перечень всех товаров в магазине с возможностью их сортировки.
        Принимает строковый аргумент sorting_by со значаниями:
        'id' - по умолчанию, сортировка по артикулу товара,
        'name' - сортировка по названию товара,
        'brand' - сортировка по фирме производителя,
        'country' - сортировка по стране производства,
        'type' - сортировка по типу товара
        'price' или любая друга строка - сортировка по цене;
        принимает булевый аргумент desc - для сортировки по убыванию"""
        if sorting_by == 'id':
            query = Goods.select().order_by(Goods.good_id.desc()) if desc else Goods.select().order_by(Goods.good_id)
        elif sorting_by == 'name':
            query = Goods.select().order_by(Goods.good_name.desc()) if desc else Goods.select().order_by(Goods.good_name)
        elif sorting_by == 'brand':
            query = Goods.select().order_by(Goods.brand)
        elif sorting_by == 'country':
            query = Goods.select().order_by(Goods.made_in)
        elif sorting_by == 'type':
            query = Goods.select().order_by(Goods.good_type)
        else:
            query = Goods.select().order_by(Goods.price.desc()) if desc else Goods.select().order_by(Goods.price)
        result = query.dicts().execute()
        GoodsSelector.iterate_query_result(result)

    @staticmethod
    def search():
        """Метод поиска товара в таблице"""
        question = input('Поиск товара, введите запрос и нажмите Enter: ')
        query = (Goods.select().where(Goods.good_name == question).
                 union(Goods.select().where(Goods.keywords == question)).
                 union(Goods.select().where(Goods.color == question)))
        result = query.dicts().execute()
        GoodsSelector.iterate_query_result(result)

    @staticmethod
    def change_goods_char(parameter: str):
        """Метод для изменения информации о товаре
                Принимает строковый аргумент parameter,
                который может принимать следующие значения:
                'name' - для изменения названия,
                'brand' - для изменения производителя,
                'country' - для изменения страны производства
                'color' - для изменения цвета
                'size' - для изменения размера
                'keywords' - для изменения ключевых слов
                'price' - для изменения цены"""
        print(f"Найдите товар для изменения характеристики '{parameter}' через запрос")
        GoodsSelector.search()
        print('------------------')
        id_for_change = int(input('Введите артикул товара для изменения характеристик и нажмите Enter: '))
        if not GoodsSelector.good_exists(id_for_change):
            raise ValueError('Товар с указанным артикулом отсутствует в ассортименте магазина')
        if parameter == 'name':
            new_name = input('Введите новое нaзвание товара и нажмите Enter: ')
            query = Goods.update(good_name=new_name).where(Goods.good_id == id_for_change)
        elif parameter == 'brand':
            new_brand = input('Введите новое нaзвание бренда и нажмите Enter: ')
            query = Goods.update(brand=new_brand).where(Goods.good_id == id_for_change)
        elif parameter == 'country':
            new_country = input('Введите новое нaзвание страны-производителя и нажмите Enter: ')
            query = Goods.update(made_in=new_country).where(Goods.good_id == id_for_change)
        elif parameter == 'color':
            new_color = input('Введите новый цвет и нажмите Enter: ')
            query = Goods.update(color=new_color).where(Goods.good_id == id_for_change)
        elif parameter == 'size':
            new_size = input('Введите новый размер и нажмите Enter: ')
            query = Goods.update(size=new_size).where(Goods.good_id == id_for_change)
        elif parameter == 'keywords':
            new_keywords = input('Введите новые ключевые слова и нажмите Enter: ')
            query = Goods.update(keywords=new_keywords).where(Goods.good_id == id_for_change)
        elif parameter == 'price':
            new_price = input('Введите новую цену и нажмите Enter: ')
            query = Goods.update(price=new_price).where(Goods.good_id == id_for_change)
        else:
            raise ValueError('Такая характеристика товара отсутствует')
        query.execute()
        print(f"Операция по изменению характеристики '{parameter}' у товара с артикулом '{id_for_change}' УСПЕШНО ЗАВЕРШЕНА")

    @staticmethod
    def change_goods_amount(goods_id: int, amount: int = 1, incr: bool = True):
        """Метод изменения количества товаров в магазине.
        Принимает целочисленный аргумент goods_id - артикул товара,
        целочисленный аргумент amount - количество для изменения, по умолчанию = 1
        булевый аргумент incr, по умолчанию со значением True - увеличить количество товара,
         если принимает значение False - уменьшить количество товара"""
        query1 = Goods.select(Goods.amount).where(Goods.good_id == goods_id)
        result1 = query1.dicts().execute()
        current_amount = [amount['amount'] for amount in result1][0]
        changed_amount = current_amount + amount if incr else current_amount - amount
        if changed_amount < 0:
            raise ValueError('Недостаточно товара для покупки')
        query2 = Goods.update(amount=changed_amount).where(Goods.good_id == goods_id)
        query2.execute()
        print(f'Операция по изменению количества товара с артикулом {goods_id} прошла успешно')

    @staticmethod
    def delete_goods():
        print('Найдите товар для удаления через запрос')
        GoodsSelector.search()
        print('------------------')
        id_for_del = int(input('Введите артикул товара для удаления и нажмите Enter: '))
        if not GoodsSelector.good_exists(id_for_del):
            raise ValueError('Товар с указанным артикулом отсутствует в ассортименте магазина')
        query = Goods.delete().where(Goods.good_id == id_for_del)
        query.execute()
        print(f"Товар с артикулом {id_for_del} успешно удален")
