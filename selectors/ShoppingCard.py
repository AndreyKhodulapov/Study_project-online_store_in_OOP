name = "ShoppingCardSelector"

from my_study_projects_2.models import ShoppingCard, Orders
from decimal import Decimal
from Goods import GoodsSelector
from BankAccount import BankAccountSelector
from User import UserSelector


class ShoppingCardSelector:
    """Класс для работы с таблицей Корзина покупок ('shoppingcard')"""
    @staticmethod
    def add_to_card(goods_id: int, amount: int = 1):
        """Метод для добавления товаров в корзину.
        Принимает два целочисленных аргумента:
        'goods_id' - артикул товара,
        'amount' - необходимое количество товара"""
        if not GoodsSelector.good_exists(goods_id):
            raise ValueError('Товар отсутствует в ассортименте магазина')
        GoodsSelector.change_goods_amount(goods_id=goods_id, amount=amount, incr=False)
        ShoppingCard.create(goods_id=goods_id, amount=amount)
        print('Товар успешно добавлен в корзину')

    @staticmethod
    def see_card():
        """Метод для просмотра содержимого корзины"""
        card_query = ShoppingCard.select()
        card_query_result = card_query.dicts().execute()
        if len([goods for goods in card_query_result]) == 0:
            print('Корзина пуста')
        else:
            card_query = ShoppingCard.select()
            card_query_result = card_query.dicts().execute()
            print('Товары в корзине:')
            print('Название товара_______________________цена___количество в корзине')
            for good_id in card_query_result:
                print(f"'{GoodsSelector.return_goods_by_id(good_id['goods'])}'__{GoodsSelector.return_price_by_id(good_id['goods'])} RUB__{good_id['amount']}")

    @staticmethod
    def del_from_card():
        """Метод для возвращения товаров из корзины на склад"""
        card_query = ShoppingCard.select()
        card_query_result = card_query.dicts().execute()
        for good_id in card_query_result:
            GoodsSelector.change_goods_amount(goods_id=good_id['goods'], amount=good_id['amount'], incr=True)
        query = ShoppingCard.delete()
        query.execute()
        print('Корзина освобождена!')

    @staticmethod
    def total_price():
        """Метод, возвращающий итоговую стоимоть корзины"""
        card_query = ShoppingCard.select()
        card_query_result = card_query.dicts().execute()
        return sum(
            [GoodsSelector.return_price_by_id(good_id['goods']) * good_id['amount'] for good_id in card_query_result])

    @staticmethod
    def total_amount():
        """Метод, показывающий количество единиц товара в корзине"""
        card_query = ShoppingCard.select()
        card_query_result = card_query.dicts().execute()
        items = sum([good_id['amount'] for good_id in card_query_result])
        positions = len(set([good_id['goods'] for good_id in card_query_result]))
        print(f"Количество позиций в корзине: {positions}")
        print(f"Количество единиц товаров в корзине: {items if items <= 10 else '10+'}")

    @staticmethod
    def buy_from_card():
        """Метод для покупки товаров из корзины"""
        print("Авторизуйтесь для покупки")
        customer = UserSelector.log_in()
        customer_id = customer['user_id']
        customer_money = customer['money']
        card_price = ShoppingCardSelector.total_price()
        BankAccountSelector.change_money(cust_id=customer_money, amount=Decimal(card_price), incr=False)
        BankAccountSelector.change_money(cust_id=1, amount=Decimal(card_price), incr=True)
        print('Оплата прошла успешно!')
        Orders.create(total_pur_price=card_price, customer=customer_id)
        query = ShoppingCard.delete()
        query.execute()
        print('Спасибо за покупку!')


