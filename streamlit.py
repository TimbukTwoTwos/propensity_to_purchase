from catboost import CatBoostClassifier, Pool
import streamlit as st
import pandas as pd
import numpy as np
import pickle

#Loading up the Regression model we created

# Load the model from the JSON file
with open('catboost_model.json', 'rb') as file:
    model = pickle.load(file)

#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(state, totalOrderCount, thirtyDayOrderCount, ninetyDayOrderCount, oneEightyDayOrderCount, ThreeSixFiveDayOrderCount, countOfDogFood, countOfCatFood, daysSinceLastOrder, groupLoyaltyCustomer, countOfItemID, minBagSize, maxBagSize, avgBagSize, mostFrequentCategoryValue, mostFrequentSubCategoryValue, daysBetweenOrderAVG, daysBetweenOrderSTD, averageRevenue, latestTransactionRevenue):
    prediction = model.predict(pd.DataFrame([[state, totalOrderCount, thirtyDayOrderCount, ninetyDayOrderCount, oneEightyDayOrderCount, ThreeSixFiveDayOrderCount, countOfDogFood, countOfCatFood, daysSinceLastOrder, groupLoyaltyCustomer, countOfItemID, minBagSize, maxBagSize, avgBagSize, mostFrequentCategoryValue, mostFrequentSubCategoryValue,
           daysBetweenOrderAVG, daysBetweenOrderSTD, averageRevenue, latestTransactionRevenue]], columns=['State', 'totalOrderCount', '30DayOrderCount', '90DayOrderCount', '180DayOrderCount', '365DayOrderCount', 'countOfDogFood', 'countOfCatFood', 'daysSinceLastOrder', 'groupLoyaltyCustomer', 'countOfItemID', 'minBagSize', 'maxBagSize', 'avgBagSize', 'mostFrequentCategoryValue', 'mostFrequentSubCategoryValue',
           'daysBetweenOrderAVG', 'daysBetweenOrderSTD', 'averageRevenue', 'latestTransactionRevenue']))
    return prediction


st.title('Retail Propensity to Purchase')
st.header('Enter the feature values of the customer:')
state = st.selectbox('State:', ['NSW', 'QLD', 'VIC', 'WA', 'SA', 'NT', 'ACT', 'TAS'])
totalOrderCount = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)
thirtyDayOrderCount = st.number_input('30 Day Order Count:', min_value=0.1, max_value=100.0, value=1.0)
ninetyDayOrderCount = st.number_input('90 Day Order Count:', min_value=0.1, max_value=100.0, value=1.0)
oneEightyDayOrderCount = st.number_input('180 Day Order Count:', min_value=0.1, max_value=100.0, value=1.0)
ThreeSixFiveDayOrderCount = st.number_input('365 Day Order Count:', min_value=0.1, max_value=100.0, value=1.0)
countOfDogFood = st.number_input('Count of Dog Food Orders:', min_value=0.1, max_value=100.0, value=1.0)
countOfCatFood = st.number_input('Count of Cat Food Orders:', min_value=0.1, max_value=100.0, value=1.0)
daysSinceLastOrder = st.number_input('Days since last order:', min_value=0.1, max_value=100.0, value=1.0)
groupLoyaltyCustomer = st.selectbox('Group Loyalty Customer:', [1,0])


if st.button('Predict'):
    price = predict(state, totalOrderCount, thirtyDayOrderCount, ninetyDayOrderCount, oneEightyDayOrderCount, ThreeSixFiveDayOrderCount, countOfDogFood, countOfCatFood, daysSinceLastOrder, groupLoyaltyCustomer, countOfItemID, minBagSize, maxBagSize, avgBagSize, mostFrequentCategoryValue, mostFrequentSubCategoryValue, daysBetweenOrderAVG, daysBetweenOrderSTD, averageRevenue, latestTransactionRevenue)
    st.success(f'The predicted price of the diamond is ${price[0]:.2f} USD')
