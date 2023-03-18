import controller

def read_phonebook():
    with open('file.txt', 'r', encoding='utf-8') as file:
        return file.readlines()
        

def add_rec():
    
    while True:
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию:')
        code_count = input('Введите код страны:')
        phone = input("Введите телефон:")
        file = open("file.txt", "a", encoding='utf-8')
        contact = first_name + ' ' + last_name + ' ' + code_count + ' ' + phone + '\n'
        file.write(contact)
        
        match input('Добавить ещё контакт(y/n)?'):
            case 'y':
                continue
            case 'n':          
                file.close
                return contact
            case _:
                controller.message()
                return
