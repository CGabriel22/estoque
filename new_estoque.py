import os.path
import csv


def register():
    product = input('Informe o nome do produto:')
    qnt = int(input('Informe a quantidade:'))
    with open('estoque.csv', 'a') as file:
        w = csv.writer(file)
        w.writerow([product, qnt])
        print('\nproduto inserido com sucesso! :)\n')


def listProducts():
    mode = input('Por nome ou quantidade?')
    products = []
    with open('estoque.csv', 'r') as file:
        r = csv.reader(file)
        for row in r:
            products.append(row)
        if mode == 'nome':
            products_ord = sorted(products, key=lambda ref: len(ref[0]))
            for product in products_ord:
                print(f'Produto: {product[0]}\nQuantidade: {product[1]}\n')

        elif mode == 'quantidade':
            products_ord = sorted(products, key=lambda ref: int(ref[1]), reverse=True)
            for product in products_ord:
                print(f'Produto: {product[0]}\nQuantidade: {product[1]}\n')

        else:
            print('escolha uma opção valida\n')
            listProducts()
            return False


def search():
    mode = input('Busca por nome ou quantidade?')
    has_product = False
    product_response = []
    if mode == 'nome':
        product_ref = input('Qual o nome do produto?')
        with open('estoque.csv', 'r') as file:
            r = csv.reader(file)
            for row in r:
                if row[0] == product_ref:
                    has_product = True
                    product_response = row
        if not has_product:
            print('\nO produto está indisponível\n')
            return False
        else:
            print(f'Produto: {product_response[0]}\nQuantidade: {product_response[1]}\n')

    elif mode == 'quantidade':
        qnt_ref = input('Informe a quantidade desejada para a busca:')
        with open('estoque.csv', 'r') as file:
            r = csv.reader(file)
            for row in r:
                if row[1] == qnt_ref:
                    has_product = True
                    product_response.append(row)
        if not has_product:
            print('\nO produto está indisponível\n')
            return False
        else:
            for p in product_response:
                print(f'Produto: {p[0]}\nQuantidade: {p[1]}\n')
    else:
        print('escolha uma opção valida\n')
        search()
        return False


def update():
    product = input('Qual o produto?')
    has_product = False
    products = []
    with open('estoque.csv', 'r') as file:
        r = csv.reader(file)
        for row in r:
            if row[0] == product:
                new_qnt = input('Qual a nova quantidade?')
                row[1] = new_qnt
                products.append(row)
                has_product = True
            else:
                products.append(row)
    if not has_product:
        print('\nO produto está indisponível\n')
        return False
    with open('estoque.csv', 'w') as file:
        w = csv.writer(file)
        w.writerows(products)
        print('\nProduto atualizado com sucesso\n')


def remove():
    product = input('Qual o nome do produto a ser removido?')
    has_product = False
    products = []
    with open('estoque.csv', 'r') as file:
        r = csv.reader(file)
        for row in r:
            if row[0] == product:
                has_product = True
            else:
                products.append(row)
    if not has_product:
        print('\nO produto está indisponível\n')
        return False
    with open('estoque.csv', 'w') as file:
        w = csv.writer(file)
        w.writerows(products)
        print('\nProduto removido com sucesso\n')


def init():
    if not os.path.exists('estoque.csv'):
        print('criando arquivo estoque.csv ...')
        open('estoque.csv', 'w', newline='', encoding='utf-8')

    while True:
        operation = input('[C] Cadastrar\n\
[L] Listar\n\
[B] Buscar\n\
[A] Atualizar\n\
[R] Remover\n\
[S] Sair\n\
Escolha uma operação:')
        operation = operation.lower()

        if operation != 'c' and \
                operation != 'l' and \
                operation != 'b' and \
                operation != 'a' and \
                operation != 'r' and \
                operation != 's':
            print('\n !!Por favor, escolha uma opção valida!! \n')
            continue

        if operation == 's':
            print('\n------------------------ Fim ----------------------------\n')
            print('------------------- Volte sempre :) ---------------------\n')
            break

        if operation == 'c':
            register()

        if operation == 'l':
            listProducts()

        if operation == 'b':
            search()

        if operation == 'r':
            remove()

        if operation == 'a':
            update()


if __name__ == "__main__":
    init()
