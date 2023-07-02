# импорт необходимых модулей,функций
from abc import ABC, abstractmethod
from .main_code_bot import main
from .note import run_command
from .sort import Sorter


# инициализируем объект класса Sorter
sort_folder = Sorter()

# переменные, пример для ввода пути папки на разных OS
windows = r"Windows: C:\Users\Username\Documents\My_Folder"
macOS = r"macOS: /Users/Username/Documents/My_folder"
linux = r"Linux: /home/Username/Documents/My_folder"

#Базвый интерфейс абстрактного продукта 'Help'
class AbstractHelp(ABC):
    @abstractmethod
    def operation_help(self) -> str:
        pass


#Базвый интерфейс абстрактного продукта 'Exit'
class AbstractExit(ABC):
    @abstractmethod
    def operation_exit(self) -> str:
        pass


#Базвый интерфейс абстрактного продукта 'Command'
class AbstractCommand(ABC):
    @abstractmethod
    def operation_command(self, commanda) -> str:
        pass


#Интерфейс абстрактной фабрики для создания типов каждого продукта
class AbstractBot(ABC):
    @abstractmethod
    def help(self) -> AbstractHelp:
        pass

    @abstractmethod
    def exit(self) -> AbstractExit:
        pass

    @abstractmethod
    def command(self) -> AbstractCommand:
        pass


#Реализация конктретной фабрики 'MainBot'
class MainBot(AbstractBot):
    def __init__(self):
        print(f"\nHi, this main menu bot. I can help with the following tasks\n\n- Maintain your personal contact book (to access this function, please enter 'Сontact book')\n\n- Enter any of your test NoteBooks (to access this function, please enter 'NoteBook')\n\n- Sort files in the specified folder by category (to access this function, please enter 'Sort')\n\nFor more detailed information, enter 'Help'\nFor finish bot, enter 'Exit'")
    
    def help(self) -> AbstractHelp:
        return MainBotHelp()
    
    def exit(self) -> AbstractExit:
        return MainBotExit()
    
    def command(self) -> AbstractCommand:
        return MainBotCommand()


#Реализация конктретной фабрики 'ContactBook'
class ContactBook(AbstractBot):
    def __init__(self):
        print(f"\nI am a contact book helper bot!\nI can:\n- Save contacts in Сontact book with names, addresses, phone numbers, email and birthdays (to access this function, please enter 'Add')\n- Display a list of contacts whose birthday is a specified number of days from the current date (to use this function, please enter 'Birthday-list (number)')\n- Search for contacts among contacts in the book (to use this function, please enter 'Search'\n- Edit entries from the contact book (to use this function, please enter 'Edit');\n- Delete entries from the contact book (to use this function, please enter 'Delete')\n- Save contacts to a file (to use this function, please enter 'Save')\n- View contacts saved in the file (to use this function, please enter 'Read')\n\nI also check the correctness of the entered phone number and email when creating or editing a record and notify you in case of an incorrect entry\nFor more detailed information, enter 'Help' or 'Exit' to return to the main menu")
    
    def help(self) -> AbstractHelp:
        return ContactBookHelp()
        
    def exit(self) -> AbstractExit:
        return ContactBookExit()
    
    def command(self) -> AbstractCommand:
        return ContactBookCommand()
    

#Реализация конктретной фабрики 'NoteBook'
class NoteBook(AbstractBot):
    def __init__(self):
        print(f"\nI am a NoteBookbook helper bot!\nI can:\n- Save NoteBooks with text information and keywords (tags) (to access this function, please enter 'Add')\n- Search for NoteBooks (to use this function, please enter 'Search')\n- Search for NoteBooks and show all NoteBooks (to use this function, please enter 'Search-all')\n- Edit NoteBooks by index (to use this function, please enter 'Edit-index')\n- Edit NoteBooks by keywords (tags)  (to use this keyword, please enter 'Edit-keyword')\n- Delete NoteBooks by index (to use this function, please enter 'Delete-index')\n- Delete NoteBooks by keywords (tags)  (to use this function, please enter 'Delete-keyword')\n- Sort NoteBooks (to use this function, please enter 'Sort')\nFor more detailed information, enter 'Help'")

    def help(self) -> AbstractHelp:
        return NoteBookHelp()
    
    def exit(self) -> AbstractExit:
        return NoteBookExit()
    
    def command(self) -> AbstractCommand:
        return NoteBookCommand()
    

