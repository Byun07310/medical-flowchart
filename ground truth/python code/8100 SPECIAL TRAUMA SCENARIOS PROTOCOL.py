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
# 8100 SPECIAL TRAUMA SCENARIOS PROTOCOL
# ---------------------------

# Step 1: General Trauma Care
EMT_action("See General Trauma Care protocol")

# Step 2: Branch - Sexual Assault or Abuse/Neglect
scenario = "Sexual Assault"  # Example input: Sexual Assault or Abuse/Neglect

if scenario == "Sexual Assault":
    EMT_action("Confine history to pertinent medical needs (when assault occurred, where)")
    EMT_action("- Trauma-focused, victim-centered care\n"
               "- Respect patient’s emotional needs")
    EMT_action("Don’t judge, accuse, or confront victim")
    EMT_action("Protect evidence: No washing, changing clothes. Keep NPO.")
    EMT_action("Coordinate transport destination with law enforcement")
    EMT_action("For reporting, refer to General Guidelines Mandatory Reporting or agency guidelines")

elif scenario == "Abuse/Neglect":
    EMT_action("Watch out for:\n"
               "- Injury inconsistent with stated mechanism\n"
               "- Delayed treatment\n"
               "- Spreading blame\n"
               "- Conflicting stories\n"
               "- Prior/healing injuries")
    EMT_action("Don’t judge, accuse, or confront victim or suspected assailant")
    EMT_action("Transport patient if suspected abuse or neglect, no matter how apparently minor the injury")
    EMT_action("For reporting, refer to General Guidelines Mandatory Reporting or agency guidelines")

# Unconnected block: Mandatory Reporters
print("Mandatory Reporters:\n"
      "- EMS providers provide a critical layer of protection to vulnerable adults and children who have been abused.\n"
      "- C.R.S. 19-3-304 passed in 2014 extended the role of mandated reporters to EMS providers in Colorado.\n"
      "- Mandated reporters are to “report their suspicion” of abuse. This is not considered a direct accusation if acting in good faith.\n"
      "- Informing providers at the receiving facility of suspicions for DOES NOT meet the requirements of a mandated reporter - EMS providers ARE REQUIRED to register their suspicion with the appropriate authorities per General Guidelines Mandatory Reporting or agency guidelines.\n"
      "- For children, the Colorado Child Abuse and Neglect Hotline is 1-844-CO-4-KIDS (844-264-5437).")
