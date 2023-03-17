import view
import model

def run():
    view.greetings()
    
    while True:
        view.menu()
        #answer = input('?')
        
        match input('?'):
            case '1':#1.Открыть справочник
                data = model.read_phonebook
                view.showcontact(data)
            case '2':#2.Поиск
                model.find()
            case '3':#3.Добавить запись
                model.add_rec()
            case '4':#4.Добавить\Изменить данные в записи
                view.mod_data()
            case '5':#5.Закрыть справочник
                break
            case _:
                view.message()