#young's formula -->aged 1 to 12
#  age / (age + 12) * adult dose

Name = input("enter your name:\n")
child_age = int(input("Enter age:\n"))
adult_medication_dose = int(input("enter adult dose:\n")) 

def calculate_youngs_dose(age_years, adult_dose):

    if age_years < 1:
        return "Error: Young's Rule is not suitable for infants under 1 year old."
    elif age_years > 12:
        return "Warning: Young's Rule is typically used for children aged 1-12. Consider adult dosing or weight-based dosing."
    
    child_dose = (age_years / (age_years + 12)) * adult_dose
    return round(child_dose, 2)

recommended_dose = calculate_youngs_dose(child_age, adult_medication_dose) 
print("=============================================")
print(f"Standard Adult Dose: {adult_medication_dose} mg")
print(f"Patient Age: {child_age} years old")
print(f"Calculated Pediatric Dose: {recommended_dose} mg")
print("=============================================")

    
     










