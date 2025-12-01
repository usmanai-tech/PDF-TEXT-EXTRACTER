# import os
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from the environment variables
# api_key = os.getenv("GROQ_API_KEY")

# # Check if the API key was loaded successfully
# if not api_key:
#     raise ValueError("API key is missing from the .env file.")

# # Define the system prompt for the model
# system_prompt = """
# Your task is to clean the data first according to legal deed documents, which may be in English or Spanish, and accurately extract the following details:

# Date of Sale: The official date when the property was sold.
# Sales Price: The monetary value agreed upon for the sale of the property.
# Seller's Name: The individual(s) or entity selling the property.
# Buyer's Name: The individual(s) or entity purchasing the property.
# Cadaster Number: If available, extract the unique identifier for the property in official land registries.
# Development Name: The name of the housing development or community where the property is located, if specified.
# Unit Number: The designated number for the specific property unit, if applicable.
# Lot Size: The size of the land or property lot, typically mentioned in square feet or meters.
# Bedrooms and Bathrooms: The total number of bedrooms and bathrooms in the property.
# Parking Spaces: The number of parking spaces included with the property.

# Ensure accurate extraction from both English and Spanish documents while maintaining focus on relevant details.
# """

# def process_with_groq_model(text: str):
#     client = Groq(api_key=api_key)

#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": text},
#         ],
#         model="llama-3.3-70b-versatile",
#         temperature=0.5,
#         max_tokens=1024,
#         top_p=1,
#         stop=None,
#         stream=False,
#     )

#     # Return the response from the model
#     return chat_completion.choices[0].message.content














import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("GROQ_API_KEY")

# Check if the API key was loaded successfully
if not api_key:
    raise ValueError("API key is missing from the .env file.")

# Define the system prompt for the model
system_prompt = """
Your task is to clean the data first according to legal deed documents, which may be in English or Spanish, and accurately extract the following details:

Date of Sale: The official date when the property was sold.
Sales Price: The monetary value agreed upon for the sale of the property.
Seller's Name: The individual(s) or entity selling the property.
Buyer's Name: The individual(s) or entity purchasing the property.
Cadaster Number: If available, extract the unique identifier for the property in official land registries.
Development Name: The name of the housing development or community where the property is located, if specified.
Unit Number: The designated number for the specific property unit, if applicable.
Lot Size: The size of the land or property lot, typically mentioned in square feet or meters.
Bedrooms and Bathrooms: The total number of bedrooms and bathrooms in the property.
Parking Spaces: The number of parking spaces included with the property.

Ensure accurate extraction from both English and Spanish documents while maintaining focus on relevant details.
"""

# Function to chunk text into smaller pieces of 2000 characters
def chunk_text(text, chunk_size=2000):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def process_with_groq_model(text: str):
    client = Groq(api_key=api_key)

    # Chunk the extracted text into smaller pieces
    text_chunks = chunk_text(text)

    # Initialize a list to store the model's responses
    full_response = []

    # Send each chunk to the model
    for chunk in text_chunks:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": chunk},
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        # Collect the model's response
        full_response.append(chat_completion.choices[0].message.content)

    # Combine all the responses into one full response
    return "\n".join(full_response)
