import streamlit as st


def page_color():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-color: #163452;
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
                padding: 0px 24px;
                font-size: 15px;
                height: 50px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                transition: background-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
            }
            .stButton > button:hover {
                color: white;
                background-color: #3CB371;
                transform: translateY(-2px);
                box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
            }
            .stButton > button:active {
                color: white;
                background-color: #257247;
                transform: translateY(0px);
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
            }
            div.stButton > button:focus:not(:active) {
                color: white;
                border: none;
            }
            div.stButton > button:focus-visible {
                outline: 2px solid #A8E6C1;
                outline-offset: 2px;
            }
            </style>
            """, unsafe_allow_html=True)
