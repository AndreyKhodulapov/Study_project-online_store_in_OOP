name = "GoodTypeSelector"

from my_study_projects_2.models import GoodType, Goods


class GoodTypeSelector:
    """Класс для работы с таблицей Типы товаров ('GoodType')"""
    @staticmethod
    def add_new_type():
        """Метод для добавления нового типа товара в таблицу"""
        type_name = input("Введите название типа товаров и нажмите Enter: ")
        GoodType.create(type_name=type_name)
        print('Тип товара успешно внесен')

    @staticmethod
    def get_all_rows_type():
        """Метод, показывающий все типы из таблицы"""
        query = GoodType.select()
        result = query.dicts().execute()
        print('Имеющиеся типы товаров:')
        for row in result:
            print(f"Тип товара: '{list(row.values())[1]}', id: {list(row.values())[0]}")

    @staticmethod
    def get_row_type():
        """Метод, выдающий запрошенный тип товара"""
        GoodTypeSelector.get_all_rows_type()
        request_type = input("""Выберите необходимый тип, скопируйте его название или id, \
введите в запрос и нажмите Enter: """)
        query = (GoodType.select().where(GoodType.type_name == request_type).
                 union(GoodType.select().where(GoodType.type_id == request_type)))
        result = query.dicts().execute()
        print('-------------')
        if result:
            for row in result:
                print(f"Тип товара: '{list(row.values())[1]}', id: {list(row.values())[0]}")
        else:
            print('Тип товара не найден')

    @staticmethod
    def see_goods_in_type():
        """Метод, показывающий какие товары соответствуют запрошенному типу"""
        GoodTypeSelector.get_all_rows_type()
        request_type = input("""Выберите необходимый тип товаров, скопируйте его название или id, \
введите в запрос и нажмите Enter: """)
        query = (GoodType.select(Goods).join(Goods).
                 where(GoodType.type_name == request_type).
                 union(GoodType.select(Goods).join(Goods).where(GoodType.type_id == request_type)))
        result = query.dicts().execute()
        print('-------------')
        if result:
            for good in result:
                print(good)
        else:
            print('В указанном типе товаров пока нет ни одной позиции')

    @staticmethod
    def del_type():
        GoodTypeSelector.get_all_rows_type()
        request_type = input("""Выберите тип для удаления, скопируйте его НАЗВАНИЕ, \
введите в запрос и нажмите Enter: """)
        query = GoodType.select(GoodType.type_id).where(GoodType.type_name == request_type)
        type_id = [t_id for t_id in query.execute()]
        if type_id:
            query1 = GoodType.delete().where(GoodType.type_name == request_type)
            query1.execute()
            print(f'Тип товаров "{request_type}" успешно удален')
            question = input("""Удалить из таблицы 'Товары' все позиции этого типа? 
        Если ДА - введите '1' и нажмите Enter, для завершения работы - просто нажмите Enter """)
            if question == '1':
                query2 = Goods.delete().where(Goods.good_type == type_id)
                query2.execute()
                print(f'Выполнено успешное удаление типа "{request_type}" и всех связанных с ним товаров')
        else:
            print('Такой тип товаров отсутствует')
        print("Работа с таблицей 'Типы товаров' ('GoodType') завершена")

