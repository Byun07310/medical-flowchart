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
# 5050 SNAKE BITE PROTOCOL
# ---------------------------

# Step 1: Assess patient and initiate general care
EMT_action("Assess ABCs, mental status\n"
           "- Administer oxygen\n"
           "- Start IV\n"
           "- Monitor VS")
EMT_action("Initiate general care for snake bites")

# Step 2: Assess for localized vs. systemic signs and symptoms
EMT_action("Assess for localized vs. systemic signs and symptoms")

# Branch: Localized Symptoms or Systemic Symptoms
symptom_type = "Localized"  # Example input: "Localized" or "Systemic"

if symptom_type == "Localized":
    EMT_action("Localized Symptoms:\n"
               "- Pain and swelling\n"
               "- Numbness, tingling to bitten part\n"
               "- Bruising/ecchymoses")
    EMT_action("Consider pain management")

elif symptom_type == "Systemic":
    EMT_action("Systemic Symptoms:\n"
                "- Metallic or peculiar taste in mouth\n"
                "- Hypotension\n"
                "- Altered mental status\n"
                "- Widespread bleeding\n"
                "- Other signs of shock")
    EMT_action("Be prepared to manage airway if signs of airway obstruction develop")
    EMT_action("Consider pain management")
    EMT_action("If there is hypotension for age and/or definite signs of shock, treat per Medical Shock protocol")

# Final Step: Transport protocol
EMT_action("Transport with bitten part immobilized\n"
           "- Monitor ABCs and for development of systemic signs/symptoms\n"
           "- Complete General Care en route")

# Unconnected block: General Care
print("General Care:\n"
      "- Remove patient from proximity to snake\n"
      "- Remove all constricting items from bitten limb (e.g., rings, jewelry, watch, etc.)\n"
      "- Immobilize bitten part\n"
      "- Do NOT use ice, refrigerants, tourniquets, scalpels, or suction devices\n"
      "- Mark margins of erythema and/or edema with pen or marker and include time measured")

# Unconnected block: Obtain specific information
print("Obtain Specific Information:\n"
      "- Appearance of snake (rattle, color, thermal pit, elliptical pupils)\n"
      "- Appearance of wound: location, # of fangs vs. entire jaw imprint\n"
      "- Timing of bite\n"
      "- Prior first aid\n"
      "- To help with identification of snake, photograph snake, if possible. Include image of head, tail, and any distinctive markings\n"
      "- Do not bring snake to ED")

# Unconnected block: Specific Precautions
print("Specific Precautions:\n"
      "- The prairie rattlesnake is native to Denver Metro region and is most common venomous snake bite in the region.\n"
      "- Exotic venomous snakes, such as pets or zoo animals, may have different signs and symptoms than those of pit vipers. In case of exotic snake bite, contact base and consult zoo staff or poison center for direction.\n"
      "- Take a picture of the snake, including images of head and tail. If an adequate photo can be taken, it is not necessary to bring snake to ED.\n"
      "- Never pick up a presumed-to-be-dead snake by hand. Rather, use a shovel or stick. A dead snake may reflexively bite and envenomate.\n"
      "- 25% of snake bites are 'dry bites,' without envenomation.\n"
      "- Conversely, initial appearance of bite may be deceiving as to severity of envenomation.\n"
      "- Fang marks are characteristic of pit viper bites (e.g., rattlesnakes).\n"
      "- Jaw prints, without fang marks, are more characteristic of non-venomous species.")
