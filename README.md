![](https://img.shields.io/github/followers/alokthakur93?label=Follow%40alokthakur93&style=social)
![](https://img.shields.io/github/forks/alokthakur93/Forecasting-CO2-emission?label=Fork&style=social)
![](https://img.shields.io/github/stars/alokthakur93/Forecasting-CO2-emission?style=social)
![](https://img.shields.io/github/watchers/alokthakur93/Forecasting-CO2-emission?style=social)
![](https://img.shields.io/github/issues/alokthakur93/Forecasting-CO2-emission)
![](https://img.shields.io/github/repo-size/alokthakur93/Forecasting-CO2-emission)
![](https://img.shields.io/github/languages/code-size/alokthakur93/Forecasting-CO2-emission)

# Forecasting Carbon Dioxide Emission level

## Project Overview:
* Designed a Forecasting model which forecasts CO2 emission levels, taking number of years you want to forecast as input.
* Analyzed time series for stationary and used different transformation.
* Implemented different forecasting model like ARIMA, Smoothing techniques like Holt - winter's method etc.
* Compared different model based on MAPE value which were built both on stationary and non - stationary data.
* Deployed model using Streamlit.
* Please visit the PPT provided in this repository for in-depth understanding.

## How to run ?
1. Download this project folder.
2. Open Anaconda prompt in root project directory and run this command:
    ``` streamlit run TS.py ```
3. After opening of browser, Upload CO2_dataset.csv provided in the folder.
4. Enter the number of years you want to forecast and press enter.

![](https://raw.githubusercontent.com/alokthakur93/Forecasting-CO2-emission/main/Screenshot%20(111).png)

## Business Problem / Objective:
To forecast the Carbon Dioxide emission levels for an industry so as the emission levels are within the standard limit, so that the organization can follow the government norms with respect to Carbon Dioxide emission levels.

## Dataset details:
Got dataset from Gap Minder.

## Exploratory Data Analysis:
* Visualized time series data and found data to be non - stationary. Done ADFuller test to cross - check whether data is stationary or not.
* Transformed data to stationary using differencing and decomposing.

## Model Building:
* Done data partition of time series keeping in view that order of must not be disturbed.
* Implemented different forecasting models on both stationary and non - stationary data.

![](https://raw.githubusercontent.com/alokthakur93/Forecasting-CO2-emission/main/graph.PNG)

## Model evaluation and comparison:
* Compared all the models build on basis of MAPE values.
![](https://raw.githubusercontent.com/alokthakur93/Forecasting-CO2-emission/main/Picture1.png)
* ARIMA(3,1,4) gave best results so chosen it as final model.
* Trained model using full dataset and used this model for deployment.

