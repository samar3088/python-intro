import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"]+"\n"
    todos.append(todo_local)
    functions.write_todos(todos)
    print(todo_local)

st.title("My TODO App")
st.subheader("This is my TODO app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        #st.session_state.pop(todo)

st.text_input(label="Enter a TODO", placeholder="Write the TODO to be added...",
              on_change=add_todo,
              key='new_todo')


st.session_state