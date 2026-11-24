import json
from typing import Any

from src.models import Category, Product


def load_data_from_json(file_path: str) -> list[Category]:
    """Читает классный JSON-файл и возвращает список объектов Category с объектами Product."""
    with open(file_path, "r", encoding="utf-8") as file:
        raw_data: list[dict[str, Any]] = json.load(file)

    categories: list[Category] = []

    for category_item in raw_data:
        products_list: list[Product] = []
        for product_item in category_item.get("products", []):
            product = Product(
                name=product_item["name"],
                description=product_item["description"],
                price=product_item["price"],
                quantity=product_item["quantity"],
            )
            products_list.append(product)

        category = Category(
            name=category_item["name"],
            description=category_item["description"],
            products=products_list,
        )
        categories.append(category)

    return categories
