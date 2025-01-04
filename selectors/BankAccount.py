name = "BankAccount"

from my_study_projects_2.models import BankAccount
from decimal import Decimal, DecimalException

class BankAccountSelector:
    """Класс для работы с таблицей Банковские счета клиентов ('BankAccounts')"""
    @staticmethod
    def add_new_account():
        """Метод для добавления нового счета в таблицу"""
        try:
            money = Decimal(input("Введите сумму на счете и нажмите Enter: "))
            BankAccount.create(money=money)
            print('Платежный счет успешно создан')
        except DecimalException:
            print('Некорректное значение для суммы на счете')

    @staticmethod
    def check_money_from_acc(acc_id: int):
        """Метод возвращающий сумму денег на счету, принимает аргумент acc_id - id банковского счета"""
        query = BankAccount.select(BankAccount.money).where(BankAccount.account_id == acc_id)
        result = query.dicts().execute()
        return [money['money'] for money in result][0]

    @staticmethod
    def check_id_in_table(acc_id: int) -> bool:
        """Метод проверки наличия банковского счета, принимает аргумент acc_id - id банковского счета"""
        request = BankAccount.select(BankAccount.account_id)
        result = request.dicts().execute()
        return acc_id in [id_acc['account_id'] for id_acc in result]

    @staticmethod
    def change_money(cust_id: int, amount: Decimal, incr:bool = True):
        """Метод изменения суммы на счету пользователя.
        Принимает целочисленный аргумент cust_id - номер счета пользователя,
        Decimal-аргумент amount - сумма для изменения,
        булевый аргумент incr, по умолчанию со значением True - увеличить количество денег,
         если принимает значение False - уменьшить количество денег"""
        query1 = BankAccount.select(BankAccount.money).where(BankAccount.account_id == cust_id)
        result1 = query1.dicts().execute()
        current_money = [money['money'] for money in result1][0]
        changed_money = current_money + amount if incr else current_money - amount
        if changed_money < 0:
            raise ValueError('Недостаточно средств для списания')
        query2 = BankAccount.update(money=changed_money).where(BankAccount.account_id == cust_id)
        query2.execute()
        print('Операция прошла успешно')

    @staticmethod
    def del_bank_acc(acc_id: int):
        """Метод для удаления банковского счета из таблицы, принимает аргумент acc_id - id банковского счета"""
        if acc_id == 1:
            raise ValueError('Нельзя удалить счет магазина')
        elif acc_id == 5:
            raise ValueError('Нельзя удалить счет банка-кредитора')
        elif not BankAccountSelector.check_id_in_table(acc_id):
            raise ValueError('Счет с таким id отсутствует')
        else:
            query = BankAccount.delete().where(BankAccount.account_id == acc_id)
            query.execute()
            print('Счет успешно удален')

