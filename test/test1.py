import streamlit as st

class TodoApp:
    def __init__(self):
        st.title("Todo App")
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        # Load tasks from a file or database
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        # Save tasks to a file or database
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
                st.write(task)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()

    def edit_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            self.save_tasks()

    def show_tasks(self):
        for task in self.tasks:
            if st.checkbox(task):
                self.remove_task(task)
                st.experimental_rerun()

    def show_interface(self):
        # self.show_tasks()

        st.sidebar.title("Add/Edit Task")
        task = st.sidebar.text_input("New Task", key="new_task")
        if task:
            self.add_task(task)
            st.experimental_rerun()

        old_task = st.sidebar.selectbox("Select Task to Edit", self.tasks)
        new_task = st.sidebar.text_input("Edit Task", value=old_task)
        if st.sidebar.button("Update Task"):
            self.edit_task(old_task, new_task)
            st.experimental_rerun()

def main():
    app = TodoApp()
    app.show_interface()

if __name__ == "__main__":
    main()
