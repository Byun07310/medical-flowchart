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
# 8040 FACE AND NECK TRAUMA
# ---------------------------

# Step 1: Complete care and interventions specific to face and neck trauma
EMT_action("Complete care and interventions specific to face and neck trauma")

# Step 2: Initial Management
EMT_action("- Clear airway\n"
           "- Rapid trauma assessment\n"
           "- Consider spinal motion restriction\n"
           "- Assess for need for airway management")

# Step 3: If laryngeal trauma
EMT_action("If laryngeal trauma, avoid intubation if patient can be oxygenated by less invasive means")

# Step 4: For severe airway bleeding
EMT_action("For severe airway bleeding:\n"
           "- Use direct pressure if able without obstructing airway")
EMT_I_action("- Consider advanced airway if adequate ventilation and oxygenation cannot be achieved with basic airway maneuvers")
EMT_action("- BVM/OPA ventilation preferred in pediatrics")

# Step 5: Further assessment
EMT_action("- Complete neuro exam\n"
           "- Assess for subcutaneous air\n"
           "- Cover/protect eyes as indicated\n"
           "- Do not try to block drainage from ears, nose")

# Step 6: Rapid transport
EMT_action("Rapid transport to appropriate Trauma Center\n"
           "- Suction airway as needed")

# Step 7: If hypotension for age and/or signs of poor perfusion
EMT_action("If hypotension for age and/or signs of poor perfusion, see Traumatic Shock protocol")

# Step 8: Pain management
EMT_action("Consider pain management")

# Step 9: Continue General Trauma Care protocol
EMT_action("Continue General Trauma Care protocol")

# Unconnected block: Facial Injury Considerations
print("Facial Injury Considerations:\n"
      "- Nasotracheal intubation is a relative contraindication in suspected head trauma or grossly unstable mid-face trauma\n"
      "- Orbital area fractures should be of high concern for serious ocular injury and sequela\n"
      "- Save avulsed teeth in moist gauze, if possible\n"
      "- Be attentive to airway and suctioning, as bleeding, avulsed teeth, or other tissue can become an airway obstruction, especially with supine positioning")

# Unconnected block: Eye Injury Considerations
print("Eye Injury Considerations:\n"
      "- Cover and protect eyes as indicated by injury type; do not apply pressure to eyes\n"
      "- Orbital area fractures should be of high concern as they can result in ocular muscle entrapment and ocular compartment syndrome")

# Unconnected block: Neck Injury Considerations
print("Neck Injury Considerations:\n"
      "- Spinal motion restriction is not routinely indicated for penetrating neck injury but should be placed in the presence of neurologic deficit\n"
      "- Laryngeal trauma should be suspected with the following:\n"
      "  - Voice changes and stridor\n"
      "  - Respiratory distress\n"
      "  - External signs of bruising, swelling, or bleeding")
