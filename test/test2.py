import streamlit as st
from Todo import *

st.title('Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')
todo=ToDos(filepath='todo.txt')

todos=todo.read_file()

for todo in todos:
    if st.checkbox(todo):
        todos.remove(todo)



