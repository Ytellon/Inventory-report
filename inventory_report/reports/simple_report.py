from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        oldest_date = cls.manufacturing_data(inventory)
        close_exp = cls.closest_expiration_date(inventory)
        big_stock = cls.biggest_stock(inventory)
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {close_exp}\n"
            f"Empresa com mais produtos: {big_stock}"
        )

    def manufacturing_data(inventory):
        return min(
            oldest_date["data_de_fabricacao"] for oldest_date in inventory
        )

    def closest_expiration_date(inventory):
        date_now = datetime.now().strftime("%Y-%m-%d")

        return min(
            closest_date["data_de_validade"]
            for closest_date in inventory
            if closest_date["data_de_validade"] > date_now
        )

    def biggest_stock(inventory):
        return Counter(
            biggest_stock["nome_da_empresa"] for biggest_stock in inventory
        ).most_common(1)[0][0]
