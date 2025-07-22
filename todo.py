import streamlit as st

st.title("✅ Simple To-Do List")

tasks = st.session_state.get("tasks", [])

new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task:
        tasks.append({"text": new_task, "done": False})
        st.session_state["tasks"] = tasks
        st.experimental_rerun()

if tasks:
    for i, task in enumerate(tasks):
        checked = st.checkbox(task["text"], value=task["done"], key=i)
        tasks[i]["done"] = checked
    st.session_state["tasks"] = tasks
