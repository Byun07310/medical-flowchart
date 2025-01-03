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
# 8060 CHEST TRAUMA
# ---------------------------

# Step 1: Complete care and interventions specific to chest trauma
EMT_action("Complete care and interventions specific to chest trauma")

# Step 2: Document serial respiratory exams
EMT_action("Document serial respiratory exams in all patients with suspected chest trauma")

# Step 3: If unable to effectively oxygenate and ventilate
EMT_action("If unable to effectively oxygenate and ventilate with basic airway maneuvers, consider advanced airway\n"
           "BVM/OPA ventilation preferred in pediatrics")

# Step 4: Consider tension pneumothorax and chest needle decompression
EMT_I_action("Consider tension pneumothorax and chest needle decompression when ALL the following clinical indicators are present:\n"
                 "- Severe respiratory distress\n"
                 "- Hypotension\n"
                 "- Unilateral absent or decreased breath sounds\n"
                 "Needle decompression is NEVER indicated for simple pneumothorax")

# Step 5: For open chest wounds
EMT_action("For open chest wounds, apply 3-sided occlusive dressing")

# Step 6: If hypotension for age and/or signs of poor perfusion
EMT_action("If hypotension for age and/or signs of poor perfusion, see Traumatic Shock protocol")

# Step 7: Consider pain management
EMT_action("Consider pain management")

# Step 8: Continue General Trauma Care protocol
EMT_action("Continue General Trauma Care protocol")
