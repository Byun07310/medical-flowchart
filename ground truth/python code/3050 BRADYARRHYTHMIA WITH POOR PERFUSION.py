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
# 3050 BRADYARRHYTHMIA WITH POOR PERFUSION
# ---------------------------

# Step 1: Bradycardia with a pulse
EMT_action("Bradycardia with a pulse\n"
           "Heart rate < 60")
EMT_action("- Support ABCs\n"
           "- Give oxygen\n"
           "- Start IV\n"
           "- Initiate transport")
EMT_I_action("- Cardiac monitor\n"
             "- Identify rhythm\n"
             "- 12-lead ECG")

# Step 2: Are there signs or symptoms of poor perfusion present?
EMT_action("Are there signs or symptoms of poor perfusion present?\n"
           "(Altered mental status, chest pain, hypotension, signs of shock)")
response = "Poor perfusion"  # Example response: Adequate perfusion or Poor perfusion

if response == "Adequate perfusion":
    EMT_action("Monitor and transport")

elif response == "Poor perfusion":
    # Branch: Poor perfusion
    patient_type = "Adult"  # Example: Adult or Pediatric

    if patient_type == "Adult":
        EMT_I_action("Adult\n"
                     "- Give atropine\n"
                     "- Prepare for transcutaneous pacing\n"
                     "- If mechanical pacing capture but still hypotensive, consider fluids")
        Paramedic_action("- Consider epinephrine if pacing with poor perfusion or hypotension")

    elif patient_type == "Pediatric":
        EMT_action("Pediatric\n"
                   "- Give epinephrine\n"
                   "- Consider atropine\n"
                   "- If no improvement, Contact Base to discuss transcutaneous pacing")

# Unconnected block: Pediatric Considerations
print("Pediatric Considerations:\n"
      "- Consider any HR <60 in an ill child abnormal regardless of age\n"
      "- Perform CPR if HR <60 with poor perfusion despite oxygenation and ventilation\n"
      "- Administer epinephrine if bradycardia persists despite oxygenation/ventilation and chest compressions\n"
      "- Atropine should be administered for increased vagal tone or AV block\n")

# Unconnected block: Reminders
print("Reminders:\n"
      "- If pulseless arrest develops, go to pulseless arrest algorithm\n"
      "- Search for possible contributing factors: '5 Hs and 5 Ts'\n"
      "- Symptomatic severe bradycardia is usually related to one of the following:\n"
      "  - Ischemia (MI)\n"
      "  - Drugs (beta blocker, calcium channel blocker)\n"
      "  - Electrolytes (hyperkalemia)")
