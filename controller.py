import view
import model

enum_list = enumerate(model.read_phonebook())

def run():
    view.greetings()
    
    while True:
        view.menu()
        #answer = input('?')
        
        match input('?'):
            case '1':#1.Открыть справочник
                print(end='')
                data = model.read_phonebook()
                view.showcontact(data)
            case '2':#2.Поиск
                model.find()
            case '3':#3.Добавить запись
                model.add_rec()
            case '4':#4.Редактировать данные в записи
                message('Выберите контакт:\n')
                view.showcontact(enum_list)
                model.edit(int(input_data('?')))
            case '5':#5.Удалить запись
                message('Выберите контакт:\n')
                view.showcontact(enum_list)
                model.delete(int(input_data('?')))
            case '6':#6.Закрыть справочник
                break
            case _:
                message('Введены не корректные данные. Введите корректные данные!')
                
def message (message_read):
    print(message_read)
    
    
def input_data (message_read):
    return input(message_read)