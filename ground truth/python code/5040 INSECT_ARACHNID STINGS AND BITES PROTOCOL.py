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
# 5040 INSECT/ARACHNID STINGS AND BITES PROTOCOL
# ---------------------------

# Step 1: Initiate general care for bites and stings
EMT_action("Initiate general care for bites and stings")

# Step 2: Assess for localized vs. systemic signs and symptoms and depending on animal involved
EMT_action("Assess for localized vs. systemic signs and symptoms and depending on animal involved")

# Branch: Localized Symptoms
localized_symptoms = "Yes"  # Example response: Yes or No
if localized_symptoms == "Yes":
    EMT_action("Localized Symptoms:\n"
               "- Pain, warmth and swelling")
    EMT_action("Consider pain management for severe pain (e.g.: black widow spider) and/or")
    AEMT_action("diphenhydramine if needed for itching")

# Branch: Systemic Symptoms
systemic_symptoms = "Yes"  # Example response: Yes or No
if systemic_symptoms == "Yes":
    EMT_action("Systemic Symptoms:\n"
                "- Hives, generalized erythema, swelling, angioedema\n"
                "- Hypotension\n"
                "- Altered mental status\n"
                "- Other signs of shock")
    EMT_action("Administer oxygen\nStart IV")
    EMT_action("Treat per allergy & anaphylaxis protocol")

# Unconnected block: General Care
print("General Care:\n"
      "- For bees/wasps - Remove stinger mechanism by scraping with a straight edge. Do not squeeze venom sac")

# Unconnected block: Specific Information Needed
print("Specific Information Needed:\n"
      "- Timing of bite/sting\n"
      "- Identification of spider, bee, wasp, other insect, if possible\n"
      "- History of prior allergic reactions to similar exposures\n"
      "- Treatment prior to EMS eval: e.g. EpiPen, diphenhydramine, etc")

# Unconnected block: Specific Precautions
print("Specific Precautions:\n"
      "- For all types of bites and stings, the goal of prehospital care is to prevent further envenomation and to treat allergic reactions\n"
      "- Anaphylactoid reactions may occur upon first exposure to allergen, and do not require prior sensitization\n"
      "- Anaphylactic reactions typically occur abruptly, and rarely > 60 minutes after exposure")
