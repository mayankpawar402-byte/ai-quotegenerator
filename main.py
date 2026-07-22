from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI(title="AI Quote Generator API")


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Quote Generator API!"
    }


@app.get("/quote")
def generate_quote(topic: str = "success"):
    try:
        response = client.chat.completions.create(
            model="poolside/laguna-s-2.1:free",   
            messages=[
                {
                    "role": "system",
                    "content": "You are a motivational quote generator."
                },
                {
                    "role": "user",
                    "content": f"Generate one short motivational quote about '{topic}'. Only return the quote without quotation marks or extra explanation."
                }
            ],
            temperature=0.8,
            max_tokens=60,
        )

        quote = response.choices[0].message.content.strip()

        return {
            "topic": topic,
            "quote": quote,
            "author": "AI"
        }

    except Exception as e:
        return {
            "error": str(e)
        }