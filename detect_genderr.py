import re

def detect_gender(transcript):
    # Extract titles, pronouns, and directly addressed terms from the transcript
    titles = re.findall(r"(?:Mr|Ms|Miss|Mrs)\.", transcript)
    pronouns = re.findall(r"(?:he|she|his|hers|him|her)", transcript)
    addressed_terms = re.findall(r"(?:mam|sir)", transcript, flags=re.IGNORECASE)

    # Determine gender based on directly addressed terms
    if addressed_terms:
        if "mam" in addressed_terms:
            return "female"
        elif "sir" in addressed_terms:
            return "male"
        else:
            return None

    # If no directly addressed terms are found, proceed with title and pronoun-based detection
    else:
        # Determine gender based on titles
        if titles:
            if titles[0] == "Mr.":
                return "male"
            elif titles[0] in ["Ms.", "Miss", "Mrs."]:
                return "female"
            else:
                return None

        # Determine gender based on pronouns
        elif pronouns:
            male_pronouns = ["he", "his", "him"]
            female_pronouns = ["she", "hers", "her"]

            male_pronoun_count = sum(1 for pronoun in pronouns if pronoun in male_pronouns)
            female_pronoun_count = sum(1 for pronoun in pronouns if pronoun in female_pronouns)

            if male_pronoun_count > female_pronoun_count:
                return "male"
            elif male_pronoun_count < female_pronoun_count:
                return "female"
            else:
                return None

        # If no titles or pronouns are found, return None
        else:
            return None

# Example usage
transcript = "Customer: \"Hello, I'd like to check my account balance.\"\nAgent: \"Thank you mam for calling ABC. May I have your account number, please?\"\nCustomer: \"Sure, it's 1234567890.\"\nAgent: \"Thank you. Your current account balance is $100.\"\nCustomer: \"Thank you. Can you also tell me if there are any upcoming transactions?\"\nAgent: \"Yes, you have a direct deposit of $50 scheduled for 12th may.\"\nCustomer: \"Thank you for your help.\"\nAgent: \"You're welcome. Is there anything else I can help you with today?\"\nCustomer: \"No, that's all for now.\"\nAgent: \"Okay, thank you for calling ABC. Have a great day!\"\nCustomer: \"You too.\""

gender = detect_gender(transcript)
print(gender)
