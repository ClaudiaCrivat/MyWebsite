from PIL import Image
import requests
import streamlit as st
import webbrowser
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title='My Webpage', page_icon=':smiley:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
with st.sidebar:
    selected = option_menu("Menu", ["About me", 'Education', 'Projects', 'Contact'],
    icons = ['person-circle', 'pencil', "folder", "envelope"])

#use localCSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css('style/style.css')

#---LOAD ASSETS---
lottie_coding = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_glp2wakj.json')
lottie_organize = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_duUhpb7PXY.json')
img_game = Image.open('images/TurtleGame.png')
profil_pic = Image.open('images/cropphoto.png')
GitHub = 'https://github.com/ClaudiaCrivat?tab=repositories'
Linkedin = 'https://www.linkedin.com/in/claudia-criv%C4%83%C8%9B-b119a5189/'
Instagram = 'https://www.instagram.com/claudiia97/'
logo_git = Image.open('images/25231.png')

if selected == "About me":
    # ----HEADER SECTION ----
    with st.container():
        st.subheader('Hi, I am Claudia :wave:')
        st.title('Student at the Python course')
    st.write('##')

    col1,col2, col3 = st.columns((2,2,1))
    with col1:
        st.image(profil_pic, width=250)
    with col2:
        st.title('Claudia Crivat')
        st.write('Passionate about finding way to use Python')
        st.write(':round_pushpin:','Bucuresti')
        st.write(':email:','claudia.crivat97@gmail.com')
        st.write(':telephone_receiver:','0742398933')

    #---SOCIAL LINKS---
    with col3:
        st.write('##')
        if st.button('GitHub'):
            webbrowser.open_new_tab(GitHub)
        st.write('##')
        if st.button('Linkedin'):
            webbrowser.open_new_tab(Linkedin)
        st.write('##')
        if st.button('Instagram') :
            webbrowser.open_new_tab(Instagram)

    # ----ABOUT ME ---
    with st.container():
        st.write('---')
        left_column, right_column = st.columns(2)
        with left_column:
            st.header('About me')
            st.write('##')
            st.write('I\'m 25 years old and I recently finished my master\'s degree in graphics and design at the Polytechnic University of Bucharest. '
                     'For the final project, I created a private plane interior in 3D. Due to the fact that I studied web design during my master\'s degree, I thought that I would like to do programming in the future.')
        with right_column:
            st_lottie(lottie_coding, height=300)

if selected == 'Education':
    #---EDUCATION---
    with st.container():
        st.title('Education')
        st.write('##')
        st.header('Polytechnic University of Bucharest')
        st.write('##')
        col1, col2 = st.columns((1, 2))
        with col1:
            st.write('Type of studies')
            st.write('Field of studies')
            st.write('Period of studies')
            st.write('Informations')
        with col2:
            st.write('Master\'s degree')
            st.write('Graphics and Design')
            st.write('2020-2022')
            st.write('During the master\'s program, I studied several 3D modeling programs, such as Autodesk Maya, 3dsMax, Inventie, Autocad. Also within this program, I also studied Web Design, where I acquired knowledge of html and css.'
                     'Dissertation work-"Modeling of closed spaces in a private aircraft."')
        st.write('##')
        st.write('---')
        st.header('Polytechnic University of Bucharest')
        st.write('##')
        col1, col2 = st.columns((1,2))
        with col1:
            st.write('Type of studies')
            st.write('Field of studies')
            st.write('Period of studies')
            st.write('Informations')
        with col2:
            st.write('Bachelor\'s degree')
            st.write('Economic Engineering')
            st.write('2016-2020')
            st.write('I graduated in Economic Engineering in the Chemical and Materials Industry, and I did my internship at Porsche Romania, for 9 weeks, in the Logistics department.'
                     'For the bachelor\'s thesis, I carried out a marketing research for a cosmetics company, and approached various marketing strategies to increase sales volume.')
        st.write('---')

        #--Foreign languages--
        st.header('Foreign languages')
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
        with col1:
            st.subheader('Language')
            st.write('##')
            st.write('-','English')
            st.write('-','French')
        with col2:
            st.subheader('Writing')
            st.write('##')
            st.write('Intermediate')
            st.write('Beginner')
        with col3:
            st.subheader('Reading')
            st.write('##')
            st.write('Advanced')
            st.write('Intermediate')
        with col4:
            st.subheader('Speaking')
            st.write('##')
            st.write('Intermediate')
            st.write('Beginner')
        st.write('---')

        # --It knowledge--
        with st.container():
            st.header('IT knowledge & Certificates')
            col1, col2 = st.columns((1, 1))
            with col1:
                st.subheader('IT knowledge')

            with col2:
                st.write('Microsoft Office-Word, Excel, PPT')
                st.write('Python-Intermediate')
                st.write('Wordpress-Intermediate')
                st.write('HTML-Beginner')
                st.write('3ds Max-Intermediate')
                st.write('Autodesk Maya-Intermediate')
        st.write('##')
        with st.container():
            col1, col2 = st.columns((1, 1))
            with col1:
                st.subheader('Certificates')
            with col2:
                st.write('DELF-B1')

if selected == 'Projects':
    #---Project---
    with st.container():
        st.title('My projects')
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_game)
        with text_column:
            st.subheader('Turtle Game')
            st.write('In this game, the turtle must pass through the colored "cars" without being touched. '
                     'So, you will move to the next level, and the cars will have a higher speed. '
                     'If the turtle is hit by a car, the game stops and game over will appear on the screen')
            st.write('##')
            st.markdown("Link GitHub -> (https://github.com/ClaudiaCrivat/Game)")
    st.write('##')
    st.write('##')
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(lottie_organize, height=300)
        with text_column:
            st.subheader('Automation project in Python')
            st.write('In this project, I created an automation with python to organize the files in a certain folder.')
            st.write('##')
            st.markdown("Link GitHub -> (https://github.com/ClaudiaCrivat/File_organizer)")
if selected == 'Contact':
    #---CONTACT--
    with st.container():
        st.title('Get In Touch With Me!')
        st.write('##')

        contact_form = """
        <form action="https://formsubmit.co/claudia.crivat@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">   
             <input type="text" name="name" placeholder = 'Your name' required>
             <input type="email" name="email" placeholder = 'Your email' required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()