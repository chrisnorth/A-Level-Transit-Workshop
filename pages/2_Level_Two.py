#Imports
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
from pytransit import QuadraticModel
# use the non-interactive Agg backend to be more thread safe
mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
#mpl.use('TkAgg')
#_lock = RendererAgg.lock

#import PyTransit and some key modules.
from matplotlib.animation import FuncAnimation
# from pytransit import UniformModel
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy import constants as const

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

tm = QuadraticModel() # a model that uses two limb-darkening coefficients

if section2==1:
    # Add text
    st.write('When the planet moves in front of the star, the light of the star dims slightly for a short period of time. Think about when you put your hand in front of a torch and the light gets dimmer! Now, imagine this but the torch is the size of the Sun and your hand is the size of the Earth and both are thousands of kilometres away! This is very hard to see so astronomers have to use sensitive instruments that monitor the brightness of stars and analyse plots called transit light curves to see the dips in brightness. Have a look at the transit light curve of a real exoplanet called K2-18 b below!')

    

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
    
    #with _lock:
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
    tm = QuadraticModel() # a model that uses two limb-darkening coefficients
    t = np.linspace(-0.1, 0.1, 1200)
    tm.set_data(t)

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
    
    st.write('Look at the above slider plot in a different way')
    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    lc391b  = tm.evaluate(k=rp_rs391b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    lc132b  = tm.evaluate(k=rp_rs132b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    lc116b  = tm.evaluate(k=rp_rs116b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    with _lock:
        fig_lc = plt.figure('lc')
        lc391b = plt.plot(t,lc391b,'-o', label='Kepler-391 b')
        lc132b = plt.plot(t,lc132b,'-o', label='Kepler-132 b')
        lc18b = plt.plot(t,lc18b, '-o', label='K2-18 b')
        lc116b = plt.plot(t,lc116b,'-o', label='Kepler-116 b')
        plt.ylabel('Relative signal')
        plt.xlabel('Time (days)')
        plt.legend();
        plt.minorticks_on();
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray');
        st.pyplot(lc391b)
        st.pyplot(lc132b)
        st.pyplot(lc18b)
        st.pyplot(lc116b)
    t = np.linspace(0, 5, 1200)  #times at which to calculate light curve (days)

    k_txt = st.text_input(f"Enter a ratio of planet to star radius ")

    st.write("Hint: Keep your values between 0.1 and 1")

    # Plot the data
    with _lock:
        plt.figure(figsize=(8, 6))
        lc_k  = tm.evaluate(k=k_txt, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
        lc_k = plt.plot(t,lc_k, '-o')

        # Add labels and title
        plt.ylabel('Relative signal')
        plt.xlabel('Time (days)')
        plt.title('Your transit light curve!')

        # Show the plot
        plt.minorticks_on();
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray');
        st.pyplot(lc_k)
    
    st.write('From your plot, think about how you can calculate the time range of when the planet passes in front of the star.')

if section2==3:
    st.write('Different transit events can tell you how far away the planet is from the star! This is all due to perspective. For example, if you cover a light source with a shield that is right in front of the light source it will block a lot of light but if you place the shield very far from the light source it will only block some of the light. See this in action with the interactive plot below!')
    per = st.slider("Value for period", 1.0, 50.0, 5.)
    lc  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per, a=ars18b, i=inc18b)
    with _lock:
        fig = plt.figure('lc')
        lc_plt = plt.plot(t, lc, '-o')
        plt.ylabel('Relative signal')
        plt.xlabel('Time (days)')
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
        st.pyplot(lc_plt)

    st.write('Now, look at a static plot of planets with different orbital periods. Remember that period is the time taken for the exoplanet to complete one orbit around its host star!')
    lc83c  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=10.00102551, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #K2-83 c
    lc1h  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=20, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #TRAPPIST-1 h
    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #K2-18 b
    lc1260d  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=49.8251659648395, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #TOI-1260 d

    with _lock:
        fig = plt.figure('lc')

        lc83c = plt.plot(t,lc83c, '-o', label='K2-83 c') #K2-83 c
        lc1h = plt.plot(t,lc1h,'-o', label='TRAPPIST-1 h') #TRAPPIST-1 h
        lc18b = plt.plot(t,lc18b, '-o', label='K2-18 b') #K2-18 b
        lc1260 = plt.plot(t,lc1260d,'-o', label='TOI-1260 d') #TOI-1260 d
        plt.ylabel('Relative signal')
        plt.xlabel('Time (days)')
        plt.legend();
        plt.minorticks_on();
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray');
        st.pyplot(lc83c)
        st.pyplot(lc1h)
        st.pyplot(lc18b)
        st.pyplot(lc1260)

    # Initialise lists to store data
    x_values = []
    y_values = []

    p = st.text_input(f"Enter a value for the period ")

    st.write('Hint: Keep your values between 1 and 50')

    # Plot the data
    with _lock:
        fig = plt.figure(figsize=(8, 6))
        lc_p  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=p, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
        lc_p_plt = plt.plot(t,lc_p, '-o')
        # Add labels and title
        plt.ylabel('Relative signal')
        plt.xlabel('Time (days)')
        plt.title('Your transit light curve!')
        # Show the plot
        plt.minorticks_on();
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray');
        st.pyplot(lc_p_plt)

if section2==4:
    st.write('Astronomers love to find patterns and if you see that a dip in brightness happens regularly then you can start to predict when the next dip will occur because then you are most likely looking at the orbit of a planet!')
    tlong=np.linspace(0,5,10000)
    tm.set_data(tlong)

    per = st.slider('Values for the period', 1.0, 2.0, 0.01)

    lc  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per, a=ars18b*0.05, i=inc18b)
    with _lock:
        fig = plt.figure('lc')
        tlong_plt = plt.plot(tlong,lc, '-o')
        plt.xlim(0, 5)
        plt.ylim(0.997,1.001)
        plt.ylabel('Relative signal')
        plt.xlabel('Time (days)')
        # Add minor ticks
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
        st.pyplot(tlong_plt)
    
    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=2.00, a=ars18b*0.05, i=inc18b)
    with _lock:
        fig = plt.figure('lc')
        tlong_lc18b = plt.plot(tlong,lc18b, '-o')
        plt.xlim(0, 5)
        plt.ylim(0.9972,1.0001)
        plt.ylabel('Relative Flux')
        plt.xlabel('Time (days)')
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
        st.pyplot(tlong_lc18b)
    
if section2==5:
    question2_1_1 = "What do scientists look for to confirm the presence of an exoplanet using the transit method?"
    st.write(question2_1_1)
    options2_1_1=["Change in the star's colour", "Variations in the star's size", "Repeated dips in the star's brightness at regular intervals", "Fluctuations in the star's temperature"]
    st.write(options2_1_1)
     # Display Question 1.2.1 and options
    selected_option2_2_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_1_1')
    # Check the selected option
    if selected_option2_2_1 == "2":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_2_1 == "0":
            st.write("Try again!")
        elif selected_option2_2_1 == "1":
            st.write("Try again!")
        elif selected_option2_2_1 == "3":
            st.write("Try again!")

    question2_1_2 = "When does the planet pass in front of the star?"
    options2_1_2=["Between -0.100 and -0.075 days", "Between -0.075 and 0.075 days", "Between 0.075 and 0.100 days", "None of the above"]
    st.write(question2_1_2)
    st.write(options2_1_2)
     # Display Question 2.2.1 and options
    selected_option2_2_2 = st.text_input("Type the number (0-3) corresponding to your solution:")
    # Check the selected option
    if selected_option2_2_2 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_2_2 == "0":
            st.write("Try again!")
        elif selected_option2_2_2 == "2":
            st.write("Try again!")
        elif selected_option2_2_2 == "3":
            st.write("Try again!")


    question2_1_3 = "What happens to a star's light during a transit caused by an exoplanet?"
    options2_1_3=["It brightens", "It remains constant", "It dims slightly", "It disappears completely"]
    st.write(question2_1_3)
    st.write(options2_1_3)    
    selected_option2_2_3 = st.text_input("Type the number (0-3) corresponding to your solution:")
    # Check the selected option
    if selected_option2_2_3 == "1":
        st.write("Correct!  :)")
    else:
        # Provide a hint
        if selected_option2_2_3 == "0":
            st.write("Try again!")
        elif selected_option2_2_3 == "2":
            st.write("Try again!")
        elif selected_option2_2_3 == "3":
            st.write("Try again!")


    question2_1_4 ="Why does the brightness of a star decrease during a transit?"
    options2_1_4=["Due to the presence of sunspots on the star's surface", "Because the exoplanet blocks a portion of the star's light as it passes in front of it", "As a result of an error in the data", "Because of fluctuations in the star's internal temperature"]
    st.write(question2_1_4)
    st.write(options2_1_4)
    selected_option2_1_4 = st.text_input("Type the number (0-3) corresponding to your solution:")
    # Check the selected option
    if selected_option2_1_4 == "1":
        st.write("Correct!  :)")
    else:
        # Provide a hint
        if selected_option2_1_4 == "0":
            st.write("Try again!")
        elif selected_option2_1_4 == "2":
            st.write("Try again!")
        elif selected_option2_1_4 == "3":
            st.write("Try again!")


    question2_1_5 = "What is represented by the slopes in the transit light curve?"
    options2_1_5=["Velocity of the exoplanet", "Change in brightness over time", "Atmospheric density of the exoplanet", "None of the above"]
    st.write(question2_1_5)
    st.write(options2_1_5)
    selected_option2_1_5 = st.text_input("Type the number (0-3) corresponding to your solution:")
    # Check the selected option
    if selected_option2_1_5 == "1":
        st.write("Correct!  :)")
    else:
        # Provide a hint
        if selected_option2_1_5 == "0":
            st.write("Try again!")
        elif selected_option2_1_5 == "2":
            st.write("Try again!")
        elif selected_option2_1_5 == "3":
            st.write("Try again!")

    
