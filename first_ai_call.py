import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_ai(question):
    """Send a question to the AI and return its answer."""

    #Create a "conversation" with one user message
    response = client.messages.create(
        model="claude-haiku-4-5-20251001", #The AI model we're using
        max_tokens=1024,
        system="You are a friendly assistant helping someone learn Python and AI.",
        messages=[
            {
                "role":"user",
                "content":question
            }
        ]
    )

    #Extract just the text of the response
    return response.content[0].text

#Ask a question
answer = ask_ai("What is Python, and why is it good for AI?")
print("Claude says:")
print(answer)