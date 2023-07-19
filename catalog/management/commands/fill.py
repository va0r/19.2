from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Products:
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Список категорий для добавления
        categories = [

            {'title': 'Овощи',
             'description': 'Кулинарный термин, обозначающий съедобную часть (например, плод или клубень) '
                            'некоторых растений, а также всякую твёрдую растительную пищу, за исключением фруктов, '
                            'круп и орехов (включение в эту категорию плодовых тел грибов и съедобных водорослей '
                            'зависит от источника). Кулинарный термин «овощ» может применяться к съедобным плодам, '
                            'которые с точки зрения ботаники являются ягодами.'},

            {'title': 'Фрукты',
             'description': 'Сочный съедобный плод растения. Фрукты являются важной составляющей пищи человека и '
                            'многих животных.'},

            {'title': 'Компьютеры',
             'description': 'Функциональное устройство, способное выполнять значительный объём вычислений, '
                            'включая многочисленные арифметические и логические операции, без вмешательства '
                            'человека. Компьютер может быть как отдельным блоком, так и состоять из нескольких '
                            'взаимосвязанных устройств. Является синонимом терминов «электронная вычислительная '
                            'машина», «вычислительная система».'},

            {'title': 'Бытовая техника',
             'description': 'Электрические и/или механические приборы, которые выполняют некоторые бытовые функции, '
                            'такие как приготовление пищи или чистка.'},

        ]

        # Очистка таблицы Category
        Category.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице Category
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Список экземпляров класса Category
        categories_for_create = []
        for category in categories:
            categories_for_create.append(Category(**category))

        # Добавление категорий в базу данных
        Category.objects.bulk_create(categories_for_create)

        # Список продуктов для добавления в БД
        products = [

            {'title': 'Огурец', 'price': 5, 'category': categories_for_create[0],
             'description': 'Однолетнее травянистое растение, вид рода Огурец (Cucumis) семейства Тыквенные '
                            '(Cucurbitaceae), овощная культура.'},  # Категория "овощи"

            {'title': 'Яблоко', 'price': 5, 'category': categories_for_create[1],
             'description': 'Сочный плод яблони, который употребляется в пищу в свежем и запеченном  виде, служит '
                            'сырьём в кулинарии и для приготовления напитков.'},  # Категория "фрукты"

            {'title': 'Ноутбук', 'price': 5, 'category': categories_for_create[2],
             'description': 'Переносной компьютер, в корпусе которого объединены типичные компоненты '
                            'персонального компьютера, включая дисплей, клавиатуру и устройство '
                            'указания (обычно сенсорная панель или тачпад), а также аккумуляторные '
                            'батареи. '},  # Категория "компьютеры"

            {'title': 'Телевизор', 'price': 5, 'category': categories_for_create[3],
             'description': 'Приёмник телевизионных сигналов изображения и звука, отображающий их на '
                            'экране и с помощью динамиков.'}  # Категория "бытовая техника"

        ]

        # Очистка таблицы Product
        Product.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице Product
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

        # Список экземпляров класса Product
        products_for_create = []
        for product in products:
            products_for_create.append(Product(**product))

        # Добавление продуктов в базу данных
        Product.objects.bulk_create(products_for_create)
