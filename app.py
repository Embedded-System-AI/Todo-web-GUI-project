import streamlit as st

from Todo import *
class ToDoApp(ToDos):
    def __init__(self):
        super().__init__(filepath='todo.txt')
        st.title('Todo App')
        st.subheader('This is my todo app')
        st.write('This app is to increase your productivity')
        self.todos = self.read_file()

    def add_todo(self):
        todo = st.session_state['new_todo']
        print(todo)
        self.todos.append(todo+'\n')
        self.open_file()

    def delete_method(self):
        # self.todos = self.read_file()
        to_delete = st.session_state['action']
        for todo in self.todos:
            if st.checkbox(todo):
                self.todos.remove(to_delete)
                st.experimental_rerun()

    def action(self):
        # self.delete_method()
        st.checkbox(label='',on_change=self.delete_method,value=False,key='action')
        text = st.text_input(label='',placeholder='Add to do', on_change=self.add_todo, key='new_todo')




if __name__=='__main__':
    app=ToDoApp()
    app.action()