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
# 3040 TACHYARRHYTHMIA WITH POOR PERFUSION
# ---------------------------

# Step 1: Tachyarrhythmia
EMT_action("Tachyarrhythmia")
EMT_action("- Support ABCs\n"
           "- IV access\n"
           "- Give oxygen")
EMT_I_action("12 lead ECG")

# Step 2: Probable Sinus Tachycardia?
EMT_action("Probable Sinus Tachycardia?\n"
           "- Adult: rate usually <150\n"
           "- Children: rate usually <180\n"
           "- Infants: rate usually <220")
response = "No"  # Example response directly from flowchart

if response == "Yes":
    EMT_action("Search for and treat underlying cause: e.g. dehydration, fever, hypoxia, hypovolemia, pain\n"
               "Consider medical shock")

elif response == "No":
    # Step 3: Is patient stable?
    EMT_action("Is patient stable?\n"
               "Unstable signs include altered mental status, chest pain, hypotension, signs of shock-rate-related symptoms uncommon if HR <150 in adults")
    response = "Stable"  # Example response directly from flowchart

    if response == "Stable":
        # Step 4: Stable Branch
        EMT_action("Stable\n"
                   "- Identify Rhythm\n"
                   "- Measure QRS width")
        QRS_width = "Narrow"  # Example response: Narrow or Wide

        if QRS_width == "Narrow":
            EMT_action("Narrow QRS\n"
                       "- Adult <120 msec\n"
                       "- Pediatric <90 msec")
            # Regular or Irregular for Narrow QRS
            rhythm_type = "Regular"  # Example: Regular or Irregular

            if rhythm_type == "Regular":
                Paramedic_action("Regular")
                EMT_action("Children who are stable with AVNRT generally remain so and transport is preferred over intervention")
                Paramedic_action("- Try Valsalva maneuver\n"
                                 "- Give adenosine IV if suspected AV nodal reentrant tachycardia (AVNRT)")
                EMT_action("- EMT-I requires direct order for adenosine")

                # Final Steps: Convert or Doesn't Convert
                response = "Convert" # Example response: Convert or Doesn't Convert
                if response == "Convert":
                    EMT_I_action("Convert\n"
                                 "Repeat 12 lead ECG\n"
                                 "Monitor in transport\n"
                                 "If recurrent dysrhythmia, go to unstable pathway")

                elif response == "Doesn't Convert":
                    EMT_action("Contact Base for consult\n"
                               "Monitor in transport\n"
                               "If unstable, go to unstable pathway")

            elif rhythm_type == "Irregular":
                EMT_action("Irregular\n"
                           "- Atrial fibrillation, flutter, or MAT\n"
                           "- Do not give adenosine\n"
                           "- If becomes unstable go to unstable pathway")

        elif QRS_width == "Wide":
            EMT_action("Wide QRS\n"
                       "- Adult >120 msec\n"
                       "- Pediatric >90 msec")
            # Regular or Irregular for Wide QRS
            rhythm_type = "Regular"  # Example: Regular or Irregular

            if rhythm_type == "Regular":
                EMT_I_action("Regular")
                EMT_action("- Contact Base for consult")
                EMT_I_action("- V Tach (>80%) or SVT with aberrancy\n"
                           "- Contact Base for verbal order for amiodarone unless contraindicated")
                Paramedic_action("- If regular and polymorphic (Torsades de Pointes) consider magnesium")

            elif rhythm_type == "Irregular":
                EMT_action("Irregular\n"
                           "- See box C\n"
                           "- Contact Base for consult\n"
                           "- Do not give adenosine")

    elif response == "Unstable":
        # Step 5: Unstable Branch
        Paramedic_action("Unstable\n"
                         "Immediate synchronized cardioversion")
        EMT_I_action("Repeat 12 lead ECG\n"
                    "identify rhythm\n"
                    "Contact Base")
