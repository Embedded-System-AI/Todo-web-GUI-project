import sys


class ToDos:

    def __init__(self,filepath):
        self.filepath = filepath
        self.todos = []

    def add(self,menu):
        todo=menu[4:] + '\n'
        self.read_file()
        self.todos.append(todo)
        self.open_file()

    def read_file(self):
        with open(self.filepath, 'r') as file:
            self.todos = file.readlines()
        return self.todos

    def show(self,menu):

        self.read_file()
        for index,item in enumerate(self.todos):
            item=item.strip('\n')
            row=f'{index+1} - {item}'
            print(row)

    def edit(self,menu):

        try:

            number = int(menu[5:])
            number = number - 1
            self.read_file()
            new_todo = input('Enter a new todo')
            self.todos[number] = new_todo
            self.open_file()

        except ValueError:
            print('This is uncorrected, we expect to enter integer number.')

        except IndexError:
            print('This is uncorrected index.')

    def open_file(self):
        with open(self.filepath, 'w') as file:
            file.writelines(self.todos)

    def delete(self,menu):
        try:

            number = int(menu[7:])

            number = number - 1

            self.read_file()

            todo_to_remove=self.todos[number].strip('\n')
            self.todos.pop(number)
            self.open_file()

            massage = f'This todo {todo_to_remove} was deleted from file.'
            print(massage)

        except ValueError:
            print('This is uncorrected, we expect to enter integer number.')

        except IndexError:
            print('This is uncorrected index.')

    def exit(self,menu):
        print('Bye')
        sys.exit()
