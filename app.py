import streamlit as st
import datetime
import requests

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Taxi Fare Predictor", page_icon="🚕")

st.title("🚕 NYC Taxi Fare Predictor")
st.write("Configure your ride parameters below and get an instant prediction!")

# --- RIDE PARAMETERS CARD ---
with st.container():
    st.subheader("🗓️ Ride Parameters")
    st.markdown("---")

    col1, col2 = st.columns(2)

    # LEFT COLUMN
    with col1:
        pickup_date = st.date_input("📅 Pickup date")
        pickup_time = st.time_input("⏰ Pickup time")
        pickup_longitude = st.number_input("📍 Pickup longitude", value=-73.985428)
        dropoff_longitude = st.number_input("🏁 Dropoff longitude", value=-73.985428)

    # RIGHT COLUMN
    with col2:
        pickup_latitude = st.number_input("📍 Pickup latitude", value=40.748817)
        dropoff_latitude = st.number_input("🏁 Dropoff latitude", value=40.748817)
        passenger_count = st.slider("👥 Passengers", 1, 8, 1)

datetime_pickup = datetime.datetime.combine(pickup_date, pickup_time)

# --- MINI MAP ---
st.subheader("🗺️ Ride Visualization")
st.caption("Pickup and dropoff points previewed on the map")
st.map(
    {
        "lat": [pickup_latitude, dropoff_latitude],
        "lon": [pickup_longitude, dropoff_longitude],
    }
)

# --- API SECTION ---
st.markdown("## 🔮 Fare Prediction")
st.write("We will now call the **TaxiFare API** to get your ride price.")

api_url = "https://taxifare.lewagon.ai/predict"

st.info("💡 Tip: Replace the API URL with your own if you deployed one!")

params = {
    "pickup_datetime": datetime_pickup.isoformat(),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
}

# --- PREDICT BUTTON ---
if st.button("🚀 Predict fare"):
    try:
        with st.spinner("Contacting the taxi gods… please wait 🔮"):
            response = requests.get(api_url, params=params)
            result = response.json()

        fare = result.get("fare", None)

        if fare is not None:
            st.success(f"💵 **Estimated Fare: ${fare:.2f}**")
            st.snow()
        else:
            st.error("❌ No fare returned by the API. Check parameters or API URL.")

    except Exception as e:
        st.error(f"⚠️ API call failed: {e}")
