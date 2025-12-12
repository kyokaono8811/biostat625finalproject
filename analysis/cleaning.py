def clean_data(heart_data):
    heart_clean = heart_data.copy()

    # Binary variables
    binary_vars = ["HadHeartAttack", "PhysicalActivities", "HadStroke", "AlcoholDrinkers"]
    for var in binary_vars:
        heart_clean[var] = heart_clean[var].map({"Yes": 1, "No": 0})

    # Sex
    heart_clean["Sex"] = heart_clean["Sex"].map({"Female": 0, "Male": 1})

    # AgeCategory
    age_order = [
        "Age 18 to 24", "Age 25 to 29", "Age 30 to 34", "Age 35 to 39",
        "Age 40 to 44", "Age 45 to 49", "Age 50 to 54", "Age 55 to 59",
        "Age 60 to 64", "Age 65 to 69", "Age 70 to 74", "Age 75 to 79",
        "Age 80 or older"
    ]
    age_map = {age: i + 1 for i, age in enumerate(age_order)}
    heart_clean["AgeCategory"] = heart_clean["AgeCategory"].map(age_map)

    # HadDiabetes
    heart_clean["HadDiabetes"] = heart_clean["HadDiabetes"].replace({
        "Yes": 1,
        "Yes, but only during pregnancy (female)": 1,
        "No": 0,
        "No, pre-diabetes or borderline diabetes": 0
    })

    # SmokerStatus
    heart_clean["SmokerStatus"] = heart_clean["SmokerStatus"].replace({
        "Never smoked": 0,
        "Former smoker": 1,
        "Current smoker - now smokes every day": 2,
        "Current smoker - now smokes some days": 2
    })

    # RaceEthnicityCategory
    heart_clean["RaceEthnicityCategory"] = heart_clean["RaceEthnicityCategory"].replace({
        "White only, Non-Hispanic": 0,    
        "Black only, Non-Hispanic": 1,    
        "Hispanic": 2,                     
        "Multiracial, Non-Hispanic": 3,  
        "Other race only, Non-Hispanic": 4
    })

    return heart_clean

