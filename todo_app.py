import streamlit as st

# Page configuration
st.set_page_config(page_title="📝 To-Do List", layout="centered")

st.title("✅ To-Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
new_task = st.text_input("➕ Add a new task")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")
    else:
        st.warning("Please enter a valid task.")

# Display tasks
st.subheader("📋 Your Tasks")
if len(st.session_state.tasks) == 0:
    st.info("No tasks added yet.")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        checked = col1.checkbox("", value=task["done"], key=i)
        if checked != task["done"]:
            st.session_state.tasks[i]["done"] = checked
        task_text = f"~~{task['task']}~~" if checked else task['task']
        col2.markdown(task_text)

# Clear completed tasks
if st.button("🗑️ Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.success("Completed tasks removed.")
