# Define functions for each certification level
def EMT_action(description):
    print(f"EMT Action:\n{description}\n")

def AEMT_action(description):
    print(f"AEMT Action:\n{description}\n")

def EMT_I_action(description):
    print(f"EMT-I Action:\n{description}\n")

def Paramedic_action(description):
    print(f"Paramedic Action:\n{description}\n")

# ---------------------------
# 2050 PEDIATRIC STRIDOR/CROUP
# ---------------------------

# Unconnected block: Characteristics of Croup
print("Characteristics of Croup:\n"
      "- Most common cause of stridor in children\n"
      "- Child will have stridor, barky cough, and URI symptoms of sudden, often nocturnal onset\n"
      "- Most often seen in children < 9 years old\n"
      "- Agitation worsens the stridor and respiratory distress\n")

# Unconnected block: Considerations with Stridor
print("Considerations with Stridor:\n"
      "- Stridor is a harsh, usually inspiratory sound caused by narrowing or obstruction of the upper airway\n"
      "- Causes include croup, foreign body aspiration, allergic reactions, trauma, infection, mass\n"
      "- Epiglottitis is exceedingly rare. May consider in the unimmunized child. Treatment is minimization of agitation. Airway manipulation is best done in the hospital\n")

# Step 1: Pediatric Universal Respiratory Distress
EMT_action("Pediatric Universal Respiratory Distress protocol and prepare for immediate transport")

# Step 2: Minimize agitation
EMT_action("Minimize agitation: Transport in position of comfort, interventions only as necessary")

# Step 3: Check SpO2
EMT_action("Check SpO2, give oxygen as needed")

# Step 4: Are symptoms severe and croup most likely?
EMT_action("Are symptoms severe and croup most likely?\n"
           "- Stridor at rest or biphasic stridor\n"
           "- Severe retractions\n"
           "- SpO2 < 90% despite O2\n"
           "- Altered LOC\n"
           "- Cyanosis")
response = "Yes"  # Example response directly from flowchart

if response == "Yes":
    EMT_I_action("Give nebulized epinephrine")

    # Step 5: Signs of poor perfusion or hypotension?
    EMT_action("If signs of poor perfusion AND/OR hypotension for age, see Medical Shock protocol and begin fluid resuscitation")

# Final Step: Continue monitoring and assessment
EMT_action("Continue monitoring and assessment en route\n"
           "Contact Base for repeat dose of nebulized epinephrine and medical consult as needed")
