import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY IS MISSING! Export it in terminal.")

client = Groq(api_key=GROQ_API_KEY)

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

        # Updated to active Groq model
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI calculator backend. Give a short, ultra-concise, "
                        "direct response suitable for a calculator display screen. "
                        "If it is a math problem, show the formula or step briefly and the final numerical answer."
                    )
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.2,
            max_tokens=100
        )

        response_text = completion.choices[0].message.content.strip()
        return jsonify({"result": response_text})

    except Exception as e:
        return jsonify({"result": f"Groq Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)