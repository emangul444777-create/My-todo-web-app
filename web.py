import streamlit as st
import functions

todo_list = functions.get_todolist()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todo_list.append(todo)
    functions.write_todolist(todo_list)


st.title("My Todo App")
st.subheader("Todo to do")
st.write("Its for practice")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todolist(todo_list)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new todo...",on_change=add_todo, key="new_todo")
