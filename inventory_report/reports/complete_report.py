from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = SimpleReport.generate(inventory)
        stock_by_company = cls.stock_by_company(inventory)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n{stock_by_company}"
        )

    def stock_by_company(inventory):
        company = {}
        for product in inventory:
            if product["nome_da_empresa"] in company:
                company[product["nome_da_empresa"]] += 1
            else:
                company[product["nome_da_empresa"]] = 1
        list_stock = ""
        for key, value in company.items():
            list_stock += f"- {key}: {value}\n"
        return list_stock
