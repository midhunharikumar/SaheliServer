import streamlit as st


from dbconnector import MongoConnector, Customer

import pandas

import requests
import json


#connection = MongoConnector('None')

url = "http://localhost:8000"


if st.sidebar.checkbox("View Customers"):

    users = requests.get(url + '/showcustomers/').json()

    st.write(pandas.DataFrame(users))


first_name = st.text_input("FirstName")

last_name = st.text_input("LastName")

address = st.text_input("Address")

pincode = st.text_input("pincode")

email = st.text_input("email")

cellphone = st.text_input("cellphone")


if st.button('Submit'):
    customer = Customer(first_name, last_name, address,
                        pincode, email, cellphone)
    # connection.add_customer(customer.serialize())
    requests.post(url + '/addcustomer/', data=json.dumps(customer.serialize()))
