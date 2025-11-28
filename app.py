import streamlit as st
import datetime
import requests

st.subheader("🗓️ Choose your ride parameters")

pickup_date = st.date_input("📅 Pickup date")
pickup_time = st.time_input("⏰ Pickup time")
datetime_pickup = datetime.datetime.combine(pickup_date, pickup_time)

pickup_longitude = st.number_input("📍 Pickup longitude", value=-73.985428)
pickup_latitude = st.number_input("📍 Pickup latitude", value=40.748817)

dropoff_longitude = st.number_input("🏁 Dropoff longitude", value=-73.985428)
dropoff_latitude = st.number_input("🏁 Dropoff latitude", value=40.748817)

passenger_count = st.slider("👥 Passengers", min_value=1, max_value=8, value=1)

st.map({
    "lat": [pickup_latitude, dropoff_latitude],
    "lon": [pickup_longitude, dropoff_longitude]
})


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
