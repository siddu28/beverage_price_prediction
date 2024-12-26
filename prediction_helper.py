import joblib
import pandas as pd
label_encoders = joblib.load("artifacts/label_encoders.pkl")
model=joblib.load("artifacts/final_xgboost_model.pkl")
price_encoder=joblib.load("artifacts/label_encoder_price_range.pkl")



MODEL_PATH = 'artifacts/final_xgboost_model.pkl'


def prepare_input(age, gender, zone, occupation, income_level, consume_frequency, 
                    current_brand, consumption_size, brand_awareness, reason_for_choice, 
                    flavor_preference, purchase_channel, packaging_preference, 
                    health_concerns, consumption_situation):
    
    zone_mapping = {"urban": 3, "metro": 4, "rural": 1, "semi-urban": 2}
    income_level_mapping = {"<10L": 1, "> 35L": 5, "16L - 25L": 3, "Not Reported": 0, "10L - 15L": 2, "26L - 35L": 4}
    brand_awareness_mapping = {"0 to 1": 1, "2 to 4": 2, "above 4": 3}
    consume_frequency_mapping = {"3-4 times": 2, "0-2 times": 1, "5-7 times": 3}

    if age >= 18 and age <= 25:
        age_group = '18-25'
    elif age >= 26 and age <= 35:
        age_group = '26-35'
    elif age >= 36 and age <= 45:
        age_group = '36-45'
    elif age >= 46 and age <= 55:
        age_group = '46-55'
    elif age >= 56 and age <= 70:
        age_group = '56-70'
    else:
        age_group = '18-25'

    cf_ab_score = consume_frequency_mapping.get(consume_frequency, 0) / (
    consume_frequency_mapping.get(consume_frequency, 0) + brand_awareness_mapping.get(brand_awareness, 0)
    ) if (consume_frequency_mapping.get(consume_frequency, 0) + brand_awareness_mapping.get(brand_awareness, 0)) != 0 else 0

    zas_score = zone_mapping.get(zone, 0) * income_level_mapping.get(income_level, 0)

    bsi = 1 if current_brand != 'Established' and reason_for_choice in ['Price', 'Quality'] else 0


    
    input_data = {
        'zone': zone_mapping.get(zone, 0),
        'income_levels': income_level_mapping.get(income_level, 0),
        'consume_frequency(weekly)': consume_frequency_mapping.get(consume_frequency, 0),
        'preferable_consumption_size': label_encoders['preferable_consumption_size'].transform([consumption_size])[0] if 'preferable_consumption_size' in label_encoders else -1,
        'awareness_of_other_brands': brand_awareness_mapping.get(brand_awareness, 0),
        'health_concerns': label_encoders['health_concerns'].transform([health_concerns])[0] if 'health_concerns' in label_encoders else -1,
        'age_group': label_encoders['age_group'].transform([age_group])[0] if 'age_group' in label_encoders else -1,
        'cf_ab_score': cf_ab_score, 
        'zas_score': zas_score, 
        'bsi': bsi, 
        'current_brand_newcomer': 1 if current_brand == 'newcomer' else 0,
        'flavor_preference_Traditional': 1 if flavor_preference == 'Traditional' else 0,
        'gender_M': 1 if gender == 'M' else 0,
        'occupation_Retired': 1 if occupation == 'Retired' else 0,
        'occupation_Student': 1 if occupation == 'Student' else 0,
        'occupation_Working Professional': 1 if occupation == 'Working Professional' else 0,
        'packaging_preference_Premium': 1 if packaging_preference == 'Premium' else 0,
        'packaging_preference_Simple': 1 if packaging_preference == 'Simple' else 0,
        'purchase_channel_Retail Store': 1 if purchase_channel == 'Retail Store' else 0,
        'reasons_for_choosing_brands_Brand Reputation': 1 if reason_for_choice == 'Brand Reputation' else 0,
        'reasons_for_choosing_brands_Price': 1 if reason_for_choice == 'Price' else 0,
        'reasons_for_choosing_brands_Quality': 1 if reason_for_choice == 'Quality' else 0,
        'typical_consumption_situations_Casual (eg. At home)': 1 if consumption_situation == 'Casual (eg. At home)' else 0,
        'typical_consumption_situations_Social (eg. Parties)': 1 if consumption_situation == 'Social (eg. Parties)' else 0,
    }

    df = pd.DataFrame([input_data])

    return df


def predict(age, gender, zone, occupation, income_level, consume_frequency, 
                    current_brand, consumption_size, brand_awareness, reason_for_choice, 
                    flavor_preference, purchase_channel, packaging_preference, 
                    health_concerns, consumption_situation):
    
    input_df = prepare_input(age, gender, zone, occupation, income_level, consume_frequency, 
                    current_brand, consumption_size, brand_awareness, reason_for_choice, 
                    flavor_preference, purchase_channel, packaging_preference, 
                    health_concerns, consumption_situation)
    
    prediction = model.predict(input_df)[0]
    loaded_encoder = joblib.load("artifacts/label_encoder_price_range.pkl")
    original_prediction = loaded_encoder.inverse_transform([prediction])[0]

    return original_prediction