#Реализация конктретной фабрики 'Sort'
class Sort(AbstractBot):
    def __init__(self):
        print(f'\nI am a sort of helper bot!\n\nI can:\n- Sort files in the specified folder by category (to use this function, please enter "Sort folder path")\n Folder path for different OS:\n{windows}\n{macOS}\n{linux}')

    def help(self) -> AbstractHelp:
        return SortHelp()
    
    def exit(self) -> AbstractExit:
        return SortExit()
    
    def command(self) -> AbstractCommand:
        return SortCommand()
    

#Реализация конктретного продукта 'MainBotHelp'
class MainBotHelp(AbstractHelp):
    def operation_help(self) -> str:
        print(f"\nThe personal assistant console program can implement the following functionality:\n1) A contact book that can:\n- save contacts with names, addresses, phone numbers, email, and birthdays to the contacts book;\n- display a list of contacts whose birthday is a specified number of days from the current date;\n- check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect entry;\n- search for contacts among book contacts;\n- edit and delete entries from the contact book;\nTo switch to the contact book functionality, please enter 'Сontact book'\n\n2) NoteBookbook that can:\n- save NoteBooks with text information;\n- search for NoteBooks;\n- edit and delete NoteBooks;\n- add 'tags' to NoteBooks, keywords describing the subject and subject of the record;\nsearch and sort NoteBooks by keywords (tags);\nTo switch to the NoteBookbook functionality, please enter 'NoteBook'\n\n3) Sort, which can sort files in the specified folder by categories (images, documents, videos, etc.).\nTo switch to the Sort function, please enter 'Sort'\n\nTo exit the Assistant bot, enter 'Exit'\n")


#Реализация конктретного продукта 'ContactBookHelp'
class ContactBookHelp(AbstractHelp):
    def operation_help(self) -> str:
        print(f"\nThe contact book can implement the following functionality:\n'Add' - adds contact book with names, addresses, phone numbers, email, and birthdays. In order to save the contact, click Add and enter all the necessary information, the required field is Name - this is a unique property of the contact. Also, in the Add function, a check for the adds connput parameters such as Phone number and Email is implemented.\n\nThe contact book has the ability to save contacts' birthdays:\n'Birthday-list (number)' -  display a list of contacts whose birthday is a specified number of days from the current date\n\nWork with the list of contacts is implemented using advanced functions:\n'Search contact' - search for contacts,instead of a contact, enter a request (name/part of a name);\n'Show all' - show all contacts\n'Edit contact'- edit entries from the contact book, instead of contact, enter the name contact;\n'Remove-contact' - delete contact, enter the name for delete;\n'Save' - save contacts to a file (.csv file format).\n'Read' - read data from file (.csv file format)\n\nEnter the command you need from the list above.\nReturn to the main menu, enter 'Exit'")


#Реализация конктретного продукта 'NoteBookHelp'
class NoteBookHelp(AbstractHelp):
    def operation_help(self) -> str:
        print(f"\nThe NoteBookbook has the following list of functions, it can store NoteBooks with text information, search for NoteBooks, edit and delete NoteBooks, it is also possible to add 'tags' to NoteBooks, keywords describing the topic and subject of the record, search and sort NoteBooks by keywords (tags).\n\nThe list of commands is as follows:\n'Add' - save NoteBooks with text information and keywords (tags);\n'Search' - search for NoteBooks;\n'Search-all' - search for NoteBooks and show all NoteBooks;\n'Edit-index' - edit NoteBooks by index\n'Edit-keyword' - edit NoteBooks by keywords (tags)\n'Delete-index' - delete NoteBooks by index \n'Delete-keyword' - delete NoteBooks by keywords (tags)\n'Sort' - sort NoteBooksEnter the command you need from the list above.\nReturn to the main menu, enter 'Exit'")


