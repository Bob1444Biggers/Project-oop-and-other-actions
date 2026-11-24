import json
from pathlib import Path

from src.models import Category, Product
from src.utils import load_data_from_json


def test_product_init() -> None:
    """Проверка корректности инициализации объекта Product."""
    product = Product("Тестовый товар", "Описание товара", 1500.50, 10)
    assert product.name == "Тестовый товар"
    assert product.description == "Описание товара"
    assert product.price == 1500.50
    assert product.quantity == 10


def test_category_init(sample_category: Category, sample_products: list[Product]) -> None:
    """Проверка корректности инициализации объекта Category и не более."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Описание категории смартфонов"
    assert sample_category.products == sample_products
    assert len(sample_category.products) == 2


def test_category_counters(sample_category: Category) -> None:
    """Проверка подсчёта количества категорий и товаров."""
    assert Category.category_count == 1
    assert Category.product_count == 2

    extra_product = Product("Телевизор", "4K экран", 50000.0, 3)
    Category("Телевизоры", "Описание телевизоров", [extra_product])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_load_data_from_json(tmp_path: Path) -> None:
    """Проверка загрузки категорий и товаров из JSON-файла."""
    Category.category_count = 0
    Category.product_count = 0

    test_data = [
        {
            "name": "Книги",
            "description": "Художественная литература",
            "products": [
                {"name": "1984", "description": "Роман-антиутопия", "price": 500.0, "quantity": 12}
            ],
        }
    ]
    json_file = tmp_path / "test_products.json"
    json_file.write_text(json.dumps(test_data, ensure_ascii=False), encoding="utf-8")

    categories = load_data_from_json(str(json_file))

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Книги"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "1984"
    assert Category.category_count == 1
    assert Category.product_count == 1
