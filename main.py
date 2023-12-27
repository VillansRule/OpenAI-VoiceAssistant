import openai
import requests
import pygame
import time
import os

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Set your ElevenLabs API key
elevenlabs_api_key = "your_elevenlabs_api_key"

# File path for storing conversation history
history_file_path = "conversation_history.txt"

# Function to generate a response using OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to convert text to speech using ElevenLabs API
def text_to_speech(text):
    # Your ElevenLabs text-to-speech logic here
    pass

# Function to load conversation history from a file
def load_history():
    history = []
    if os.path.exists(history_file_path):
        with open(history_file_path, "r") as file:
            history = file.readlines()
    return history

# Function to save conversation history to a file
def save_history(history):
    with open(history_file_path, "w") as file:
        file.writelines(history)

# Main conversation loop
def conversation():
    print("Welcome! Type 'exit' to end the conversation.")
    user_input = ""
    history = load_history()

    while user_input.lower() != "exit":
        user_input = input("You: ")

        # Generate OpenAI response
        prompt = f"You said: {user_input}\n"
        response = generate_response(prompt)

        # Append the current conversation to history
        history.append(f"You: {user_input}\nAI: {response}")

        # Output OpenAI response
        print(f"AI: {response}")

        # Convert OpenAI response to speech
        text_to_speech(response)

    # Save the entire conversation history when the user exits
    save_history(history)
    print("\nConversation History:")
    for entry in history:
        print(entry)

if __name__ == "__main__":
    pygame.init()
    conversation()
