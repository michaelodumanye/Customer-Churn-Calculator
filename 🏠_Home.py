#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title ='Home Page',
    page_icon ='🏠',
    layout="wide"
)

st.title("RetentionRadar: Churn Insights, Retention Loyalty ✂️")


mp4_video_url= "./Assets/customer_retention.mp4"

# Embed the MP4 video in the Streamlit app
# st.video(mp4_video_url, format="video/mp4", start_time=0)


#intro talking about title 
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.title("Who We Are")
        st.write("##### We are a group of experienced Data Scientists who empower organizations with data-driven strategies for sustainable growth⭐⭐⭐⭐⭐")
        st.markdown("""
                    ###### Our group of experts in the team operate with the following objectives:

                    - ######  Focused on helping businesses enhance customer loyalty and reduce turnover.
                    - ###### Enabling proactive measures to maintain a loyal customer base.
                    - ######  Committed to driving your business success through improved retention rates.""")
    with col2:
        st.video(mp4_video_url, format="video/mp4", start_time=0, loop= True,  autoplay= True)
     

    col1,col2 = st.columns(2)
    with col1:
        st.header("Key Features")
        st.write("""
                    - View Data - Allows you to view data 
                    - Predict - Feature that allows to make single prediction or predict your csv data in bulk
                    - View History - Allows you to view the history of your predictions
                    - Dashboard - View data visualizations
                    """)
        
    with col2:
        st.header("User Benefits")
        st.write("""
                    - Make data driven decisions effortlessly
                    - User-Friendly Interface
                    - Real-Time predictions
                    - Insightful dashboards
                    - Ease to use
                    """)
        
    col1,col2 = st.columns(2)
    with col1:
        st.header("Machine Learning Integration")
        st.write("""
                - You have access three trained machine learning models
                - Simple integration and user-friendly access
                - Save data to local database or locally for future use
                - Get probability of predictions
                """)
    with col2:
        st.header("How To Run Applicattion")
        code = '''
        #Activate Virtual Environment
        source venv/bin/activate

        #Install dependencies
        pip install -r requirements.txt

        #Run the application
        streamlit run app.py
        '''
        st.code(code,language="python")
        

with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Contact Me")
        st.write("""
                 contact me at parockson@gmail.com for collaborations © 2024. All rights reserved    
        """)
        col3,col4 = st.columns(2)
        with col3:
            st.markdown(f'<a href="https://github.com/parockson" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">GitHub</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://www.linkedin.com/in/prince-acquah-rockson" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">LinkedIn</button></a>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<a href="https://medium.com/parockson" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">Medium</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="princerockson.netlify.app" target="_blank"><button style="background-color:Red; border:none; border-radius: 5px;">Website</button></a>', unsafe_allow_html=True)
    with col2:
        st.header("Explore")
        st.write("With our powerful machine learning algorithms, you could also try to predict whether a customer will churn or not with you own dataset!")
        data_button = st.button("Predict Here",key="make_prediction")
        if data_button:
            switch_page("Bulk_Predict")  
        
        
        