import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="my website",page_icon="udhs",layout="wide")
def load_lott(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

company=load_lott("https://assets3.lottiefiles.com/packages/lf20_x17ybolp.json")
Ai=load_lott("https://assets6.lottiefiles.com/packages/lf20_KXdLRdwnM5.json")
Data_loading=load_lott("https://assets5.lottiefiles.com/packages/lf20_49rdyysj.json")
graph=load_lott("https://assets7.lottiefiles.com/private_files/lf30_7zjif55a.json")

img_amnet=Image.open("images/amnet.png")
img_krishna=Image.open("images/krishna.png")


st.image(img_amnet,width=100)
with st.container():

    st.subheader("Welcome to Amnet Digital")
    st.title("Your satisfaction is our highest priority")

   

with st.container():
  
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("what do we do")
        st.write(
            """We solve your problems using cutting edge technology""")
        st.write(
            """Data is the fuel of the business
               We help you to get all the insights you want
               for the growth of your business from data.
               """)
       
    with right_column:
        st_lottie(company,height=300,key="data1")
with st.container():
    left_column,right_column=st.columns(2)
    with right_column:
        st.header("We are here to care your business")
        st.write(
            """
            The most important facter in business is compitition:
            Every business is growing in its own way with the data it Have.
            We care your business the most and give you the key insights such that you can take important decision
            
            """)
       
    with left_column:
        st_lottie(Data_loading,height=300,key="data")

with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("How we do it")
        st.write(
            """
            We would love to be transparent with our clients.
            We have data analysts, data engineers, data scientists working for you day-in and day-out.

            
            """)
       
    with right_column:
        st_lottie(graph,height=300,key="graph")



with st.container():
    st.write("---")
    st.header("GEt in touch with us")
    
    contact_form= """
    <form action="https://formsubmit.co/kamasanirohith@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css=("style/style.css")