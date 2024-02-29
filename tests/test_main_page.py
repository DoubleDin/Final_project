
from pages.main_page import Main_page


def test_main_page(setup, set_group):

    mp = Main_page(setup)

    # Авторизация
    mp.main_authorization()

    # Поиск товара в в строке поиска и переход на страницу с найденными товарами
    mp.searching()

    # Скролл к популярным категориям, выбор категории и переход на нее
    mp.choice_popular_category()

    # Новинки товаров, скролл к блоку и клик по стрелкам вперед/назад
    mp.top_rating_product()

    # Переход в каталог

    mp.transit_to_catalog()




