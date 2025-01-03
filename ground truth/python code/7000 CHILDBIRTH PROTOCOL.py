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
# 7000 CHILDBIRTH PROTOCOL
# ---------------------------

# Step 1: Initial steps and overview
EMT_action("ABCs\nO2 15 liters via NRB\nIV access")

# Step 2: Obtain obstetrical history
EMT_action("Obtain obstetrical history (see adjacent)")
EMT_action("Specific Information Needed:\n"
           "- Number of pregnancies (gravida)\n"
           "- Live births (PARA)\n"
           "- Expected delivery date\n"
           "- Length of previous labors\n"
           "- Narcotic use in past 4 hours")

# Step 3: Suspected imminent childbirth?
EMT_action("If suspected imminent childbirth:\n"
           "- Allow patient to remain in position of comfort\n"
           "- Visualize perineum\n"
           "- Determine if there is time to transport")
response = "Imminent"  # Example response: Imminent or Not Imminent

if response == "Imminent":
    # Step 4: Emergency childbirth procedure
    EMT_action(" Imminent Delivery\n"
               "Delivery is imminent if there is crowning or bulging of perineum")
    EMT_action("Emergency Childbirth Procedure:\n"
               "- If there is a prolapsed umbilical cord or apparent breech presentation, go to obstetrical complications protocol and initiate immediate transport.\n"
               "- For otherwise uncomplicated delivery:\n"
               "  - Position mother supine on flat surface, if possible.\n"
               "  - Do not attempt to impair or delay delivery.\n"
               "  - Support and control delivery of head as it emerges.\n"
               "  - Protect perineum with gloved hand.\n"
               "  - Check for cord around neck, remove from around neck, if present.\n"
               "  - Suction mouth and nose only if signs of obstruction by secretions.\n"
               "  - If delivery not progressing, baby is 'stuck', see obstetrical complications protocol and begin immediate transport.\n"
               "  - As shoulders emerge, gently guide head and neck downward to deliver anterior shoulder. Support and gently lift the head and neck to deliver posterior shoulder.\n"
               "  - Rest of infant should deliver with passive participation – get a firm hold on baby.\n"
               "  - Dry baby and place skin-to-skin on the mother. Assess breathing, tone, and activity.")

    # Nested if-else: Postpartum care for infant or mother
    postpartum_care = "Infant"  # Example response: Infant or Mother

    if postpartum_care == "Infant":
        EMT_action("Postpartum Care Infant:\n"
                   "- Suction mouth and nose only if signs of obstruction by secretions.\n"
                   "- Respirations should begin within 15 seconds after stimulating reflexes. If not, begin artificial ventilations at 40-60 breaths/min.\n"
                   "- If apneic, cyanotic, or HR < 100, begin neonatal resuscitation.\n"
                   "- Healthy term babies should be managed skin-to-skin with their mothers. After birth, the baby should be dried and directly placed skin-to-skin with attention to warm coverings and maintenance of normal temperature.\n"
                   "- Clamp the cord after the infant is quickly dried, placed on the mother, and assessed for breathing and activity. Double clamp 6” from infant abdominal wall and cut between clamps with sterile scalpel. If no sterile cutting instrument available, lay infant on mother and do not cut clamped cord.\n"
                   "- Document 1- and 5-minute APGAR scores.\n"
                   "- Keep the baby covered, including cap over the head.")
    else:
        EMT_action("Postpartum Care Mother:\n"
                   "- Placenta should deliver in 20-30 minutes. If delivered, collect in plastic bag and bring to hospital. Do not pull cord to facilitate placenta delivery and do not delay transport awaiting placenta delivery.\n"
                   "- If the perineum is torn and bleeding, apply direct pressure with sanitary pads.\n"
                   "- Postpartum hemorrhage – see obstetrical complications protocol.\n"
                   "- Initiate transport once delivery of child is complete and mother can tolerate movement.")
else:
    EMT_action("Delivery not imminent:\n"
               "- Transport in position of comfort, preferably on left side, to patient’s requested hospital if time and conditions allow.\n"
               "- Monitor for progression to imminent delivery.")

# Unconnected block: Overview
print("Overview:\n"
      "- EMS providers called to a possible prehospital childbirth should determine if there is enough time to transport expectant mother to hospital or if delivery is imminent.\n"
      "- If imminent, stay on scene and immediately prepare to assist with the delivery.")

# Unconnected block: Critical Thinking
print("Critical Thinking:\n"
      "- If there is an infant in distress, call for additional EMS resources to provide care to 2 patients.\n"
      "- Normal pregnancy is accompanied by higher heart rates and lower blood pressures.\n"
      "- Shock will be manifested by signs of poor perfusion.\n"
      "- Labor can take 8-12 hours, but as little as 5 minutes if high PARA.\n"
      "- The higher the PARA, the shorter the labor is likely to be.\n"
      "- High risk factors include: no prenatal care, drug use, teenage pregnancy, DM, htn, cardiac disease, prior breech or C section, preeclampsia, twins.\n"
      "- Note color of amniotic fluid for meconium staining.")
