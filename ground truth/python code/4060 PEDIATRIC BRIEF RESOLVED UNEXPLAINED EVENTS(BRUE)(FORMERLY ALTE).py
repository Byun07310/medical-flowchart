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
# 4060 PEDIATRIC BRIEF RESOLVED UNEXPLAINED EVENTS (BRUE)
# ---------------------------

# Step 1: Definition
EMT_action("Definition:\n"
           "An infant < 1 year of age with episode frightening to the observer characterized by apnea, choking/gagging, color change or change in muscle tone")

# Step 2: Support ABCs as necessary
EMT_action("Support ABCs as necessary")

# Step 3: Obtain detailed history of event and medical history
EMT_action("Obtain detailed history of event and medical history")

# Step 4: Complete head-to-toe assessment
EMT_action("Complete head-to-toe assessment")

# Step 5: Transport and monitor
EMT_action("- Any child with a BRUE should be transported to ED for evaluation\n"
           "- Monitor vital signs en route")

# Unconnected block: Clinical history to obtain from observer of event
print("Clinical history to obtain from observer of event:\n"
      "- Document observer’s impression of the infant’s color, respirations and muscle tone\n"
      "- For example, was the child apneic, or cyanotic or limp during event?\n"
      "- Was there seizure-like activity noted?\n"
      "- Was any resuscitation attempted or required, or did event resolve spontaneously?\n"
      "- How long did the event last?")

# Unconnected block: Past Medical History
print("Past Medical History:\n"
      "- Recent trauma, infection (e.g. fever, cough)\n"
      "- History of GERD\n"
      "- History of Congenital Heart Disease\n"
      "- History of Seizures\n"
      "- Medication history")

# Unconnected block: Examination/Assessment
print("Examination/Assessment:\n"
      "- Head to toe exam for trauma, bruising, or skin lesions\n"
      "- Check anterior fontanelle: is it bulging, flat or sunken?\n"
      "- Pupillary exam\n"
      "- Respiratory exam for rate, pattern, work of breathing and lung sounds\n"
      "- Cardiovascular exam for murmurs and symmetry of brachial and femoral pulses\n"
      "- Neuro exam for level of consciousness, responsiveness and any focal weakness")
