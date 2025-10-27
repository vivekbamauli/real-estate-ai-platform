import streamlit as st
import pandas as pd
from index_calculator import calculate_liveability, calculate_viability

st.title("AI-Driven Real Estate Advisory Platform")
st.header("Evaluate Properties for Livability and Investment Viability")

# Option selector
option = st.radio("Choose Input Method:", ("Manual Entry", "Upload CSV"))

# ---------------- Manual Entry ----------------
if option == "Manual Entry":
    st.subheader("Enter Property Details Manually")

    city = st.text_input("City", "Delhi")
    price = st.number_input("Price", 100000, 100000000, step=100000)
    area = st.number_input("Area (sqft)", 100, 10000, step=50)
    bedrooms = st.number_input("Bedrooms", 1, 10)
    bathrooms = st.number_input("Bathrooms", 1, 10)
    pollution = st.number_input("Pollution Index (0-100)", 0, 100, 50)
    crime = st.number_input("Crime Rate (1-10)", 1, 10, 5)
    school_dist = st.number_input("Distance to School (km)", 0.1, 20.0, 2.0)
    hospital_dist = st.number_input("Distance to Hospital (km)", 0.1, 20.0, 2.0)
    rent_yield = st.number_input("Expected Rent Yield (%)", 0.0, 20.0, 5.0)
    age_years = st.number_input("Property Age (years)", 0, 100, 5)

    if st.button("Analyze Property"):
        property_row = pd.DataFrame([{
            "City": city,
            "Price": price,
            "Area_sqft": area,
            "Bedrooms": bedrooms,
            "Bathrooms": bathrooms,
            "Pollution_Index": pollution,
            "Crime_Rate": crime,
            "School_Distance_km": school_dist,
            "Hospital_Distance_km": hospital_dist,
            "Rent_Yield": rent_yield,
            "Age_Years": age_years
        }])
        property_row["Liveability_Index"] = property_row.apply(calculate_liveability, axis=1)
        property_row["Viability_Score"] = property_row.apply(calculate_viability, axis=1)
        st.subheader("Property Analysis")
        st.dataframe(property_row)

# ---------------- CSV Upload ----------------
else:
    st.subheader("Upload CSV File with Multiple Properties")
    uploaded_file = st.file_uploader("Choose CSV", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        # Calculate scores safely
        df["Liveability_Index"] = df.apply(calculate_liveability, axis=1)
        df["Viability_Score"] = df.apply(calculate_viability, axis=1)
        
        st.subheader("Analyzed Properties")
        st.dataframe(df)
        
        # Download analyzed CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Analyzed CSV",
            data=csv,
            file_name="analyzed_properties.csv",
            mime="text/csv"
        )
    else:
        st.info("Please upload a CSV file to analyze multiple properties.")
