from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Produto 1",
        "Empresa 1",
        "2024-01-01",
        "2026-01-01",
        "123456789",
        "Em local seco",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Produto 1"
    assert product.nome_da_empresa == "Empresa 1"
    assert product.data_de_fabricacao == "2024-01-01"
    assert product.data_de_validade == "2026-01-01"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "Em local seco"
