#Imports
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
# use the non-interactive Agg backend to be more thread safe
#mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock
from matplotlib.animation import FuncAnimation

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

# adding pages
st.write("# Welcome to The Transit Trail!")
st.sidebar.success("Select a level above.")
    
# Define function for page 1
def page1():
    #Imports
    import streamlit as st
    import streamlit.components.v1 as components
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import time
    # use the non-interactive Agg backend to be more thread safe
    #mpl.use("agg")
    from matplotlib.backends.backend_agg import RendererAgg
    _lock = RendererAgg.lock
    from matplotlib.animation import FuncAnimation

    st.markdown("# Level One: Uncovering The Transit Method")
    st.sidebar.header("Level One")
    st.write("Level One: clear, smooth terrain with 10% chance of rain!")

    # Define section titles
    sectiontitles1 = ['Mission One', 'Mission Two', 'Level One Questions']

    # Define section titles
    def sectiontitle(number):
        return "{0}: {1}".format(number, sectiontitles1[number-1])

    # Define section
    section1 = st.radio('Select mission:', [1,2,3], format_func=sectiontitle)

    # Write section headers
    st.markdown("## {}".format(sectiontitle(section1)))

    if section1==1:
        # Add text
        st.write("The transit method is a way astronomers detect exoplanets, which are planets outside of our solar system.")
        # Add an image title
        #st.title('K2-18 b')
        # Add an image from local file
        #st.image('C:\Users\elena\Pictures\Desktop background\Exoplanet_K2-18_b_(Illustration).jpg', caption='The above image is an illustration of an exoplanet Kb-18 b! The red sphere is the cool dwarf star that it orbits around called K2-18. Illustration: NASA, CSA, ESA, J. Olmsted (STScI), Science: N. Madhusudhan (Cambridge University)')
        # Define Question 1.1.1 and options

    if section1==2:
        # Add progress bar in sidebar
        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empt
        
        # Parameters
        star_radius = 1.0
        planet_radius = 0.3
        orbit_radius = 3.0
        angular_velocity = 0.02
        frames = 400
        with _lock:
            # Create figure and subplots
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
            # Set up first subplot (edge-on view)
            ax1.set_aspect('equal')
            ax1.set_xlim(-5, 5)
            ax1.set_ylim(-5, 5)
            ax1.set_xlabel('X')
            ax1.set_ylabel('Y')
            ax1.set_title('Edge-On View')
            # Set up second subplot (birds-eye view)
            ax2.set_aspect('equal')
            ax2.set_xlim(-5, 5)
            ax2.set_ylim(-5, 5)
            ax2.set_xlabel('X')
            ax2.set_ylabel('Y')
            ax2.set_title('Above View')
            # Draw line segment representing the orbital plane (edge-on view)
            orbital_plane_edgeon, = ax1.plot([-orbit_radius, orbit_radius], [0, 0], linestyle='--', color='gray')
            ax1.annotate('Orbital Plane', xy=(2, 0), xytext=(2, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            # Draw circle segment representing the orbital plane (above view)
            theta = np.linspace(0, 2*np.pi, 100)
            orbital_plane_above, = ax2.plot(orbit_radius * np.cos(theta), orbit_radius * np.sin(theta), linestyle='--', color='gray')
            ax2.annotate('Orbital Plane', xy=(0, 3), xytext=(2, 4), arrowprops=dict(facecolor='black', arrowstyle='->'))
            # Draw the star and planet in both subplots
            star = ax1.add_patch(plt.Circle((0, 0), star_radius, color='yellow'))
            planet_edgeon = ax1.add_patch(plt.Circle((0, orbit_radius), planet_radius, color='blue'))
            star = ax2.add_patch(plt.Circle((0, 0), star_radius, color='yellow'))
            planet_above = ax2.add_patch(plt.Circle((0, orbit_radius), planet_radius, color='blue'))
            ax1.annotate('Star', xy=(-1, 0), xytext=(-1, -1.5))
            ax2.annotate('Star', xy=(0, 0), xytext=(0.5, -1.5))
            # Animation function
            def update(frame):
                angle = frame * angular_velocity
                # Update position of the planet in edge-on view
                x_edgeon, y_edgeon = orbit_radius * np.cos(angle), 0
                planet_edgeon.set_center((x_edgeon, y_edgeon))
                # Update position of the planet in above view
                x_above, y_above = orbit_radius * np.sin(angle), -orbit_radius * np.cos(angle)
                planet_above.set_center((x_above, y_above))
                # Check if the planet is behind the star in both views
                if np.pi/2 < angle % (2 * np.pi) < 3 * np.pi / 2:
                    planet_edgeon.set_alpha(0.2)
                    planet_above.set_alpha(0.2)
                else:
                    planet_edgeon.set_alpha(1.0)
                    planet_above.set_alpha(1.0)
                return planet_edgeon, planet_above,
            # Create animation
            ani = FuncAnimation(fig, update, frames=frames, blit=True)
            # Convert animation to HTML
            #Convert the animation to HTML format using to_jshtml() method of the FuncAnimation object.
            #html = ani.to_html5_video()
            # Display the animation in Streamlit
            components.html(ani.to_jshtml(), height=1000, width=3000)
        
        # Animation 
        progress_bar.empty() # clear elements by calling them empty

        st.markdown("The animation above shows a planet orbiting a star!")
        st.markdown("Imagine you're standing far away and watching a distant star. Now, if a planet passes in front of that star from your perspective, you will see a tiny shadow. This is the planet blocking some of the star's light! Have a look at the plot below of a planet going around a star.")
        st.markdown("Astronomers can detect this because they see a small dip in the star's brightness. By carefully observing these dips in brightness over time, astronomers can figure out if there might be a planet orbiting that star. They can also learn about the size of the planet, how long it takes to orbit its star, and sometimes even its atmosphere!")
        st.markdown("Ready to proceed to the next level? Answer the questions in the next section!")

        # Define Question 1.2.1 and options
        question1_2_1 = "What is a transit?"
        st.write(question1_2_1)
        options1_2_1 = ["The movement of stars across the sky during the night", "The passage of an exoplanet in front of its parent star", "The alignment of multiple planets in a solar system", "The change in brightness of a star caused by its rotation"]
        st.write(options1_2_1)
        # Display Question 1.2.1 and options
        selected_option1_2_1 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_1 == "1":
            st.write("Correct! A transit is the passage of an exoplanet in front of its parent star. :)")
        else:
            # Provide a hint
            if selected_option1_2_1 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_1 == "2":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_1 == "3":
                st.write("Try again! Re-read the Mission Two details.")

        # Define Question 1.2.2 and options
        question1_2_2 = "How does the transit method detect exoplanets?"
        st.write(question1_2_2)
        options1_2_2 = ["By measuring changes in the star's colour", "By observing fluctuations in the exoplanet's size", "By detecting dips in the star's brightness when an exoplanet passes in front of it", "By analysing the chnage in the star's temperature"]
        st.write(options1_2_2)
        # Display Question 1.2.2 and options
        selected_option1_2_2 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_2 == "2":
            st.write("Correct! The transit method detects exoplanets by detecting dips in the star's brightness when an exoplanet passes in front of it. :)")
        else:
            # Provide a hint
            if selected_option1_2_2 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_2 == "1":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_2 == "3":
                st.write("Try again! Re-read the Mission Two details.")

        # Define Question 1.2.3 and options
        question1_2_3 = "Why is it important for astronomers to observe multiple transits of an exoplanet?"
        st.write(question1_2_3)
        options1_2_3 = ["To determine the colour of the exoplanet", "To calculate the distance between the exoplanet and the star", "To confirm the presence of the exoplanet", "To estimate the exoplanet's composition"]
        st.write(options1_2_3)
        # Display Question 1.2.3 and options
        selected_option1_2_3 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_3 == "2":
            st.write("Correct! It is important for astronomers to observe multiple transits of an exoplanet so they can confirm the presence of the exoplanet. :)")
        else:
            # Provide a hint
            if selected_option1_2_3 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_3 == "1":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_3 == "3":
                st.write("Try again! Re-read the Mission Two details.")
        
        # Define Question 1.2.4 and options
        question1_2_4 = "Which of the following is a limitation of the transit method in detecting exoplanets?"
        st.write(question1_2_4)
        options1_2_4 = ["It can only detect large exoplanets", "It cannot detect exoplanets that are too far from their star", "It cannot detect exoplanets with irregular orbits", "It cannot detect exoplanets that are too close to their stars"]
        st.write(options1_2_4)
        # Display Question 1.2.4 and options
        selected_option1_2_4 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_4 == "3":
            st.write("Correct! A limitation of the transit method in detecting exoplanets is that it cannot detect exoplanets that are too close to their stars. :)")
        else:
            # Provide a hint
            if selected_option1_2_4 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_4 == "1":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_4 == "2":
                st.write("Try again! Re-read the Mission Two details.")
        
        st.markdown('You have found an exoplanet!')
        st.markdown('Congratulations, you have found an exoplanet! The transit method has been responsible for finding over 4000 exoplanets! But we are not done here! The transit method is very useful for finding many characterisitics of an exoplanet, including some that can even help find life!')
        
    if section1==3:
        question1_1_1 = "What is the transit method used for?"
        st.write(question1_1_1)
        options1_1_1 = ["Detecting exoplanets", "Detecting comets", "Studying asteroids", "Observing galaxies"]
        st.write(options1_1_1)
        # Display Question 1.1.1 and options
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

        # Define Question 1.2.1 and options
        question1_2_1 = "What is a transit?"
        st.write(question1_2_1)
        options1_2_1 = ["The movement of stars across the sky during the night", "The passage of an exoplanet in front of its parent star", "The alignment of multiple planets in a solar system", "The change in brightness of a star caused by its rotation"]
        st.write(options1_2_1)
        # Display Question 1.2.1 and options
        selected_option1_2_1 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_1 == "1":
            st.write("Correct! A transit is the passage of an exoplanet in front of its parent star. :)")
        else:
            # Provide a hint
            if selected_option1_2_1 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_1 == "2":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_1 == "3":
                st.write("Try again! Re-read the Mission Two details.")

        # Define Question 1.2.2 and options
        question1_2_2 = "How does the transit method detect exoplanets?"
        st.write(question1_2_2)
        options1_2_2 = ["By measuring changes in the star's colour", "By observing fluctuations in the exoplanet's size", "By detecting dips in the star's brightness when an exoplanet passes in front of it", "By analysing the chnage in the star's temperature"]
        st.write(options1_2_2)
        # Display Question 1.2.2 and options
        selected_option1_2_2 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_2 == "2":
            st.write("Correct! The transit method detects exoplanets by detecting dips in the star's brightness when an exoplanet passes in front of it. :)")
        else:
            # Provide a hint
            if selected_option1_2_2 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_2 == "1":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_2 == "3":
                st.write("Try again! Re-read the Mission Two details.")

        # Define Question 1.2.3 and options
        question1_2_3 = "Why is it important for astronomers to observe multiple transits of an exoplanet?"
        st.write(question1_2_3)
        options1_2_3 = ["To determine the colour of the exoplanet", "To calculate the distance between the exoplanet and the star", "To confirm the presence of the exoplanet", "To estimate the exoplanet's composition"]
        st.write(options1_2_3)
        # Display Question 1.2.3 and options
        selected_option1_2_3 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_3 == "2":
            st.write("Correct! It is important for astronomers to observe multiple transits of an exoplanet so they can confirm the presence of the exoplanet. :)")
        else:
            # Provide a hint
            if selected_option1_2_3 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_3 == "1":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_3 == "3":
                st.write("Try again! Re-read the Mission Two details.")
        
        # Define Question 1.2.4 and options
        question1_2_4 = "Which of the following is a limitation of the transit method in detecting exoplanets?"
        st.write(question1_2_4)
        options1_2_4 = ["It can only detect large exoplanets", "It cannot detect exoplanets that are too far from their star", "It cannot detect exoplanets with irregular orbits", "It cannot detect exoplanets that are too close to their stars"]
        st.write(options1_2_4)
        # Display Question 1.2.4 and options
        selected_option1_2_4 = st.text_input("Type the number (0-3) corresponding to your solution:")
        # Check the selected option
        if selected_option1_2_4 == "3":
            st.write("Correct! A limitation of the transit method in detecting exoplanets is that it cannot detect exoplanets that are too close to their stars. :)")
        else:
            # Provide a hint
            if selected_option1_2_4 == "0":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_4 == "1":
                st.write("Try again! Re-read the Mission Two details.")
            elif selected_option1_2_4 == "2":
                st.write("Try again! Re-read the Mission Two details.")

# Define function for page 2
def page2():
    st.write("This is page 2")
    # Add content specific to page 2
    #Imports
    import streamlit as st
    import streamlit.components.v1 as components
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import time
    # use the non-interactive Agg backend to be more thread safe
    #mpl.use("agg")
    from matplotlib.backends.backend_agg import RendererAgg
    _lock = RendererAgg.lock
    from matplotlib.animation import FuncAnimation

    st.markdown('# Level Two: Transit Curve Adventure')
    st.sidebar.header("Level Two")
    st.write('Level Two: Cloudy (with no chance of meatballs), rocky terrain and with 50% chance of rain!')

    # Define section titles
    sectiontitles2 = ['Mission One', 'Mission Two', 'Mission Three','Mission Four','Level Two Questions']

    # Define section titles
    def sectiontitle(number):
        return "{0}: {1}".format(number, sectiontitles2[number-1])

    # Define section
    section2 = st.radio('Select mission:', [1,2,3,4,5], format_func=sectiontitle)

    # Write section headers
    st.markdown("## {}".format(sectiontitle(section2)))

    if section2==1:
        # Add text
        st.write('When the planet moves in front of the star, the light of the star dims slightly for a short period of time. Think about when you put your hand in front of a torch and the light gets dimmer! Now, imagine this but the torch is the size of the Sun and your hand is the size of the Earth and both are thousands of kilometres away! This is very hard to see so astronomers have to use sensitive instruments that monitor the brightness of stars and analyse plots called transit light curves to see the dips in brightness. Have a look at the transit light curve of a real exoplanet called K2-18 b below!')

        #import PyTransit and some key modules.
        from pytransit import QuadraticModel
        # from pytransit import UniformModel
        from scipy.optimize import minimize
        import numpy as np
        import matplotlib.pyplot as plt
        from astropy import units as u
        from astropy import constants as const

        #enter the parameters needed by the model.
        rp18b = 14271000 #radius of K2-18 b in metres
        sma18b = 21380000000 #semi-major axis in metres
        rs18 = 0.41*696340000 #radius of K2-18 in metres
        t0_18b = 0.                        #time of inferior conjunction in days
        per18b = 32.9                     #orbital period in days
        rp_rs18b = rp18b/rs18              #planet radius (K2-18 b) / stellar radius ratio
        ars18b = sma18b/rs18                    #semi-major axis / stellar radius ratio
        inc18b =  (89.58*u.deg).to(u.rad).value      #orbital inclination (in radians) using astropy to convert to radians
        ecc18b = 0.09                       #eccentricity
        w18b = (-5.70*u.deg).to(u.rad).value      #longitude of periastron (in radians)
        gamma18b = [0.083, 0.191]                 #limb darkening coefficients [u1, u2]
        t = np.linspace(-0.1, 0.1, 1200)  #times at which to calculate light curve (days)

        rp391b = 1818041.56 #radius of planet (Kepler-391 b) in metres
        rp_rs391b = rp391b/rs18 # planet radius (Kepler-391 b) / stellar radius ratio

        rp132b = 7721136 #radius of planet (Kepler-132 b) in metres
        rp_rs132b = rp132b/rs18 # planet radius (Kepler-132 b) / stellar radius ratio

        rp116b = 21805060 #radius of planet (Kepler-116 b) in metres
        rp_rs116b = rp116b/rs18 # planet radius (Kepler-116 b) / stellar radius ratio

        tm = QuadraticModel() # a model that uses two limb-darkening coefficients
        tm.set_data(t)

        lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
        
        with _lock:
            fig_lc18b = plt.figure('lc18b')
            lc18b = plt.plot(t,lc18b, '-o', label='K2-18 b')
            plt.grid(True)
            plt.ylabel('Relative signal')
            plt.xlabel('Time (days)')
            plt.legend();
            plt.title('Transit Light Curve');
            st.pyplot(fig_lc18b);

    if section2==2:
        st.write('Play with the slider below to see how the radius can impact the transit curve in real time! What do you notice? Discuss with the person next to you!')

        # slider
        k = st.slider("Value for radius of planet over radius of star", 0.006, 0.8, 0.1)
        lc5  = tm.evaluate(k=k, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
        with _lock:
            fig_lc=plt.figure('lc')
            lc5 = plt.plot(t, lc5, '-o')
            plt.ylabel('Relative signal')
            plt.xlabel('Time (days)')
            plt.xlim(-0.1,0.1)
            plt.ylim(0.5,1.1)
            # Add minor ticks
            plt.minorticks_on()
            # Customise minor tick appearance
            plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
            st.pyplot(lc5)
