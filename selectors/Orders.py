name = "OrdersSelector"

from my_study_projects_2.models import Orders

class OrdersSelector:
    """Класс для работы с таблицей Заказы ('orders')"""
    @staticmethod
    def see_orders():
        """Метод, выводящий содержимое таблицы"""
        query = Orders.select()
        result = query.dicts().execute()
        print('№____дата______время_______стоимость__id покупателя')
        for row in result:
            print(row['pur_id'], row['purchase_data'], row['total_pur_price'], '  ', row['customer'])

    @staticmethod
    def daily_profit():
        """Метод, выводящий выручку за день"""
        date = input("Введите необходимую дату в формате ГГГГ-ММ-ДД и нажмите Enter: ")
        query = Orders.select(Orders.total_pur_price).where(Orders.purchase_data.startswith(date))
        result = sum([value['total_pur_price'] for value in query.dicts().execute()])
        print(f"Выручка за {date} составила {result} RUB")

