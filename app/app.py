# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 22:46:39 2025

@author: user
"""

import os
import google.generativeai as genai
import chainlit as cl

# Configure Gemini - replace with your API key
genai.configure(api_key="AIzaSyAOuzKr9EnoOdGvyF2dXe54oi8KIWeohJo")

# Your original system instruction (paste exactly as from Google AI Studio)
SYSTEM_INSTRUCTION = """You are a Persuasive AI Marketing Linguist..."""

@cl.on_chat_start
def start_chat():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        },
        system_instruction=SYSTEM_INSTRUCTION
    )
    cl.user_session.set("chat", model.start_chat(history=[]))

@cl.on_message
async def main(message: cl.Message):
    chat = cl.user_session.get("chat")
    response = chat.send_message(message.content)
    await cl.Message(content=response.text).send()