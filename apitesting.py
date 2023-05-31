import openai

# Set up your OpenAI API credentials
openai.api_key = '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'
promptFilePath = "promptGeneration.txt"
responseFilePath = "responseGeneration.txt"

with open(promptFilePath, "r") as file:
    prompts = file.readlines()  # Read all lines from the file into a list

# Remove newlines and whitespace characters from each line
user_inputs = [prompt.strip() for prompt in prompts]


# Open the output file in write mode
output_file = open("output.txt", "w")

# Iterate over the user inputs
for user_input in user_inputs:
    # Define the conversation history with system and user messages
    conversation = [
        {"role": "system", "content": "You are a fitness and nutrition expert."},
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

