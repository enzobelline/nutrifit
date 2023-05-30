import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define the list of user inputs
user_inputs = [
    "What's the weather like today?",
    "Tell me a joke.",
    "What are some good movie recommendations?",
    "How do I make a pizza from scratch?"
]

# Open the output file in write mode
output_file = open("output.txt", "w")

# Iterate over the user inputs
for user_input in user_inputs:
    # Define the conversation history with system and user messages
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    # Send the conversation to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Retrieve the assistant's reply from the response
    assistant_reply = response['choices'][0]['message']['content']

    # Write the assistant's reply to the output file
    output_file.write(assistant_reply + "\n")

# Close the output file
output_file.close()

print("Output file 'output.txt' has been generated.")