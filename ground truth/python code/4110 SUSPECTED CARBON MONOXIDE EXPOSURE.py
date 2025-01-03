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
# 4110 SUSPECTED CARBON MONOXIDE EXPOSURE
# ---------------------------

# Step 1: ABCs
EMT_action("ABCs")

# Step 2: Symptoms of CO, hypoxia, and/or pregnancy?
response = "Yes"  # Example: Yes or No

if response == "Yes":
    EMT_action("100% FiO2 and transport")
elif response == "No":
    # Step 3: Measure COHb% (SpCO)
    EMT_action("Measure COHb% (SpCO)")
    SpCO = 10  # Example SpCO value

    if SpCO <= 5:
        EMT_action("No further evaluation of SpCO is needed")
    elif 5 < SpCO <= 15:
        EMT_action("Contact Base for consult")
    elif SpCO > 15:
        EMT_action("100% FiO2 and transport")

# Unconnected block: General Guidelines
print("General Guidelines:\n"
      "- Signs and Symptoms of CO exposure include:\n"
      "  - Headache, dizziness, coma, altered mentation, seizures, visual changes, chest pain, tachycardia, arrhythmias, dyspnea, N/V, 'flu-like illness'\n"
      "- The absence or low readings of COHb is not a reliable predictor of toxicity of other fire byproducts\n"
      "- In smoke inhalation victims, consider cyanide treatment with hydroxocobalamin as per indications\n"
      "- The fetus of a pregnant woman is at higher risk due to the greater affinity of fetal hemoglobin to CO. With CO exposure, the pregnant woman may be asymptomatic while the fetus may be in distress. In general, pregnant patients exposed to CO should be transported.\n"
      "- People who smoke may have SpCO of up to 10% baseline")

# Unconnected block: COHb Severity Table
print("COHb Severity Table:\n"
      "COHb (%)   Severity       Signs and Symptoms\n"
      "--------------------------------------------\n"
      "5-20%      Mild           Headache, nausea, vomiting, dizziness, blurred vision\n"
      "21-40%     Moderate       Confusion, syncope, chest pain, dyspnea, tachycardia, tachypnea, weakness\n"
      "41-59%     Severe         Dysrhythmias, hypotension, cardiac ischemia, palpitations, respiratory arrest, pulmonary edema, seizures, coma, cardiac arrest\n"
      ">60%       Fatal          Death")
