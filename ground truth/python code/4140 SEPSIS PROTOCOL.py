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
# 4140 SEPSIS PROTOCOL
# ---------------------------

# Step 1: Evaluate and identify potential sepsis
EMT_action("Evaluate and identify potential sepsis – is there suspected or confirmed infection?")
EMT_action("- ABCs\n"
           "- Complete set of vital signs\n"
           "- Monitoring including SpO2 and waveform capnography\n"
           "- O2 as appropriate")

# Step 2: Evaluate potential SIRS Criteria
EMT_action("Evaluate potential SIRS Criteria:\n"
           "- Temperature < 36C (96.8F) or > 38C (100.4F)\n"
           "- Heart rate > 90 (or tachycardic for age)\n"
           "- Respiratory rate > 20 or mechanical ventilation (or tachypneic for age)\n"
           "Are there two or more SIRS criteria?")
SIRS_criteria = "Yes"  # Example response: Yes or No

if SIRS_criteria == "No":
    EMT_action("Routine Care:\n"
               "- IV, O2, monitor\n"
               "- Consider fluid bolus if sepsis suspected\n"
               "- Transport to closest appropriate hospital\n"
               "- Continue to re-assess vital signs and perfusion")

elif SIRS_criteria == "Yes":
    # Step 3: Is there evidence of hypoperfusion?
    EMT_action("Is there evidence of hypoperfusion? (ANY ONE OF THE FOLLOWING):\n"
               "- Hypotension for age\n"
               "- Altered mental status (excluding simple febrile seizure)\n"
               "- Delayed capillary refill AND mottling\n"
               "- Systolic BP < 90 mmHg\n"
               "- MAP < 65 mmHg\n"
               "- Sustained EtCO2 < 25 mmHg")
    hypoperfusion = "Yes"  # Example response: Yes or No

    if hypoperfusion == "No":
        EMT_action("Routine Care:\n"
                   "- IV, O2, monitor\n"
                   "- Consider fluid bolus if sepsis suspected\n"
                   "- Transport to closest appropriate hospital\n"
                   "- Continue to re-assess vital signs and perfusion")
    elif hypoperfusion == "Yes":
        # Step 4: Fluid bolus and transport
        EMT_action("IV fluid bolus @ 30 mL/kg, frequently assess hemodynamics and lung sounds for pulmonary edema (approx. each 10 mL/kg)\n"
                     "2 large bore IVs\n"
                     "Transport to closest appropriate hospital")
        EMT_action("NOTIFY HOSPITAL of potential sepsis (hospital activation criteria may vary)")
        Paramedic_action("For ongoing hypotension, poor perfusion, or pulmonary edema, consider vasopressor")

# Unconnected block: Common Infection Sites with Severe Sepsis
print("Common Infection Sites with Severe Sepsis:\n"
      "- Respiratory\n"
      "- Bacteremia (unspecified site)\n"
      "- Genitourinary (more prevalent with females)\n"
      "- Abdominal\n"
      "- Device-related\n"
      "- Soft tissue/wound\n"
      "- Central nervous system\n"
      "- Endocarditis")

# Unconnected block: Principles of Sepsis
print("Principles of Sepsis:\n"
      "- Multiple studies demonstrate the benefit of early recognition and treatment of sepsis, including in the prehospital setting\n"
      "- Early hospital notification of sepsis may lead to shorter time to IV fluid and IV antibiotics and increase survival\n"
      "- Patients with septic shock require aggressive IV fluid resuscitation. Starting dose should be 30mL/kg of IV fluid\n"
      "- EtCO2 has been demonstrated to correlate with serum lactate levels and predictive of severity of sepsis. A sustained EtCO2 < 25 mmHg may indicate hypoperfusion\n"
      "- Some agencies may carry lactate monitors. In that case, a lactate level of >=4 mmol/L is indicative of hypoperfusion")

# Unconnected block: Pediatric Fluid Administration
print("Pediatric Fluid Administration:\n"
      "- For children <40 kg or not longer than length-based tape, hand pull/push fluid with a 60 mL syringe utilizing a 3 way stop cock\n"
      "- The treatment of compensated shock requires aggressive fluid replacement, may need to repeat fluid bolus up to 60mL/kg\n"
      "- Goal of therapy is normalization of vital signs within the first hour\n"
      "- Hypotension is a late sign in pediatric shock patients")
