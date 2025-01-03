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
# 4100 NON-TRAUMATIC ABDOMINAL PAIN/VOMITING
# ---------------------------

# Step 1: Assess ABCs
EMT_action("Non-traumatic abdominal pain and/or vomiting")
EMT_action("- Assess ABCs\n"
           "- Give oxygen\n"
           "- Complete set of vital signs\n"
           "- Consider life-threatening causes")

# Step 2: Signs of poor perfusion or hypotension?
EMT_action("If signs of poor perfusion AND/OR hypotension for age, see Medical Shock protocol and begin fluid resuscitation")

# Step 3: Consider IV
EMT_action("- Consider IV\n"
             "- If GI bleed, start 2nd IV\n"
             "- Transport in position of comfort")

# Step 4: Antiemetic and pain management
EMT_action("Consider antiemetic for vomiting and pain management for pain")

# Step 5: Cardiac monitor and 12 lead ECG
EMT_I_action("Cardiac monitor and 12 lead ECG for any of the following:\n"
             "- Diabetic\n"
             "- Age > 50\n"
             "- Upper abdominal pain concerning for ACS\n"
             "- Unstable vital signs in the adult patient")

# Step 6: Monitor and transport
EMT_action("- Monitor and transport\n"
           "- Frequent reassessment for deterioration and response to treatment")

# Unconnected block: Life-threatening causes
print("Life-threatening causes:\n"
      "- Cardiac etiology: MI, ischemia\n"
      "- Vascular etiology: AAA, dissection\n"
      "- GI bleed\n"
      "- Gynecologic etiology: ectopic pregnancy")

# Unconnected block: History
print("History:\n"
      "- Onset, location, duration, radiation of pain\n"
      "- Associated symptoms: vomiting, bilious emesis, GU sx, hematemesis, coffee ground emesis, melena, rectal bleeding, vaginal bleeding, known or suspected pregnancy, recent trauma")

# Unconnected block: Pediatric Patients
print("Pediatric Patients:\n"
      "- Life-threatening causes vary by age. Consider occult or non-accidental trauma, toxic ingestion, button battery ingestion, GI bleed, peritonitis\n"
      "- For most pediatric patients without signs of shock, no IV is required and pharmacologic pain management should be limited")

# Unconnected block: Elderly Patients
print("Elderly Patients:\n"
      "- Much more likely to have life-threatening cause of symptoms\n"
      "- Shock may be occult, with absent tachycardia in setting of severe hypovolemia")
