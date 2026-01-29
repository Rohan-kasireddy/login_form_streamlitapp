import streamlit as st
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan@123",
    database="my_db"
)
print("connection successful")
cursor=conn.cursor()
st.title("Registration App")
with st.form("registration_form"):
    name=st.text_input("name")
    email=st.text_input("email")
    password=st.text_input("password",type="password")
    submit=st.form_submit_button("register")
    if submit:
        insert_query="INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values=(name, email, password)
        cursor.execute(insert_query, values)
        conn.commit()
        st.success("registration successful")