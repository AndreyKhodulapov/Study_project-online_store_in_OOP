name = "UserSelector"

from my_study_projects_2.models import User
from functools import reduce
from BankAccount import BankAccountSelector


class UserSelector:
    """Класс для работы с таблицей Пользователи ('Users')"""

    @staticmethod
    def check_password(password: str) -> bool:
        """Метод проверки пароля, вводимого пользователем, на надежность.
        Принимает один строковый аргумент - пароль"""
        return len(password) > 8 and len([sym for sym in password if sym.isdigit()]) > 0\
            and len([sym for sym in password if sym.isalpha()]) > 0\
            and len([sym for sym in password if not sym.isalpha() and not sym.isdigit()]) > 0\
            and len([sym for sym in password if sym.isalpha() and sym == sym.upper()]) > 0\
            and set([sym for sym in password if sym.isalpha()]).\
                issubset(set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    @staticmethod
    def hash_password(password) -> str:
        """Хэш-функция для сохранения паролей. Принимает один строковый аргумент - пароль"""
        transfiguration1 = [str((ord(sym))**3) for sym in password]
        transfiguration2 = map(lambda x: int(x[::-1]), transfiguration1)
        transfiguration3 = reduce(lambda x, y: x * y, transfiguration2)
        return str(transfiguration3)

    @staticmethod
    def add_new_user():
        """Метод для добавления нового пользователя в таблицу"""
        user_name = input("Введите Ваше имя и нажмите Enter: ")
        login = input("Придумайте и введите логин, после чего нажмите Enter: ")
        print("""Придумайте и введите пароль, состоящий не менее, чем из 8 из строчных и ЗАГЛАВНЫХ 
        букв английского алфавита, цифр и знаков препинания и нажмите Enter: """)
        password = input()
        if not UserSelector.check_password(password):
            raise ValueError('Регистрация прервана, придумайте корректный пароль')
        password_check = input('Повторите пароль и нажмите Enter: ')
        if not password == password_check:
            raise ValueError('Регистрация прервана, пароли не совпадают')
        for_pay = int(input('Введите данные для оплаты заказа: '))
        if not BankAccountSelector.check_id_in_table(for_pay):
            raise ValueError('Регистрация прервана, пароли не совпадают')
        User.create(name=user_name, login=login, password=UserSelector.hash_password(password), money_id=for_pay)
        print('------------------')
        print('Новый пользователь успешно внесен в таблицу')

    @staticmethod
    def log_in():
        """Метод авторизации покупателя"""
        login = input("Введите логин и нажмите Enter: ")
        password = input("Введите пароль и нажмите Enter: ")
        query = User.select().where(User.login == login and User.password == UserSelector.hash_password(password))
        user_info = [data for data in query.dicts().execute()]
        try:
            print(f'Здравствуйте, {user_info[0]["name"]}')
            return user_info[0]
        except IndexError:
            print('Неверные логин или пароль')

    @staticmethod
    def change_user_info(parameter: str = 'name'):
        """Метод для изменения информации о пользователе
        Принимает строковый аргумент parameter,
        который может принимать следующие значения:
        'name' - для изменения имени,
        'login' - для изменения логина,
        'password' - для изменения пароля"""
        auth_data = UserSelector.log_in()
        if parameter == 'name':
            print('Изменение имени пользователя')
            new_name = input('Введите новое имя пользователя и нажмите Enter: ')
            query_name = User.update(name = new_name).where(User.user_id == auth_data['user_id'])
            query_name.execute()
            print('Логин пользователя успешно изменен!')
        elif parameter == 'login':
            print('Изменение логина пользователя')
            new_login = input('Введите новый логин пользователя и нажмите Enter: ')
            query_name = User.update(login=new_login).where(User.user_id == auth_data['user_id'])
            query_name.execute()
            print('Логин пользователя успешно изменен!')
        elif parameter == 'password':
            print('Изменение пароля пользователя: ')
            old_password = input("Введите старый пароль и нажмите Enter: ")
            query_p_old = User.select(User.password).where(User.user_id == auth_data['user_id'])
            if [data for data in query_p_old.dicts().execute()][0]['password'] != UserSelector.hash_password(old_password):
                raise ValueError('Неверный пароль! Запрос на изменение отклонен')
            new_password = input("""Придумайте и введите пароль, состоящий не менее, чем из 8 из строчных и ЗАГЛАВНЫХ 
        букв английского алфавита, цифр и знаков препинания и нажмите Enter: """)
            if not UserSelector.check_password(new_password):
                raise ValueError('Новый пароль не соответствует параметрам безопасности. Запрос на изменение отклонен')
            p_new = (User.update(password = UserSelector.hash_password(new_password)).where(User.user_id == auth_data['user_id']))
            p_new.execute()
            print('Пароль успешно изменен!')
        else:
            raise ValueError('Неверный аргумент метода "change_user_info"')

    @staticmethod
    def del_user():
        """Метод удаления покупателя из таблицы"""
        auth_data = UserSelector.log_in()
        print('Удаление профиля')
        approval = input("Для подтверждения операции введите пароль и нажмите Enter: ")
        query_p_app = User.select(User.password).where(User.user_id == auth_data['user_id'])
        if [data for data in query_p_app.dicts().execute()][0]['password'] != UserSelector.hash_password(approval):
            raise ValueError('Неверный пароль! Запрос на удаление профиля отклонен')
        del_query = User.delete().where(User.user_id == auth_data['user_id'])
        del_query.execute()
        print('Ваш профиль был успешно удален')

# UserSelector.add_new_user()
print(UserSelector.log_in())
# change_user_info(parameter='password')
# UserSelector.del_user()