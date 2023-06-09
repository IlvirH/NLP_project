import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://catherineasquithgallery.com/uploads/posts/2021-02/1614374202_41-p-fon-tekhnologii-svetlii-53.jpg");
background-size: 120%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://kartinkin.net/uploads/posts/2022-01/1643325727_14-kartinkin-net-p-pattern-neiroset-krasivie-16.jpg");
background-size: 115%;
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(1,1,1,1);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

div.css-1n76uvr.esravye0 {{
background-color: rgba(238, 238, 238, 0.5);
border: 10px solid #EEEEEE;
padding: 5% 5% 5% 10%;
border-radius: 5px;
}}



</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,8,1])
#col1, col2 = st.columns(2)

### Гистограмма total_bill
with col2:
# Веб-приложение с использованием Streamlit
    st.title(':blue[NLP project by team BERT]:male-technologist:')
col1, col2, col3 = st.columns([2,5,2])
#col1, col2 = st.columns(2)

### Гистограмма total_bill
with col2:
# Веб-приложение с использованием Streamlit
    
    # st.markdown("<div style='text-align: center; font-size: 35px;'**:gray[> Team members:"]**, unsafe_allow_html=True)
    # st.markdown("<div style='text-align: center; font-size: 28px;'> :gray[Vasily S.]", unsafe_allow_html=True)
    # st.markdown("<div style='text-align: center; font-size: 28px;'> :gray[Anna F.]", unsafe_allow_html=True)
    # st.markdown("<div style='text-align: center; font-size: 28px;'> :gray[Viktoria K.]", unsafe_allow_html=True)
    # st.markdown("<div style='text-align: center; font-size: 28px;'> :gray[Ivan N.]", unsafe_allow_html=True)
    # st.markdown("<div style='text-align: center; font-size: 28px;'> :gray[Ilvir Kh.]", unsafe_allow_html=True)

    st.header('**:grey[Team members:]**')
    st.subheader('**:violet[:cat:  Vasily S.]**')
    st.subheader('**:violet[:cat:  Anna F.]**')
    st.subheader('**:violet[:cat:  Viktoria K.]**')
    st.subheader('**:violet[:cat:  Ivan N.]**')
    st.subheader('**:violet[:cat:  Ilvir Kh.]**')

#st.sidebar.image

# Настройка боковой панели
st.sidebar.title("About the project")
st.sidebar.info(
    """
    Natural Language Processing
    """
)
st.sidebar.info("You can also find our repository on github "
                "[here](https://github.com/vasevooo/NLP_project).")