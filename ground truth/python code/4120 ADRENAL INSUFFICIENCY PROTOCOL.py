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
# 4120 ADRENAL INSUFFICIENCY PROTOCOL
# ---------------------------

# Step 1: Identify patients at risk for adrenal insufficiency
EMT_action("Patient at risk for adrenal insufficiency (Addisonian crisis):\n"
           "- Identified by family or medical alert bracelet\n"
           "- Chronic steroid use\n"
           "- Congenital Adrenal Hyperplasia\n"
           "- Addison’s disease")

# Step 2: Assess for signs of acute adrenal crisis
EMT_action("Assess for signs of acute adrenal crisis:\n"
           "- Pallor, weakness, lethargy\n"
           "- Vomiting, abdominal pain\n"
           "- Hypotension, shock\n"
           "- Congestive heart failure")

# Step 3: All symptomatic patients
EMT_action("All symptomatic patients:\n"
            "- Check blood glucose and treat hypoglycemia, if present\n"
            "- Start IV and give oxygen\n"
            "- If signs of poor perfusion AND/OR hypotension for age, see Medical Shock protocol and begin fluid resuscitation")

# Step 4: Administer corticosteroid
EMT_I_action("Give corticosteroid")

# Step 5: Continue monitoring and additional steps
EMT_action("Continue to monitor for development of hypoglycemia\n"
           "Contact Base for consult if patient not responding to treatment")
EMT_I_action("Monitor 12-lead ECG for signs of hyperkalemia")

# Unconnected block: General Guidelines
print("General Guidelines:\n"
      "- Chronic corticosteroid use is a common cause for adrenal crisis, carefully assess for steroid use in patients with unexplained shock.\n"
      "- Administration of steroids are life-saving and necessary for reversing shock or preventing cardiovascular collapse.\n"
      "- Patients at risk for adrenal insufficiency may show signs of shock when under physiologic stress which would not lead to cardiovascular collapse in normal patients. Such triggers may include trauma, dehydration, infection, myocardial ischemia, etc.\n"
      "- If no corticosteroid is available during transport, notify receiving hospital of need for immediate corticosteroid upon arrival.\n"
      "- Under Chapter 2 Rule: specialized prescription medications to address an acute crisis may be given by all levels with a direct VO, given the route of administration is within the scope of the provider. This applies to giving hydrocortisone for adrenal crisis, for instance, if a patient or family member has this medication available on scene. Contact Base for direct verbal order.")
