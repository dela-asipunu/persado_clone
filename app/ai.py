import google.generativeai as genai
import os

# Set up API key (store it in an environment variable for security)
genai.configure(api_key="AIzaSyAOuzKr9EnoOdGvyF2dXe54oi8KIWeohJo")

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_response(prompt):
    """Generate a response using the Gemini model"""
    structured_prompt = f"""
    Please provide a detailed response to the following prompt:
    "{prompt}"
    
    Format the response with:
    - Paragraphs for explanations
    - Bullet points for key points
    - Use clear and concise language
    """
    response = model.generate_content(structured_prompt)
    return response.text  # Extract text from the response

