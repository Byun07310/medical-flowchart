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
# 2060 CHF/PULMONARY EDEMA
# ---------------------------

# Unconnected block: Therapeutic Goals
print("Therapeutic Goals:\n"
      "- Maximize oxygenation\n"
      "- Decrease work of breathing\n"
      "- Identify cardiac ischemia (Obtain 12 lead ECG)\n"
      "Special Notes:\n"
      "- In general diuretics have little role in initial treatment of acute pulmonary edema and are no longer considered first line therapy.\n"
      "- Morphine has been associated with worse outcomes in patients with CHF and is no longer indicated.\n")

# Step 1: Universal Respiratory Distress Protocol
EMT_action("Universal Respiratory Distress Protocol")

# Step 2: CHF/Pulmonary Edema
EMT_action("CHF/Pulmonary edema")

# Step 3: Obtain 12 lead ECG
EMT_I_action("Obtain 12 lead ECG; rule out unstable rhythm, STEMI")

# Step 4: Give nitroglycerin (NTG)
AEMT_action("Give nitroglycerin (NTG)")

# Step 5: Is oxygenation and ventilation adequate?
EMT_action("Is oxygenation and ventilation adequate?")
response = "No"  # Example response directly from flowchart

if response == "No":
    EMT_action("Start CPAP protocol")

    # Step 6: Is response to treatment adequate?
    EMT_action("Is response to treatment adequate?")
    response = "No"  # Example response directly from flowchart

    if response == "No":
        EMT_action("If failing above therapy:\n"
                         "- Remove CPAP and ventilate with BVM\n"
                         "- Consider pneumothorax\n"
                         "- Consider alternative diagnoses/complications\n"
                         "- Consider advanced airway")

# Final Step: Continue monitoring and assessment
EMT_action("Continue monitoring and assessment\n"
           "Transport\n"
           "Contact base for medical consult as needed")
