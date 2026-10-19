import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY IS MISSING! Export it in terminal.")

client = Groq(api_key=GROQ_API_KEY)

# Active supported models on Groq platform
MODELS_TO_TRY = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

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

        # Try active models in order
        for model_id in MODELS_TO_TRY:
            try:
                completion = client.chat.completions.create(
                    model=model_id,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an AI calculator backend. Give a short, ultra-concise, "
                                "direct response suitable for a calculator display screen."
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
            except Exception as err:
                print(f"Model {model_id} failed: {err}")
                continue

        return jsonify({"result": "All AI models failed"})

    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"result": f"Groq Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)