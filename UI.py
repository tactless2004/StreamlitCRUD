import streamlit as st
from documentHolder import DocumentHolder
import pandas as pd

def Insert(insertion):
    st.session_state['db'].insert(insertion)
    st.text("Inserted \'" +insertion +"\'")

def Read(id):
    record = st.session_state['db'].read(int(id))
    st.text(record)

def ListAll():
    ids=[]
    messages=[]
    for id in st.session_state['db'].documents.keys():
        ids.append(st.session_state['db'].documents[id][0])
        messages.append(st.session_state['db'].documents[id][1])

    df = pd.DataFrame({"ID": ids, "Records":messages},index=None)
    st.dataframe(df,hide_index=True, width=600)

def Delete(id):
    st.session_state['db'].delete(id)

def Update(id, message):
    st.session_state['db'].update(id, message)

if 'db' not in st.session_state:
    st.session_state['db'] = DocumentHolder()

st.title("Simple Streamlit CRUD App")
st.text("Developed by Leyton McKinney")
col1,col2 = st.columns(2)
options = ["Insert", "Read", "Update", "Delete", "View"]
operation = st.selectbox(label="Operation",options=options, placeholder="Choose an Operation")

if operation == "Insert":
    col1.header("Insert")
    InsertionInput = st.text_input("Insert a record", value=None)
    if st.button("Insert"):
        if InsertionInput is None:
            st.text("Record cannot be empty!")
        else:
            Insert(InsertionInput)

elif operation == "Read":
    col1.header("Read")
    ReadID = st.text_input("Read a record", value=None)
    if st.button("Read"):
        Read(ReadID)


elif operation == "Update":
    col1.header("Update")
    id = st.text_input("ID")
    message = st.text_input("New Record")
    # God's longest if statement
    # 1. has the button been pressed
    # 2. Is the id not null
    # 3. Is the id a digit string, no "Lorem Ipsum" id's those aren't valid
    # 4. Is the id in the current db
    if st.button("Update") and id is not None and id != "" and id.isdigit() and int(id) in st.session_state['db'].documents:
        Update(id, message)
    ListAll()


elif operation == "Delete":
    col1.header("Delete")
    id = st.text_input("ID to Delete")
    if st.button("Delete") and id is not None and id != "" and id.isdigit() and int(id) in st.session_state['db'].documents:
        Delete(id)
    ListAll()

elif operation == "View":
    ListAll()

else:
    print("Shouldn't have gotten here. LGM")

# col1.header("Original")
# col2.header("Original")