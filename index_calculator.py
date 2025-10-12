def calculate_liveability(row):
    """
    Liveability Index (0-100)
    Higher score = more livable
    Formula: 
    100 - (Pollution * 0.3 + Crime * 10 + (SchoolDistance + HospitalDistance) * 5)
    """
    pollution = row.get("Pollution_Index", 50)           # default 50 if missing
    crime = row.get("Crime_Rate", 5)                     # default 5
    school_dist = row.get("School_Distance_km", 2)       # default 2 km
    hospital_dist = row.get("Hospital_Distance_km", 2)   # default 2 km

    score = 100 - (pollution * 0.3 + crime * 10 + (school_dist + hospital_dist) * 5)
    return round(max(score, 0), 2)

def calculate_viability(row):
    """
    Viability Score (0-100)
    Higher score = more profitable/investment worthy
    Formula:
    Rent_Yield * 15 + (Area / Price) * 1000 - Age * 2
    """
    rent_yield = row.get("Rent_Yield", 5)      # default 5%
    area = row.get("Area_sqft", 1000)
    price = row.get("Price", 5000000)
    age = row.get("Age_Years", 5)              # default 5 years

    score = rent_yield * 15 + (area / price) * 1000 - age * 2
    return round(max(score, 0), 2)
