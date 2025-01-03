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
# 3030 POST-CARDIAC ARREST CARE
# ---------------------------

# Unconnected block: Post-Cardiac Arrest Care
print("Post-Cardiac Arrest Care:\n"
      "- Following ROSC, several simultaneous and stepwise interventions must be performed to optimize care and maximize patient outcome\n"
      "- Survival and neurologic outcome worsen with fever, hypoxia, hypo/hypercapnia, and hypotension. Post-ROSC care should focus on prevention of these elements\n")

# Unconnected block: Return of spontaneous circulation (ROSC) criteria
print("Return of spontaneous circulation (ROSC) criteria:\n"
      "- Pulse and measurable blood pressure\n"
      "- Increase in ETCO2 on capnography\n"
      "Document:\n"
      "- Time of arrest (or time last seen normal)\n"
      "- Witnessed vs. unwitnessed arrest\n"
      "- Initial rhythm shockable vs. non-shockable\n"
      "- Time of ROSC\n"
      "- Bystander CPR given\n"
      "- GCS after ROSC\n"
      "- Initial temperature of patient after ROSC, if possible\n")

# Unconnected block: Target ROSC Vital Signs
print("Target ROSC Vital Signs:\n"
      "- SpO2: 92%-98%\n"
      "- PaCO2: 35-45 mmHg\n"
      "- Systolic pressure >90 mmHg or mean arterial pressure >65 mmHg\n")

# Step 1: ROSC after cardiac arrest
EMT_action("ROSC after cardiac arrest")

# Step 2: Perform 12 lead EKG
EMT_I_action("Perform 12 lead EKG")

# Step 3: Is STEMI present?
EMT_action("Is STEMI Present?")
response = "No"  # Example response directly from flowchart

if response == "Yes":
    EMT_action("Initiate STEMI Alert")

elif response == "No":
    # Step 4: Assess for shock and volume status
    EMT_action("Assess for shock and volume status\n"
               "- Peripheral access: IO/IV\n"
               "- Oxygenation/Ventilation\n"
               "  - Secure advanced airway if indicated\n"
               "  - Avoid hyperventilation\n"
               "  - Avoid hyper/hypocapnia (ETCO2)\n"
               "  - Correct hypoxemia\n"
               "- Elevate head of bed at 30°")

    # Step 5: Is there hypotension for age and/or signs of shock?
    EMT_action("Is there hypotension for age and/or signs of shock?")
    response = "No"  # Example response directly from flowchart

    if response == "Yes":
        EMT_I_action("Follow Medical Hypotension/Shock protocol")

    elif response == "No":
        # Step 6: Assess for dysrhythmia
        EMT_action("Assess for dysrhythmia")
        response = "Yes"  # Example response directly from flowchart

        if response == "Yes":
            Paramedic_action("Treat recurrent dysrhythmia per appropriate protocol")

        elif response == "No":
            # Final Step: Continuous rhythm monitoring and assessment
            EMT_action("Continuous rhythm monitoring and pulse checks\n"
                       "Focused neuro exam (AVPU/GCS)\n"
                       "If fever and no purposeful movement provide passive cooling by placing ice packs to neck, axillae, and/or groin\n"
                       "Transfer to closest appropriate facility")
