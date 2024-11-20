import streamlit as st
from functions import get_todos, set_todos

todos = get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    set_todos(todos)




st.title('My Todo App')
st.subheader('This is a todo app.')
st.write('Use this app to check on your tasks.')

for index, i in enumerate(todos):
    checkBox = st.checkbox(i, key=i)
    if checkBox:
        todos.pop(index)
        set_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo",
              on_change=add_todo,key='new_todo')

