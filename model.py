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
        file.close
        
        match controller.input_data('Добавить ещё контакт(y/n)?'):
            case 'y':
                continue
            case 'n':          
                file.close
                return contact
            case _:
                controller.message('Введены не корректные данные. Введите корректные данные!')
                return

def find():
    f = controller.input_data("Введите элемент поиска: ")
    lines = read_phonebook()
    count = 0
    flag=False
    
    for line in lines:
        if f in line:
            print(line)
            count += 1
            flag = True
    if flag:
        print(f'Найдено {count} контактов. Поиск завершен!')
    else:
        controller.message('Контакт не найден')
  
        
def delete(choice_key):
    lines = enumerate(read_phonebook())
    with open('file1.txt', 'w', encoding='utf-8') as files:
        for key, value in lines:
            if choice_key != key:
                files.writelines(value)
          

def edit(choice_key):
    lines = read_phonebook()
    count = 1
    new_lines_tmp = ''
    with open('file2.txt', 'w', encoding='utf-8') as files:
        for line in lines:
            if choice_key == count:
                new_lines_tmp = change_rec()
            else:
                new_lines_tmp = line
            files.write(new_lines_tmp)
            count +=1
         
            
def change_rec():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию:')
    code_count = input('Введите код страны:')
    phone = input("Введите телефон:")
    contact = first_name + ' ' + last_name + ' ' + code_count + ' ' + phone + '\n'
    return contact