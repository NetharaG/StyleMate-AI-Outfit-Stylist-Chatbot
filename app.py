import streamlit as st
from dotenv import load_dotenv
import os
import ollama

# Load environment variables (optional)
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="👗 Outfit Stylist Chatbot", page_icon="🧥")
st.title("👗 Outfit Stylist Chatbot")
st.write(
    "Tell me about the event you're attending and your personal style, "
    "and I'll suggest outfits plus shopping keywords!"
)

# User input
user_input = st.text_area(
    "Describe your event + style:",
    placeholder="e.g. Beach wedding in summer; minimalist, elegant"
)

# Button to get outfit suggestions
if st.button("Get Outfit Ideas"):
    if user_input.strip():
        with st.spinner("✨ Thinking of some stylish outfits..."):
            try:
                # Call Ollama local model
                response = ollama.chat(
                    model=os.getenv("OLLAMA_MODEL", "gemma:2b"),
                    messages=[
                        {"role": "system", "content":
                         "You are a fashion stylist assistant. "
                         "When the user describes an event and their style, "
                         "suggest 3 outfit ideas (each with items/accessories) "
                         "and generate 3–5 shopping keywords."},
                        {"role": "user", "content": user_input}
                    ]
                )

                # Extract reply
                reply = response["message"]["content"]

                # Display in Streamlit
                st.markdown("### 💡 Outfit Suggestions & Keywords")
                st.write(reply)

            except Exception as e:
                st.error(f"⚠️ Something went wrong: {e}")
    else:
        st.warning("Please describe the event and your style first.")