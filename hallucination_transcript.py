import re

def extract_numbers(text):
    # Extract all numbers from the text
    return [int(match.group()) for match in re.finditer(r'\d+', text)]

def check_numbers_match(summary, transcript):
    # Extract numbers from both summary and transcript
    summary_numbers = extract_numbers(summary)
    transcript_numbers = extract_numbers(transcript)
    
    # Check if the numbers in the summary match those in the transcript
    return all(number in transcript_numbers for number in summary_numbers)

# Given summary1 and transcript1
summary1 = "The customer called ABC to check their account balance. The agent confirmed the customer's account number and informed them that their current balance is $100. The customer then inquired about upcoming transactions and the agent informed them that they have a direct deposit of $50 scheduled for May 13th. The customer thanked the agent for their help and ended the call."

transcript1 = "Customer: \"Hello, I'd like to check my account balance.\"\nAgent: \"Thank you for calling ABC. May I have your account number, please?\"\nCustomer: \"Sure, it's 1234567890.\"\nAgent: \"Thank you. Your current account balance is $100.\"\nCustomer: \"Thank you. Can you also tell me if there are any upcoming transactions?\"\nAgent: \"Yes, you have a direct deposit of $50 scheduled for 12th May.\"\nCustomer: \"Thank you for your help.\"\nAgent: \"You're welcome. Is there anything else I can help you with today?\"\nCustomer: \"No, that's all for now.\"\nAgent: \"Okay, thank you for calling ABC. Have a great day!\"\nCustomer: \"You too.\""

# Check if the numbers in summary1 match those in transcript1
numbers_match = check_numbers_match(summary1, transcript1)

if numbers_match:
    print("Numbers in summary1 match the transcript1.")
else:
    print("Numbers in summary1 do not match the transcript1.")
