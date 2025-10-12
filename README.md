# AI-Driven Real Estate Advisory Platform

**Author:** Vivek Kumar  
**Tech Stack:** Python, Streamlit, Pandas  

---

## **Project Overview**

This project is an **AI-driven Real Estate Advisory Platform** designed for brokers, consulting firms, and investors. It automates property analysis by calculating:

- **Liveability Index:** Measures how livable a property is based on factors like pollution, crime, distance to schools/hospitals, and property features.  
- **Viability Score:** Measures the investment potential based on price, area, rent yield, and property age.  

Users can either **manually enter a single property** or **upload a CSV** with multiple properties. The platform calculates the scores, displays them in a table, and allows downloading the analyzed CSV.

---

## **Features**

1. **Manual Property Entry**
   - Enter property details like City, Price, Area, Bedrooms, Bathrooms, Pollution, Crime, Distance to School/Hospital, Rent Yield, and Age.
   - Instantly calculates Liveability and Viability scores.

2. **CSV Upload**
   - Upload a CSV file with multiple properties.
   - Automatically calculates Liveability and Viability scores for each property.
   - View the results in a table.
   - Download the analyzed CSV for further use.

3. **AI-driven Scoring**
   - Liveability Index and Viability Score use weighted formulas for realistic property evaluation.

---

## **Required Columns for CSV**

- **Mandatory:** `City`, `Price`, `Area_sqft`, `Bedrooms`, `Bathrooms`  
- **Optional:** `Pollution_Index`, `Crime_Rate`, `School_Distance_km`, `Hospital_Distance_km`, `Rent_Yield`, `Age_Years`  

> Missing optional columns will use default values.

---

## **Installation**

1. Clone the repository:
```bash
git clone https://github.com/vivekbamauli/real-estate-ai-platform.git
cd real-estate-ai-platform
