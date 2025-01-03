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
# 3060 CHEST PAIN PROTOCOL
# ---------------------------

# Step 1: Consider life-threatening causes of chest pain in all patients
EMT_action("Consider life-threatening causes of chest pain in all patients:\n"
           "- While assessing ABCs, titrate oxygen, monitor vital signs, cardiac rhythm, start IV\n"
           "- Obtain 12-lead ECG\n"
           "- Administer aspirin if history suggests possible cardiac chest pain")

# Step 2: Check for STEMI
EMT_I_action("STEMI?")
response = "Yes"  # Example response: "Yes" or "No"

if response == "Yes":
    EMT_I_action("Notify receiving facility immediately if STEMI Alert criteria met\n"
                 "Place combination defibrillation/pacing pads on patient")
    AEMT_action("Give SL nitroglycerin if suspected cardiac chest pain and no contraindication")
    EMT_action("An EMT may administer patient’s prescribed nitroglycerin, Contact Base for verbal order")

elif response == "No":
    AEMT_action("Give SL nitroglycerin if suspected cardiac chest pain and no contraindication")
    EMT_action("An EMT may administer patient’s prescribed nitroglycerin, Contact Base for verbal order")


# Step 4: For hypotension following nitroglycerin
EMT_action("For hypotension following nitroglycerin, give 250 ml NS bolus, reassess, and repeat bolus as needed.\n"
                 "Do not give additional nitroglycerin.")

# Step 5: Consider opioid for chest pain refractory to nitroglycerin
EMT_I_action("Consider opioid for chest pain refractory to nitroglycerin, if no contraindication")

# Step 6: Consider repeat 12-lead if initial 12-lead is non-diagnostic
EMT_I_action("Consider repeat 12-lead if initial 12-lead is non-diagnostic and/or patient’s condition changes\n"
             "Consider additional 12-lead views such as R sided leads for R ventricular infarct if inferior MI present")

# Unconnected block: Life-threatening causes of chest pain
print("Life-threatening causes of chest pain:\n"
      "- Acute coronary syndrome (ACS):\n"
      "  - Unstable angina\n"
      "  - NSTEMI\n"
      "  - STEMI\n"
      "- Pulmonary embolism\n"
      "- Thoracic aortic dissection\n"
      "- Tension pneumothorax")

# Unconnected block: Nitroglycerin Contraindications
print("Nitroglycerin Contraindications:\n"
      "- Suspected right ventricular ST-segment elevation MI (inferior STEMI pattern plus ST elevation in right-sided precordial leads e.g. V4R)\n"
      "- Hypotension SBP < 100\n"
      "- Recent use of erectile dysfunction (ED) medication (e.g. Viagra, Cialis)")

# Unconnected block: Causes of Chest Pain in Children
print("Causes of Chest Pain in Children:\n"
      "- Costochondritis\n"
      "- Pulmonary Causes\n"
      "- Ischemia is rare but can be seen with a history of Kawasaki’s disease with coronary aneurysms\n"
      "- Cyanotic or Congenital Heart Disease\n"
      "- Myocarditis\n"
      "- Pericarditis\n"
      "- Arrhythmia\n"
      "- Anxiety\n"
      "- Abdominal Causes")
