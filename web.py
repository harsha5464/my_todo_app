import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state['new_todo']
    todos.append(todo_to_add)
    functions.save_todos(todos)


st.title("My TODO App")
st.subheader("This is my todo app")
st.write("This app will increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a new TODO...", on_change=add_todo, key='new_todo')
st.session_state