def normalize_text(text):
    # Case normalization, converting all text to lowercase except for specific words
    specific_words = ['ACCOUNT', 'ABC']
    words = text.split()
    normalized_words = [word.lower() if word.upper() not in specific_words else word.upper() for word in words]
    normalized_text = ' '.join(normalized_words)

    # Whitespace normalization, removing extra spaces, tabs, and line breaks
    normalized_text = ' '.join(normalized_text.split())

    return normalized_text

# Given transcript1
transcript1 = "Customer: \"Hello, I'd like to check my account balance.\"\nAgent: \"Thank you for calling ABC. May I have your account number, please?\"\nCustomer: \"Sure, it's 1234567890.\"\nAgent: \"Thank you. Your current account balance is $100.\"\nCustomer: \"Thank you. Can you also tell me if there are any upcoming transactions?\"\nAgent: \"Yes, you have a direct deposit of $50 scheduled for 12th May.\"\nCustomer: \"Thank you for your help.\"\nAgent: \"You're welcome. Is there anything else I can help you with today?\"\nCustomer: \"No, that's all for now.\"\nAgent: \"Okay, thank you for calling ABC. Have a great day!\"\nCustomer: \"You too.\""

# Normalize the transcript text
normalized_transcript = normalize_text(transcript1)

# Print the normalized text
print("Normalized Transcript:")
print(normalized_transcript)
