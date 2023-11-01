# Python libraries
import streamlit as st
from PIL import Image
from recommender import song_recommender

def main():

    #############
    # Main page #
    #############
    
     ######## Selecting what is going to be in our app menu ########

    options = ['Song Recommender']


    
    st.markdown("<h1 style='text-align: center; color: Black;'>Song Recommender</h1>", unsafe_allow_html=True) 
    st.markdown("<h3 style='text-align: center; color: Gray;'>We'll recommend a similar song, based on the one you input!</h3>", unsafe_allow_html=True) 
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/spot.png")
        

    with col2 and col3:

        if st.checkbox('Proceed'):
            x = st.text_input("Name Of Song")
            y = st.text_input("Name Of Artist")
    
    
    if st.button("Search"):
        song_recommender(x,y)
main()