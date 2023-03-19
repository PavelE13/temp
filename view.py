def greetings():
    print('Телефонный справочник v1.0.23')


def menu():
    print('\nВыберите действие\n 1. Открыть справочник\n 2. Поиск\n 3. Добавить запись\n 4. Редактировать запись\n 5. Удалить данные в записи\n 6. Закрыть справочник\n') 
    
    
def showcontact(contact_output):
    print(*contact_output)