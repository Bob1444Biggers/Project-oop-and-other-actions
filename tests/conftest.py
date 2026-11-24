import pytest

from src.models import Category, Product


@pytest.fixture
def sample_products() -> list[Product]:
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
    ]


@pytest.fixture
def sample_category(sample_products: list[Product]) -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        name="Смартфоны",
        description="Описание категории смартфонов",
        products=sample_products,
    )
