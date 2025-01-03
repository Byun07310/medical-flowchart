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
# 6015 POST SEDATION RESUSCITATION AND MONITORING
# ---------------------------

# Step 1: Post Sedation Resuscitation and Monitoring
EMT_action("Post Sedation Resuscitation and Monitoring:\n"
            "- Maintain airway\n"
            "- Administer oxygen\n"
            "- Monitor capnography: Maintain respiratory rate ≥8 breaths per minute\n"
            "- Monitor SpO2: Goal of 100%\n"
            "- Establish IV access, if not already in place\n"
            "- Cardiac monitoring")

# Step 2: Continue patient assessment
EMT_action("Continue patient assessment")

# Step 3: Initiate immediate transport to appropriate Emergency Department
EMT_action("Initiate immediate transport to appropriate Emergency Department")

# Step 4: Complete restraint protocol and maintain restraints through to Emergency Department
EMT_action("Complete restraint protocol and maintain restraints through to Emergency Department")

# Unconnected block: Adequate Sedation
print("Adequate Sedation:\n"
      "- The goal of sedation is to ensure safety to patient and provider and allow for adequate evaluation and treatment of underlying causes\n"
      "- Agitation that does not compromise patient/provider safety or interfere with evaluation and treatment does not require additional sedation\n")

# Unconnected block: General Guidelines
print("General Guidelines:\n"
      "- Patients receiving sedative medications have a broad range of responses both from the medication given and the underlying etiology of the agitation. They should be treated as high risk for respiratory or cardiovascular compromise\n"
      "- Goal is to initiate resuscitation/monitoring as soon as possible\n"
      "- Each individual element of post-sedation resuscitation/monitoring should be initiated as soon as possible to do so\n")
