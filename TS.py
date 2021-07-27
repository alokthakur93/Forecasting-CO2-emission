
# 1 --- first and foremost, we import the necessary libraries
import pandas as pd
import streamlit as st
import numpy as np
#import pickle
#import seaborn as sns
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset
from statsmodels.tsa.arima_model import ARIMAResults
import warnings
warnings.filterwarnings("ignore") # specify to ignore warning messages
#######################################

#fm = pickle.load(open("Forecast_arima.pkl", 'rb'))
data1=pd.read_csv('forecast_data_10years.csv')
data2=pd.read_csv('CO2 dataset.csv')

# 2 --- you can add some css to your Streamlit app to customize it
# TODO: Change values below and observer the changes in your app
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


# here is how to create containers
header_container = st.beta_container()
stats_container = st.beta_container()	
#######################################


# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container
#with header_container:
#def home():  

st.title("Forecast Co2 Levels  For An Organization")
st.header("Welcome!")
st.subheader("This is a Analyzing Forecast app")
st.write("Lets go")

st.write("IMPORT DATA")
st.write("CO2 dataset.csv")

data = st.file_uploader('',type='csv')
option = st.sidebar.selectbox(
         'Please select an option',
         ('','Show Data', 'Predicted Data'))
st.write('Displaying the DataFrame/Dashboard you have selected above')
if option:
    st.success('Yay! 🎉')
    st.write('You selected:', option)
    

    if option=='Show Data':
        #st.header('Review Data')
        st.table(data2.head(10))
    elif option=='Predicted Data':
	#st.header('Review Data')
        st.table(data1.head(10))
        
else:
    st.warning('No option is selected')

#fm = pickle.load(open("Forecast_arima.pkl", 'rb'))
#st.write("IMPORT DATA")
#st.write("CO2 dataset.csv")

#data = st.file_uploader('',type='csv')

if data is not None:
    #appdata = pd.read_csv(data)
    dateparse = lambda x: pd.to_datetime(x, format='%Y', errors = 'coerce')
    appdata = pd.read_csv(data, parse_dates=['Year'], index_col='Year', date_parser=dateparse) 
    
    st.write(data)
    
    #max_date = appdata['ds'].max()

st.write("SELECT FORECAST PERIOD")

periods_input = st.number_input('How many years forecast do you want?',
min_value = 1, max_value = 365)

if data is not None:
   # obj = Prophet()
   fm = ARIMA(appdata['CO2'],order = (3,1,4))
   fm = fm.fit()
   #fm.fit(appdata)


#st.write("The following plot shows future predicted values. 'yhat' is the predicted value; upper and lower limits are 80% confidence intervals by default")

if data is not None:
    #future = fm.make_future_dataframe(periods=periods_input)
    future=[appdata.index[-1]+ DateOffset(years=x)for x in range(0,periods_input)]
    future=pd.DataFrame(index=future[1:],columns=appdata.columns)
    end = len(appdata)+len(future)
    fcst = fm.predict(start = 215, end = end , dynamic= True)
    st.write("Below are the forecasted values")
    fcst
    st.write("VISUALIZE FORECASTED DATA")

    plt.plot(appdata, label='original')
    plt.plot(fcst, label='forecast')
    plt.title('Forecast')
    plt.legend(loc='upper left', fontsize=8)
    plt.show()
    #forecast = fcst[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    #forecast_filtered =  forecast[forecast['ds'] > max_date]    
    #st.write(forecast_filtered)



























   

