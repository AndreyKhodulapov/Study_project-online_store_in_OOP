NAME = """Модуль для работы с функционалом магазина и обработки исключений"""

try:
    from peewee import *
    from BankAccount import BankAccountSelector
    from GoodType import GoodTypeSelector
    from User import UserSelector
    from Goods import GoodsSelector
    from ShoppingCard import ShoppingCardSelector
    from Orders import OrdersSelector


    """Добавить банковский аккаунт для оплаты"""
    # BankAccountSelector.add_new_account()

    """Удалить банковский аккаунт для оплаты"""
    # BankAccountSelector.del_bank_acc(1)

    """Добавить новую категорию товаров"""
    # GoodTypeSelector.add_new_type()

    """Показать все категории товаров"""
    # GoodTypeSelector.get_all_rows_type()

    """Вывести одну категорию товаров"""
    # GoodTypeSelector.get_row_type()

    """Показать товары в выбранной категории"""
    # GoodTypeSelector.see_goods_in_type()

    """Удалить категорию товаров"""
    # GoodTypeSelector.del_type()

    """Добавление нового профиля покупателя"""
    # UserSelector.add_new_user()

    """Авторизация покупателя"""
    # print(UserSelector.log_in())

    """Изменение профиля покупателя"""
    # change_user_info(parameter='password')

    """Удаление профиля покупателя"""
    # UserSelector.del_user()

    """Добавить новую позицию в ассортимент магазина"""
    # GoodsSelector.add_new_position()

    """Посмотреть ассортимент магазина"""
    # GoodsSelector.see_all_positions()

    """Выполнить поиск по ассортименту"""
    # GoodsSelector.search()

    """Удалить товар из ассортимента"""
    # GoodsSelector.delete_goods()

    """Изменить характеристики товара"""
    # GoodsSelector.change_goods_char('color')

    """Добавить товар в корзину"""
    # ShoppingCardSelector.add_to_card(11, 1)

    """Посмотреть корзину покупок"""
    # ShoppingCardSelector.see_card()

    """Удаление товаров из корзины"""
    # ShoppingCardSelector.del_from_card()

    """Вывести стоимость корзины"""
    # print(ShoppingCardSelector.total_price())

    """Вывести количество товаров в козине"""
    # ShoppingCardSelector.total_amount()

    """Купить корзину"""
    # ShoppingCardSelector.buy_from_card()

    """Просмотр заказов в магазине"""
    # OrdersSelector.see_orders()

    """Просмотр выручки за день"""
    OrdersSelector.daily_profit()

except ValueError as v:
    print(v)
except ModuleNotFoundError as m:
    print('Модуль не найден', m)
except OperationalError:
    print('Нет доступа к базе данных')
except Exception as e:
    print('Возникла непредвиденная ошибка',type(e), e)