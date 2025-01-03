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
# 2090 TRACHEOSTOMY EMERGENCIES
# ---------------------------

# Unconnected block: ETT Recommended Sizes - Length Based
print("ETT Recommended Sizes - Length Based:\n"
      "- Color Pink to Blue (Newborn to <7 years): 3.5 cuffed\n"
      "- Color Orange to Adult (7 years and up): 6.0 cuffed\n")

# Unconnected block: Stomas <6 weeks old
print("Stomas <6 weeks old:\n"
      "- An established tracheostomy is a tracheostomy that was surgically placed longer than 6 weeks ago. Never replace anything into a stoma that is less than 6 weeks of age.\n"
      "- For stomas <6 weeks old, if patient has an upper airway, occlude stoma and BVM via traditional method. If patient does not have an upper airway, use neonatal mask over stoma site.\n")

# Unconnected block: General Tracheostomy Guidelines
print("General Tracheostomy Guidelines:\n"
      "- Always utilize family members, both for information and for assistance\n"
      "- Types of tracheostomies include cuffed, uncuffed, fenestrated (allowing for speech), and unfenestrated\n"
      "- Ask if family has a suction catheter and use theirs if available to ensure appropriate size. If none available, inquire as to size. If size unknown, estimate by doubling the inner diameter of the tracheostomy tube and rounding down to the available size catheter\n"
      "- Never force suction catheter. When inserting, allow catheter to gently follow the curvature of the tracheostomy\n"
      "- If tracheostomy tube is a double lumen tube, the inner cannula must be in place to attach the bag-valve mask. Remove the inner cannula to suction and then re-insert. If outer flange becomes removed, it requires a Paramedic to replace.\n"
      "- Apply suction only while withdrawing catheter from the tracheostomy tube, never during insertion and always <100mmHg of suction\n")

# Step 1: Adult or Pediatric Universal Respiratory Distress Protocol
EMT_action("Adult or Pediatric Universal Respiratory Distress Protocol")

# Branch: Tracheostomy in Place or Removed
tracheostomy_status = "in_place"  # Example variable: can be "in_place" or "removed"

if tracheostomy_status == "in_place":
    EMT_action("Tracheostomy in Place")
    EMT_action("Attempt repositioning and supplemental oxygen")

    # If gurgling, rhonchi, or mucous present
    AEMT_action("If gurgling, rhonchi, or mucous present:\n"
                "- Preoxygenate with 3-5 BVM breaths\n"
                "- If inner cannula present, remove while stabilizing tracheostomy flange\n"
                "- Measure suction catheter to length of inner cannula (generally 3-6 cm)\n"
                "- Instill 1-2 mL saline and suction for ≤10 seconds\n"
                "- Replace inner cannula if removed\n"
                "- Begin ventilations with supplemental oxygen through tracheostomy")

    # If patient still has signs of inadequate oxygenation and ventilation
    Paramedic_action("If patient still has signs of inadequate oxygenation and ventilation:\n"
                     "- Remove tracheostomy, deflating cuff if needed\n"
                     "- If patient has additional tracheostomy tubes readily available, gently insert the same size tracheostomy tube with the obturator in place. Do not force the tube.\n"
                     "- If the tracheostomy tube cannot be inserted easily, withdraw the tube, and attempt to pass a smaller size tracheostomy tube, if available.\n"
                     "- If smaller tracheostomy tube is not available, or cannot be inserted easily, place ETT in stoma if trach is mature (at least 6 weeks old) and advance until balloon is within trachea\n"
                     "- Confirm placement by continuous waveform capnography, presence, and symmetry of breath sounds, and rising SpO2")

elif tracheostomy_status == "removed":
    EMT_action("Tracheostomy Removed")
    Paramedic_action("- Attempt to replace the tracheostomy tube if trach is mature (at least 6 weeks old)"
                     "- If the tracheostomy tube cannot be inserted easily, withdraw the tube, and attempt to pass a smaller size tracheostomy tube, if available."
                     "- If smaller tracheostomy tube is not available, or cannot be inserted easily, place ETT in stoma if trach is mature (at least 6 weeks old) and advance until balloon is within trachea"
                     "- Confirm placement by continuous waveform capnography, presence, and symmetry of breath sounds, and rising SpO2")
    EMT_action("If unable to place tube and patient hypoxic or in respiratory distress, begin BVM over nose and mouth and occlude the stoma with a gloved finger")
    EMT_action("If unable to oxygenate or ventilate, attempt to place advanced airway through mouth and occlude stoma with gloved finger.")
    EMT_I_action("If oral ETT is performed, advance ETT balloon below level of stoma")

# Final Step: Continue monitoring and assessment
EMT_action("Transport in position of comfort and monitor\n"
           "Reassess for signs of deterioration\n"
           "Provide oxygen and ventilator support as needed\n"
           "Contact Base if patient is not improving with treatment")
