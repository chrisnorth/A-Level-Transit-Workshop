#Imports
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# import PyTransit
import time
# use the non-interactive Agg backend to be more thread safe
#mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock
from matplotlib.animation import FuncAnimation

import pytransit_local as pytransitlocal
import pytransit

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')
# adding pages
st.write("# Welcome to The Transit Trail!")
st.sidebar.success("Select a level above.")

st.write('streamlit version',st.__version__)
st.write('pytransit local version',pytransitlocal.__version__,pytransitlocal.__file__)
st.write('pytransit local version',pytransit.__version__,pytransit.__file__)