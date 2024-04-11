import streamlit as st
import smtplib, ssl
import pandas as pd

def send_email(message):
    
    host="smtp.gmail.com"
    port=465
    username = "aliciamarchaves@gmail.com"
    password = "jrwi blqn ptjo dgzu"
    receiver = "aliciamarchaves@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

topics = pd.read_csv("venv/topics.csv")

host="smtp.gmail.com"
port=465

username = "aliciamarchaves@gmail.com"
password = "jrwi blqn ptjo dgzu"

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your e-mail address")
    option = st.selectbox(
        "What topic do you want to discuss?", topics["topic"]
    )
    raw_message = st.text_area("Your message")
    message = f"""\
        Subject: New email from {user_email}
        From: {user_email}
        {raw_message}
        """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
    