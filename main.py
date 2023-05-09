import streamlit as st
import functions
import os

# check if the 'todos_test.txt' file exists
if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, 'w') as file:
        pass

# read the 'todos_test.txt' file
todos = functions.file_read()


def get_user_input():
    user_input = st.session_state['new_todo'].capitalize()
    if len(user_input) > 0:
        todos.append(user_input + "\n")
        functions.file_rewrite(todos)


# web GUI
st.title("The ToDo App")
st.text("This webapp allows to keep all your todos in one place.")
st.text("Simply type a todo you want to add below and press Enter to add it to the list.")
st.text("To delete a todo from the list, simply click its checkbox.")

# read todos and create checkboxes
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.file_rewrite(todos)
        st.experimental_rerun()

# add a new todo
st.text_input("Add a new todo:",
              placeholder="Enter a todo",
              help='Type a new todo and press Enter to add it to the list',
              key='new_todo',
              on_change=get_user_input)

# delete all todos
delete_all = st.button("Delete All ToDos",
                       key='delete_all',
                       help="Note: This can't be undone!")
if delete_all:
    todos = []
    functions.file_rewrite(todos)
    st.experimental_rerun()
