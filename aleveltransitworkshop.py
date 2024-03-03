#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
# use the non-interactive Agg backend to be more thread safe
#mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

# adding pages
st.markdown("# Level One: Uncovering The Transit Method")
st.sidebar.markdown("# Level One")

# Define section titles
sectiontitles = ['Mission One', 'Mission Two']

# Define section titles
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles[number-1])

# Define section
section = st.radio('Select mission:', [1,2], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section)))

if section==1:
    # Add text
    st.write("Level One: clear, smooth terrain with 10% chance of rain!")
    st.write("The transit method is a way astronomers detect exoplanets, which are planets outside of our solar system.")
    import streamlit as st
    # Add an image title
    #st.title('K2-18 b')
    # Add an image from local file
    #st.image('C:\Users\elena\Pictures\Desktop background\Exoplanet_K2-18_b_(Illustration).jpg', caption='The above image is an illustration of an exoplanet Kb-18 b! The red sphere is the cool dwarf star that it orbits around called K2-18. Illustration: NASA, CSA, ESA, J. Olmsted (STScI), Science: N. Madhusudhan (Cambridge University)')
    # Define the question and options
    question1_1_1 = "What is the transit method used for?"
    st.write(question1_1_1)
    options1_1_1 = ["A) Detecting exoplanets", "B) Detecting comets", "C) Studying asteroids", "D) Observing galaxies"]
    st.write(options1_1_1)
    # Display the question and options
    selected_option = st.text_input("Type the letter corresponding to your solution:")
    # Check the selected option
    if selected_option == "A":
        st.write("Correct! The transit method is used for detecting exoplanets. Mission One complete!")
    else:
        # Provide a hint
        if selected_option == "B":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option == "C":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option == "D":
            st.write("Try again! Re-read the Mission One details.")

