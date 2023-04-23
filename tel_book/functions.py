def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')   

def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:         
        tel_book = f.read() 
    print(search(tel_book, data))  

def change_data() -> None:
    '''Изменение записи'''
    with open('book.txt', 'r', encoding='utf-8') as f:         
        tel_book = f.read() 
    a = tel_book.split('\n')    
    print(a)
    text = input("Введите значение которое нужно заменить: ")      
    b = (search(tel_book, text))
    a[a.index(b)] = edited(b)
    with open("book.txt", "w", encoding='utf-8') as f: 
        f.write('\n'.join(a))

def delete_data() -> None:
    '''Удаление записи'''
    with open('book.txt', 'r', encoding='utf-8') as f:         
        tel_book = f.read() 
    a = tel_book.split('\n')    
    print(a)
    text = input("Введите значение которое нужно удалить: ")      
    b = (search(tel_book, text))
    a[a.index(b)] = remove(b, text)
    with open("book.txt", "w", encoding='utf-8') as f: 
        f.write('\n'.join(a))        

def search(book: str, info: str) -> str:
    '''Находит в строке записи поопределенному критерию поска'''
    book = book.split('\n') 
    return '\n'.join([post for post in book if info in post])

def edited(text: str) -> str:    
    fio = input("Введите новое ФИО, если нужно изменить его: ")
    num = input("Введите новый номер телефона, если нужно измениеть его: ")
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(num) == 0:
        num = text.split(' | ')[1]
    return f'{fio} | {num}'

def remove(text:str, remove_text: str) -> str:
    if remove_text.isalpha():
        num = text.split(' | ')[1]
        return f' | {num}'
    else:
        fio = text.split(' | ')[0]
        return f'{fio} | '                




       