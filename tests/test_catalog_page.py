import time

from pages.basket_page import Basket_page
from pages.catalog_page import Catalog_page
from pages.product_page import Product_page


def test_catalog_page(set_group, setup):
    catalog = Catalog_page(setup)
    catalog.go_to_category()  # Переход в категорию Смартфоны
    time.sleep(2)
    catalog.filter_product()  # Проверка фильтров и добавление товара в Избранное
    time.sleep(2)
    catalog.go_to_favorite()  # Переход в избранное, куда добавили товар и проверка на наличие товара на странице
    time.sleep(2)
    catalog.filtration_for_buy_product()  # Фильтруем товары для дальнейшей покупки
    time.sleep(2)

    # Просмотр страницы товара
    pp = Product_page(setup)
    pp.product_page()

    # Просмотр страницы корзины и удаление товара из нее
    bp = Basket_page(setup)
    bp.basket_page()



