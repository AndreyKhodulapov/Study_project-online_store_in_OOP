name = "models"

"""Модели для магазина в ООП подходе"""


from peewee import *
import datetime


db = SqliteDatabase('C:/Users/Andrey/PycharmProjects/pythonProject/my_study_projects_2/my_store_db.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class BankAccount(BaseModel):
    """Модель банковского аккаунта клиента"""
    account_id = IntegerField(primary_key=True)
    money = DecimalField(max_digits=12, decimal_places=2, null= False, default=0.0)
    class Meta:
        table_name = "BankAccounts"


class User(BaseModel):
    """Модель клиента"""
    user_id = IntegerField(primary_key=True)
    name = CharField(max_length=50, null= False)
    login = CharField(max_length=50, null=False)
    password = CharField(max_length=150, null=False)
    money = ForeignKeyField(BankAccount)
    class Meta:
        table_name = "Users"


class GoodType(BaseModel):
    """Модель категории товара"""
    type_id = IntegerField(primary_key=True)
    type_name = CharField(max_length=50)
    class Meta:
        table_name = "GoodTypes"


class Goods(BaseModel):
    """Модель товара"""
    good_id = IntegerField(primary_key=True)
    good_name = CharField(max_length=150, null= False)
    brand = CharField(max_length=50, null= True)
    made_in = CharField(max_length=50, null= True)
    color = CharField(max_length=50, null= False)
    size = CharField(max_length=50, null= False)
    keywords = CharField(max_length=150, null= False)
    good_type = ForeignKeyField(GoodType)
    amount = IntegerField(null= False, default=0)
    price = DecimalField(max_digits=12, decimal_places=2, null= False, default=0.0)


class ShoppingCard(BaseModel):
    """Модель корзины покупок"""
    good_number = IntegerField(primary_key=True)
    goods = ForeignKeyField(Goods, null=False)
    amount = IntegerField(null=False, default=1)


class Orders(BaseModel):
    """Модель истории заказов"""
    pur_id = IntegerField(primary_key=True)
    purchase_data = DateTimeField(default=datetime.datetime.now, null=False)
    total_pur_price = DecimalField(max_digits=12, decimal_places=2, null= False, default=0.0)
    customer = ForeignKeyField(User)
