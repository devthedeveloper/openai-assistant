import openai

def generate_text(prompt):
    # Set up OpenAI API credentials
    openai.api_key = 'YOUR_API_KEY'

    # Generate text using OpenAI GPT-3.5 model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Set up initial conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant that generates text."},
    {"role": "user", "content": "Tell me a joke."},
    {"role": "assistant", "content": "Why don't scientists trust atoms? Because they make up everything!"}
]

while True:
    user_input = input("User: ")
    
    # Add user input to the conversation
    conversation.append({"role": "user", "content": user_input})
    
    # Generate assistant's reply
    prompt = "\n".join([f"{c['role']}: {c['content']}" for c in conversation])
    assistant_reply = generate_text(prompt)
    
    # Add assistant's reply to the conversation
    conversation.append({"role": "assistant", "content": assistant_reply})
    
    # Display assistant's reply
    print("Assistant:", assistant_reply)
