import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY IS MISSING! MAKE SURE TO EXPORT IT IN TERMINAL.")

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

        # Sahi Config passing mechanism
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are an AI calculator backend. Give a short, ultra-concise, "
                    "direct response suitable for a calculator display screen. "
                    "If it is a math problem, show the formula or step briefly and the final numerical answer."
                )
            )
        )
        
        return jsonify({"result": response.text.strip()})

    except Exception as e:
        return jsonify({"result": f"AI Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)