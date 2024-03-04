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
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

# adding pages
st.markdown("# Level One: Uncovering The Transit Method")
st.sidebar.markdown("# Level One")
st.write("Level One: clear, smooth terrain with 10% chance of rain!")

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
    st.write("The transit method is a way astronomers detect exoplanets, which are planets outside of our solar system.")
    import streamlit as st
    # Add an image title
    #st.title('K2-18 b')
    # Add an image from local file
    #st.image('C:\Users\elena\Pictures\Desktop background\Exoplanet_K2-18_b_(Illustration).jpg', caption='The above image is an illustration of an exoplanet Kb-18 b! The red sphere is the cool dwarf star that it orbits around called K2-18. Illustration: NASA, CSA, ESA, J. Olmsted (STScI), Science: N. Madhusudhan (Cambridge University)')
    # Define the question and options
    question1_1_1 = "What is the transit method used for?"
    st.write(question1_1_1)
    options1_1_1 = ["Detecting exoplanets", "Detecting comets", "Studying asteroids", "Observing galaxies"]
    st.write(options1_1_1)
    # Display the question and options
    selected_option = st.text_input("Type the number (0-3) corresponding to your solution:")
    # Check the selected option
    if selected_option == "0":
        st.write("Correct! The transit method is used for detecting exoplanets. Mission One complete! Provide to your next Mission :)")
    else:
        # Provide a hint
        if selected_option == "1":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option == "2":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option == "3":
            st.write("Try again! Re-read the Mission One details.")

if section==2:
    # Parameters
    star_radius = 1.0
    planet_radius = 0.3
    orbit_radius = 3.0
    angular_velocity = 0.02
    frames = 400
    st.markdown("Imagine you're standing far away and watching a distant star. Now, if a planet passes in front of that star from your perspective, you will see a tiny shadow. This is the planet blocking some of the star's light! Have a look at the plot below of a planet going around a star.")
    st.markdown("Astronomers can detect this because they see a small dip in the star's brightness. By carefully observing these dips in brightness over time, astronomers can figure out if there might be a planet orbiting that star. They can also learn about the size of the planet, how long it takes to orbit its star, and sometimes even its atmosphere!")
    st.markdown("Ready to proceed to the next level? Answer the questions below!")
