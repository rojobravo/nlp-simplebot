import os
from openai import OpenAI

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

# WRITE YOUR CODE HERE