#Реализация конктретного продукта 'SortHelp'
class SortHelp(AbstractHelp):
    def operation_help(self) -> str:
        print(f'\nI am a sort of helper bot!\n\nI can:\n- Sort files in the specified folder by category (to use this function, please enter "Sort folder path")\n Folder path for different OS:\n{windows}\n{macOS}\n{linux}')
    

#Реализация конктретного продукта 'MainBotExit'
class MainBotExit(AbstractExit):
    def operation_exit(self) -> str:
        return f'exit'


#Реализация конктретного продукта 'ContactBookExit'
class ContactBookExit(AbstractExit):
    def operation_exit(self) -> str:
        return f"Hi, this main menu bot, please enter your choice or 'help' to see my options: "


#Реализация конктретного продукта 'NoteBookExit'
class NoteBookExit(AbstractExit):
    def operation_exit(self) -> str:
        return f"Hi, this main menu bot, please enter your choice or 'help' to see my options: "
    

#Реализация конктретного продукта 'SortExit'
class SortExit(AbstractExit):
    def operation_exit(self) -> str:
        pass


#Реализация конктретного продукта 'MainBotCommand'
class MainBotCommand(AbstractCommand):
    def operation_command(self, commanda) -> str:
        if commanda == 'contact book':
            return f'contact book'
        elif commanda == 'noteBook':
            return f'noteBook'
        elif commanda == 'sort':
            return f'sort'  
        else:
            return f'You have entered an invalid command'


#Реализация конктретного продукта 'ContactBookCommand'
class ContactBookCommand(AbstractCommand):
    def operation_command(self, commanda) -> str:
        return main(commanda)


#Реализация конктретного продукта 'NoteBookCommand'
class NoteBookCommand(AbstractCommand):
    def operation_command(self, commanda) -> str:
        return run_command(commanda)


#Реализация конктретного продукта 'SortCommand'
class SortCommand(AbstractCommand):
    def operation_command(self, commanda) -> str:
        try:
            if commanda.lower().strip().startswith('sort') and commanda.lower().strip()[5:]:
                return sort_folder.sort(commanda.lower().strip()[5:])
            else:
                print('Invalid command')
        except FileNotFoundError:
            print(f'Not find the path, please repeat the command and enter correct path to folder')


#функция инициализации определенной фабрики в коде
def client_code(bot: AbstractBot):
    while True:
        user_input = input("Enter a command: ").lower().strip()
        if user_input == 'help':
            bot.help().operation_help()
        elif user_input == 'exit':
            bot.exit().operation_exit()
            break
        elif user_input:
            user_input = bot.command().operation_command(user_input)
            if user_input == 'exit':
                break
            elif user_input == 'help':
                bot.help().operation_help()
        else:
            print("Invalid command")

#функция  поведения бота, в зависимости от конктретной фабрики
def main_menu():
    bot = MainBot()
    while True:
        user_input = input("This main menu bot, enter a command or 'help' to see options: ").lower().strip()
        if user_input == 'contact book':
            client_code(ContactBook())
        elif user_input == 'notebook':
            client_code(NoteBook())
        elif user_input == 'sort':
            client_code(Sort())
        elif user_input == 'help':
            bot.help().operation_help()
        elif user_input == 'exit':
            break
        else:
            print("Invalid command")
    print("Goodbye!")

#функция старт и запуска бота 
def start_bot():
    while True:
        user_input = input("Hello, I'm a personal assistant console bot. Enter 'Hello' to get started: ").lower().strip()
        if user_input == 'hello':
            main_menu()
            break
        else:
            print("Invalid command")

   