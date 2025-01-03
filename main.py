NAME = """Модуль для работы с функционалом магазина и обработки исключений"""

try:
    from my_study_projects_2.selectors.BankAccount import BankAccountSelector
    # from my_study_projects_2.selectors.GoodType import GoodTypeSelector
    # from my_study_projects_2.selectors.User import UserSelector
    # from my_study_projects_2.selectors.Goods import GoodsSelector
    # from my_study_projects_2.selectors.ShoppingCard import ShoppingCardSelector
    from my_study_projects_2.selectors.Orders import OrdersSelector
except ModuleNotFoundError as m:
    print('Модуль не найден', m)

try:
    """Добавить банковский аккаунт для оплаты"""
    # BankAccountSelector.add_new_account()

    """Удалить банковский аккаунт для оплаты"""
    # BankAccountSelector.del_bank_acc(1)

    # GoodTypeSelector.add_new_type()
    # GoodTypeSelector.get_all_rows_type()
    # GoodTypeSelector.get_row_type()
    # GoodTypeSelector.see_goods_in_type()
    # GoodTypeSelector.del_type()

    # UserSelector.add_new_user()
    # print(UserSelector.log_in())
    # change_user_info(parameter='password')
    # UserSelector.del_user()

    """Добавить новую позицию в ассортимент магазина"""
    # GoodsSelector.add_new_position()

    """Посмотреть ассортимент магазина"""
    # GoodsSelector.see_all_positions()

    """Выполнить поиск по ассортименту"""
    # GoodsSelector.search()
    #
    """Удалить товар из ассортимента"""
    # GoodsSelector.delete_goods()

    """Изменить характеристики товара"""
    # GoodsSelector.change_goods_char('color')

    """Добавить товар в корзину"""
    # ShoppingCardSelector.add_to_card(4, 1)
    # ShoppingCardSelector.see_card()
    # ShoppingCardSelector.del_from_card()
    # print(ShoppingCardSelector.total_price())
    # ShoppingCardSelector.total_amount()
    # ShoppingCardSelector.buy_from_card()

    """Просмотр заказов в магазине"""
    # OrdersSelector.see_orders()

    """Просмотр выручки за день"""
    # OrdersSelector.daily_profit()

except ValueError as v:
    print(v)
except Exception as e:
    print('Возникла непредвиденная ошибка',type(e), e)