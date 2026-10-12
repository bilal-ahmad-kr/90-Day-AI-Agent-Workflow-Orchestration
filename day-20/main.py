import ollama

def generate_email_replies(received_email):
    prompt = f"""Read this incoming emails and generate 5 reply options:
    1. Professional
    2. Friendly
    3. Concise

    4. Formal
    5. Casual

    Incoming Email:
    "{received_email}"
    
    Format your response clearly separating the 5 options.
    """

    response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response['message']['content']
# Test the assistant
email = "Hey, are we still meeting for the project sync tomorrow at 3 pm?" \
"Please confirm your availability."
replies = generate_email_replies(email)
print(replies)