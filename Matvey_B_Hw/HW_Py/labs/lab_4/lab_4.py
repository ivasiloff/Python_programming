"""

3.

Разработать систему учета товаров для магазина, продающего бытовую технику. Разработать
классовую структуру для учета двух-трех типов товаров (например, климатическая техника,
техника для кухни).

"""


# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.
"""
 {
 "id":"12CC1",
 "product":"coca-cola 0.5",
 "department": "drinks",
 "coast":"1$"
 }
"""

import pprint


def generate_products():
    departments = {1: 'bakery', 2: 'drinks', 3: 'dairy', 4: 'meat'}
    # name, items, price, department_id,
    products = [
                ['bread', 1, 10.0, 1],
                ['sausage', 1, 25.0, 4],
                ['bacon', 1, 45.0, 4],
                ['sour cream', 1, 5.25, 3],
                ['coca-cola', 1, 1.15, 2]
               ]

    d = []
    for idx, product in enumerate(products):
        d.append({
                    'id': idx,
                    'product': product[0],
                    'department': departments[product[3]],
                    'dep_id': product[3],
                    'price': product[2],
                    'items': product[1]
        })

    return d


products = generate_products()


def show_all_products():
    pprint.pprint(generate_products())


def get_product_by_id(prod_id):
    # num = input("Enter product id :")
    found = 'No such product is found'
    for pr in products:
        if pr['id'] == int(prod_id):
            found = pr
            break
    else:
        print("please enter a digit")
        return

    return found


def get_products_by_department(num):
    cnt = 0
    for pr in products:
        if pr['dep_id'] == num:
            cnt += 1
    return cnt


def update_product_by_id(num):
    found = get_product_by_id(num)
    pprint.pprint(found)
    if found:
        for key in found.keys():
            confirm = input('Do you want to change <<{}>>, Y or N? '.format(key))
            if confirm == 'Y':
                new_value = input('Enter new value for <<{}>>? '.format(key))
                found[key] = new_value
                print("New value is: {}".format(found[key]))
            else:
                print('No Change!')
                pass
        pprint.pprint(found)


def delete_product_by_id(num):
    for pr in products:
        if pr['id'] == int(num):
            prod_idx = products.index(pr)
            products.pop(prod_idx)

    return products

def manage_products():
    choice = int(input("Select options: " \
             "1. Show all products, " \
             "2. Show product, " \
             "3. Show products by department, " \
             "4. Update product, " \
             "5. Delete product"))

    if choice == 1:
        print("SHOW ALL PRODUCTS: \n")
        show_all_products()
        manage_products()
    elif choice == 2:
        prod_id = int(input("Enter product ID: "))
        pprint.pprint(get_product_by_id(prod_id))
        manage_products()
    elif choice == 3:
        num = int(input("Enter department id, 1:Bakery, 2:Drinks, 3:Dairy, 4:Meat:"))
        print("Number of products: ", get_products_by_department(num))
        manage_products()
    elif choice == 4:
        num = int(input("Enter product id: "))
        update_product_by_id(num)
        manage_products()
    elif choice == 5:
        num = int(input("Enter product id you want to delete:"))
        print('All products')
        pprint.pprint(delete_product_by_id(num))

        manage_products()
    else:
        return

manage_products()

