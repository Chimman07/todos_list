import streamlit as st
from functions import read_data, write_data

st.header('My-Task List')
st.subheader('this is the task app')
st.write('you can add your all tasks and delete the completed one too')

tasks = read_data()


def add_task():
    new_task = st.session_state['new_task']
    tasks.append(new_task + '\n')
    write_data(tasks)


for i, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(i)
        write_data(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="", placeholder='Write task Here...', key='new_task', on_change=add_task)

