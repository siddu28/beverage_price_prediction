import streamlit as st
from prediction_helper import predict

def main():

    st.markdown(
    """
    <style>
    div[data-baseweb="select"] > div {
        height: 40px; 
        font-size: 16px;
        width: 100%; /* Increase width of select boxes */
    }
    input[type="number"] {
        height: 50px; 
        font-size: 16px; 
        width: 100%; /* Increase width of number input */
    }
    .stTextInput>div>div>input {
        width: 100%; /* Increase width of text input */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.title("CodeX Beverage: Price Prediction")

    row1 = st.columns(4)
    with row1[0]:
        age = st.number_input("Age", min_value=1, max_value=100, step=1, value=30, key="age")
    with row1[1]:
        gender = st.selectbox("Gender", ["M", "F"], key="gender")
    with row1[2]:
        zone = st.selectbox("Zone", ['urban', 'metro', 'rural', 'semi-urban'], key="zone")
    with row1[3]:
        occupation = st.selectbox("Occupation", ['Working Professional','Student','Entrepreneur','Retired'], key="occupation")

    row2 = st.columns(4)
    with row2[0]:
        income_level = st.selectbox("Income Level (In L)", ['<10L', '> 35L', '16L - 25L', 'Not Reported', '10L - 15L','26L - 35L'], key="income")
    with row2[1]:
        consume_frequency = st.selectbox("Consume Frequency (weekly)", ['3-4 times', '5-7 times', '0-2 times'], key="consume")
    with row2[2]:
        current_brand = st.selectbox("Current Brand", ['newcomer','established'], key="brand")
    with row2[3]:
        consumption_size = st.selectbox("Preferable Consumption Size", ['Medium (500 ml)','Large (1 L)','Small (250 ml)'], key="size")

    row3 = st.columns(4)
    with row3[0]:
        brand_awareness = st.selectbox("Awareness of other brands", ['0 to 1', '2 to 4', 'above 4'], key="awareness")
    with row3[1]:
        reason_for_choice = st.selectbox("Reasons for choosing brands", ['Price','Quality','Availability','Brand Reputation'], key="reason")
    with row3[2]:
        flavor_preference = st.selectbox("Flavor Preference", ['Traditional','Exotic'], key="flavor")
    with row3[3]:
        purchase_channel = st.selectbox("Purchase Channel", ['Online','Retail Store'], key="channel")

    row4 = st.columns(3)
    with row4[0]:
        packaging_preference = st.selectbox("Packaging Preference", ['Simple','Premium','Eco-Friendly'], key="packaging")
    with row4[1]:
        health_concerns = st.selectbox("Health Concerns", ['Medium (Moderately health-conscious)','Low (Not very concerned)','High (Very health-conscious)'], key="health")
    with row4[2]:
        consumption_situation = st.selectbox(
            "Typical Consumption Situations",
            ['Active (eg. Sports, gym)','Social (eg. Parties)','Casual (eg. At home)'],
            key="situation"
        )

    st.markdown("<br>", unsafe_allow_html=True)  
    if st.button("Calculate Price Range"):
        
        predict_range=predict(age, gender, zone, occupation, income_level, consume_frequency, 
                    current_brand, consumption_size, brand_awareness, reason_for_choice, 
                    flavor_preference, purchase_channel, packaging_preference, 
                    health_concerns, consumption_situation)
        
        st.success(f"Predicted Price Range: {predict_range}")

if __name__ == "__main__":
    main()
