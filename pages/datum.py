import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title='Datum test',
    page_icon='👤',
    layout='wide'

)


st.title ('Datum Test 👤') 


# @st.cache_resource(show_spinner='connecting to database ...')
# def init_connection():
#     return pyodbc.connect(
#         "DRIVER = {SQL Server}; SERVER="
#         + st.secrets["ServerName"]
#         + ";DATABASE="
#         + st.secrets["DB_Name"]
#         + " ;UID="
#         + st.secrets["DB_User"]
#         + " ;PWD="
#         + st.secrets["DB_PWD"]
#     )


# connection = init_connection()

# @st.cache_data(show_spinner='running_query ...')
# def running_query(query):
#     with connection.cursor() as c:
#         c.execute(query)
#         rows = c.fetchall()
#         st.write(c.description)
#         pd.DataFrame.from_records(rows, columns=c.description)


#     return rows

# sql_query = " SELECT * FROM dbo.LP2_Telco_churn_first_3000 "

# rows = running_query(sql_query)

# Define a function to initialize the database connection
@st.cache_resource(show_spinner='Connecting to database ...')
def init_connection():
    connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=" + st.secrets["ServerName"] + ";"
        "DATABASE=" + st.secrets["DB_Name"] + ";"
        "UID=" + st.secrets["DB_User"] + ";"
        "PWD=" + st.secrets["DB_PWD"]
    )
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Establish the database connection
connection = init_connection()

# Function to execute queries and cache the results
@st.cache_data(show_spinner='Running query ...')
def running_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]  # Extract column names
        st.write(columns)  # Display column names
        return pd.DataFrame.from_records(rows, columns=columns)

# Example SQL query
sql_query = "SELECT * FROM dbo.LP2_Telco_churn_second_2000"

# Execute the query and display results
results = running_query(sql_query)
st.write(results)