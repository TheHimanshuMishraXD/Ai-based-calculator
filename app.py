import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY IS MISSING!")

client = Groq(api_key=GROQ_API_KEY)

# Active chat completion models from your account
ACTIVE_MODELS = [
    "openai/gpt-oss-20b",
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-120b",
    "allam-2-7b"
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

        # Try supported LLMs in priority order
        for model_id in ACTIVE_MODELS:
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
                print(f"[LOG] Model {model_id} failed: {err}")
                continue

        return jsonify({"result": "No responsive model found"})

    except Exception as e:
        return jsonify({"result": f"Groq Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)