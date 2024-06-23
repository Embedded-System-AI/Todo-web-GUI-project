import streamlit as st

from Todo import *
class ToDoApp(ToDos):
    def __init__(self):
        super().__init__(filepath='todo.txt')
        st.title('Todo App')
        st.subheader('This is my todo app')
        st.write('This app is to increase your productivity')
        self.todos = self.read_file()
    def delete(self):
        # self.todos = self.read_file()
        for todo in self.todos:
            if st.checkbox(todo):
                self.todos.remove(todo)
                st.experimental_rerun()


if __name__=='__main__':
    app=ToDoApp()
    app.delete()