phone_book = {'Alla' : '+380671234567',
              'Anna' : '+380971234567',
              'Emma' : '+380501234567',
              'Inna' : '+380991234567'}


#decorator    
def input_error(func):
    def simple_wrapper(contact):
        try:
            func(contact)
            print('Completed successfully')
        except KeyError:
            print('There is not the name in the phone book')
        except IndexError:
            if contact[0] == '':#якщо після phone (заодно після add, change) нема нічого
                print('Enter user name after the command')
            else:             
                print('Enter user name and phone with a space')    
        except (UnboundLocalError, ValueError):
            print('Enter phone number correctly')
        main()
    return simple_wrapper

@input_error
def add_func(contact):
    correct_name = contact[0][0].upper() + contact[0][1:]
    correct_phone = sanitize_phone_number(contact[1])
    phone_book[correct_name] = correct_phone

#handlers:  
@input_error
def change_func(contact):
    correct_name = contact[0][0].upper() + contact[0][1:]
    phone_book.pop(correct_name)#інакше просто запише новий контакт, якщо ім'я введене з помилкою 
    correct_phone = sanitize_phone_number(contact[1])
    phone_book[correct_name] = correct_phone

@input_error
def phone_func(contact):
    correct_name = contact[0][0].upper() + contact[0][1:]
    print(phone_book[correct_name])

handlers = {
    'add' : add_func,
    'change' : change_func,
    'phone' : phone_func
}

def get_handler(start_command):
    return handlers[start_command]

def sanitize_phone_number(phone):
    phone = (phone.strip()
            .replace("(", "")
            .replace(")", "")
            .replace("-", ""))
    if len(phone) == 12:
            correct_phone = '+' + phone
    elif len(phone) == 11:
            correct_phone = '+3' + phone
    elif len(phone) == 10:
            correct_phone = '+38' + phone
    return correct_phone


def main():#Цикл запит-відповідь
    while True:
        command = input('...')#може це не треба, просто ніби запрошення щось написати
        command = (command.lower().strip())
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'show all':
            print(phone_book)
        else:
            parse(command)

            
def parse(command):#Парсер команд
    if command.startswith('add'):
        index = 3
    elif command.startswith('change'):
        index = 6
    elif command.startswith('phone'):
        index = 5
    else:
        print('The command is unknown')
        main()
    start_command = command[:index]
    end_command = (command[index:].strip())
    contact = end_command.split(' ')
    hendler = get_handler(start_command)
    hendler(contact)
    

if __name__ == "__main__":
    
    main()
