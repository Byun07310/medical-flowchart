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
# 8030 HEAD TRAUMA
# ---------------------------

# Step 1: Complete care and interventions specific to head-injured patients
EMT_action("Complete care and interventions specific to head-injured patients")

# Step 2: Assess neurologic status
EMT_action("Assess neurologic status")

# Step 3: Goals of Treatment
EMT_action("Goals of Treatment:\n"
           "- Prevent and treat hypoxia\n"
           "- Avoid hyperventilation\n"
           "- Address and treat hypotension")

# Step 4: Management steps for head trauma
EMT_action("- Decrease ICP by elevating head 30°, if possible\n"
           "- Support ventilations with target of ETCO₂ 35–45 mmHg\n"
           "- Consider advanced airway if adequate ventilation and oxygenation cannot be achieved with basic airway maneuvers\n"
           "- Nasotracheal intubation is a relative contraindication in head trauma\n"
           "- BVM/OPA ventilation preferred in pediatrics")

# Step 5: If hypotension for age and/or signs of poor perfusion
EMT_action("If hypotension for age and/or signs of poor perfusion, see Traumatic Shock protocol")

# Step 6: Continue General Trauma Care protocol
EMT_action("Continue General Trauma Care protocol")

# Unconnected block: Overview of Treatment
print("Overview of Treatment:\n"
      "- With any suspicion of traumatic brain injury (mechanism, GCS, exam), aggressive treatment to prevent hypoxia, hyperventilation, and hypotension is recommended:\n"
      "  - High flow oxygen on all TBI patients\n"
      "  - Maintain saturation >90%\n"
      "  - Do not hyperventilate; maintain end tidal CO₂ 35–45 mmHg\n"
      "  - Maintain systolic BP >100 mmHg. Treat early per Traumatic Shock protocol")
