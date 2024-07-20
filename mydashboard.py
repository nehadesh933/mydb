import streamlit as st
import pandas as pd

# Check if 'plost' is available and import it
try:
    import plost
except ModuleNotFoundError:
    st.error("The 'plost' library is not installed. Please install it by running `pip install plost`.")

# Load data
seattle_weather = pd.read_csv('seattle_weather.csv', parse_dates=['date'])
stocks = pd.read_csv('sample_stocks.csv')

# Sidebar parameters
st.sidebar.header('Data Exploration Parameters')

# 1. Display metrics
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric('Temperature', '70 °F', '1.2 °F')  # label, value, change
col2.metric('Wind', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')

c1, c2 = st.columns(2)

# Heatmap
st.sidebar.markdown('### Heatmap')
hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max'))
with c1:
    st.markdown('### Heatmap')
    if 'plost' in globals():
        plost.time_hist(data=seattle_weather, date='date',
                        x_unit='week', y_unit='day', color=hist_color,
                        aggregate='mode', legend=None, width=450,
                        height=350, use_container_width=True)
    else:
        st.warning("The 'plost' library is not available for the heatmap.")

# Donut chart
st.sidebar.markdown('### Donut Chart')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))
with c2:
    st.markdown('### Donut Chart')
    if 'plost' in globals():
        plost.donut_chart(data=stocks, theta=donut_theta,
                          color='company', legend='top',
                          use_container_width=True)
    else:
        st.warning("The 'plost' library is not available for the donut chart.")

# Line plot
st.markdown('### Line Chart')
st.sidebar.markdown('### Line Chart')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
st.line_chart(seattle_weather.set_index('date')[plot_data])

# Footer
st.sidebar.markdown('---')
st.sidebar.markdown('Created by Neha & Rakshitha')
