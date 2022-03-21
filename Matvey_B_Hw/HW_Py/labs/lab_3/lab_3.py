def welcome():
    choose_an_action = int(input("""
Доступные команды:
    1. Отобразить сущесвтующие контакты
    2. Cоздать новый контакт
    3. Найти/показать номер по имени
    4. Удалить номер по имени
    5. Выйти
    

Введите одну из предложенных цифр: """))
    return choose_an_action


def phonebook():
    contact = {}

    while True:
        choose_an_action = welcome()

        if choose_an_action == 1:
            if bool(contact):
                for key, value in contact.items():
                    print(key, "-->", value)
            else:
                print("Пустая телефонная книга! Вернись в меню и добавь контакт ")

        elif choose_an_action == 2:

            phone_number = input('Введите номер телеофана: ')
            contact_name = input('Введите ФИ контакта: ')

            if phone_number not in contact.items():
                contact.update({contact_name: phone_number})
                print('Телефон успешно сохранен!')
                print('Ваша обновленная телефонная книга покажется снизу')

                for key, value in contact.items():
                    print(key, "-->", value)
            else:
                print('Такой телефон уже записан')

        elif choose_an_action == 3:
            name = input('Введите имя контакта, чей номер хотите узнать: ')

            if name in contact:
                print('Контакт:', name, ':', contact[name])
            else:
                print('Такого контакта не существует или ошибка в имени ')
                print('Попробуй еще раз или вернись в меню и добавь новый контакт')

        elif choose_an_action == 4:
            name = input('Введите Имя контакта, чей номер вы хотели бы удалить: ')
            confirm = "No"
            print(contact)
            if name in contact:
                print('Контакт:', name, ':', contact[name])
                confirm = input('Вы уверены, что хотите удалить этот контакт? Yes/No ')
            else:
                print('Такого контакта не существует или ошибка в имени ')

            if confirm.capitalize() == 'Yes':

                contact.pop(name)

                for key, value in contact.items():
                    print('Ваша обновленная телефонная книга покажется снизу')
                    print(key, "-->", value)

            else:
                print('Возвращаемся в главное меню...')

        elif choose_an_action == 5:
            print('__________')
            break

        else:
            print('Некорректный номер действия! Введите 1/2/3/4/5 ')


phonebook()
