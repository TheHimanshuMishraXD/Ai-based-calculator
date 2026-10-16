import os
import time
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route("/")
def home():
    return render_template("calc.html")

@app.route("/ask-ai", methods=["POST"])
def ask_ai():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({"result": "Empty prompt"})

        # Retry logic for 503 high demand spikes
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=(
                            "You are an AI calculator backend. Give a short, ultra-concise, "
                            "direct response suitable for a calculator display screen."
                        )
                    )
                )
                return jsonify({"result": response.text.strip()})
            except Exception as e:
                if "503" in str(e) and attempt < max_retries - 1:
                    time.sleep(1.5)  # 1.5 seconds wait karke retry karega
                    continue
                raise e

    except Exception as e:
        return jsonify({"result": "Server Busy, Try Again!"})

if __name__ == "__main__":
    app.run(debug=True)