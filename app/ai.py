import google.generativeai as genai
import os

# Set up API key (store it in an environment variable for security)
genai.configure(api_key="AIzaSyAOuzKr9EnoOdGvyF2dXe54oi8KIWeohJo")

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_response(prompt):
    """Generate a response using the Gemini model"""
    response = model.generate_content(prompt)
    return response.text  # Extract text from the response

