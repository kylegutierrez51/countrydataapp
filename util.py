import streamlit as st


def page_color():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-color: #107AB0;
    opacity: 0.8;
    }
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def button_style():
    st.markdown("""
            <style>
            .stButton > button {
                background-color: #2E8B57; /*other options: #E18AAA; #107AB0*/
                color: white;
                border-radius: 5px;
                border: none;
                margin: 0px; 
                //padding: 10px 20px;
                font-size: 15px;
                width: 100%;
                height: 50px;
            }
            .stButton > button:hover {
                color: #d4d4d4;
                background-color: ##2E8B57;
            }
            div.stButton > button:focus {
                outline: none;
                background-color: #2E8B57;
                color: #d4d4d4;
            }
            </style>
            """, unsafe_allow_html=True)
