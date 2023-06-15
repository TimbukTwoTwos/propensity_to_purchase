from catboost import CatBoostClassifier, Pool
import streamlit as st
import pandas as pd
import numpy as np

#Loading up the Regression model we created
model = CatBoostClassifier()
model.load_model('catboost_model.json')

#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(state, totalOrderCount, 30DayOrderCount, 90DayOrderCount, 180DayOrderCount, 365DayOrderCount, countOfDogFood, countOfCatFood, daysSinceLastOrder, groupLoyaltyCustomer, countOfItemID, minBagSize, maxBagSize, avgBagSize, mostFrequentCategoryValue, mostFrequentSubCategoryValue,
           daysBetweenOrderAVG, daysBetweenOrderSTD, averageRevenue, latestTransactionRevenue):
    prediction = model.predict(pd.DataFrame([[state, totalOrderCount, 30DayOrderCount, 90DayOrderCount, 180DayOrderCount, 365DayOrderCount, countOfDogFood, countOfCatFood, daysSinceLastOrder, groupLoyaltyCustomer, countOfItemID, minBagSize, maxBagSize, avgBagSize, mostFrequentCategoryValue, mostFrequentSubCategoryValue,
           daysBetweenOrderAVG, daysBetweenOrderSTD, averageRevenue, latestTransactionRevenue]], columns=['State', 'totalOrderCount', '30DayOrderCount', '90DayOrderCount', '180DayOrderCount', '365DayOrderCount', 'countOfDogFood', 'countOfCatFood', 'daysSinceLastOrder', 'groupLoyaltyCustomer', 'countOfItemID', 'minBagSize', 'maxBagSize', 'avgBagSize', 'mostFrequentCategoryValue', 'mostFrequentSubCategoryValue',
           'daysBetweenOrderAVG', 'daysBetweenOrderSTD', 'averageRevenue', 'latestTransactionRevenue']))
    return prediction


st.title('Retail Propensity to Purchase')
st.header('Enter the feature values of the customer:')
state = st.selectbox('State:', ['NSW', 'QLD', 'VIC', 'WA', 'SA', 'NT', 'ACT', 'TAS'])
totalOrderCount = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)
30DayOrderCount = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)
90DayOrderCount = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)
180DayOrderCount = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)
365DayOrderCount = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)
countOfDogFood = st.number_input('Total Order Counnt:', min_value=0.1, max_value=100.0, value=1.0)


if st.button('Predict'):
    price = predict(state, totalOrderCount, 30DayOrderCount, 90DayOrderCount, 180DayOrderCount, 365DayOrderCount, countOfDogFood, countOfCatFood, daysSinceLastOrder, groupLoyaltyCustomer, countOfItemID, minBagSize, maxBagSize, avgBagSize, mostFrequentCategoryValue, mostFrequentSubCategoryValue,
           daysBetweenOrderAVG, daysBetweenOrderSTD, averageRevenue, latestTransactionRevenue)
    st.success(f'The predicted price of the diamond is ${price[0]:.2f} USD')