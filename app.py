import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Key check
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
client = Groq(api_key=GROQ_API_KEY)

# Confirmed active general models from your list
ACTIVE_MODELS = [
    "openai/gpt-oss-20b",
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-120b"
]

@app.route("/")
def home():
    return render_template("calc.html")

@app.route("/ask-ai", methods=["POST"])
def ask_ai():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"result": "Invalid JSON input"}), 400
            
        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({"result": "Empty prompt"})

        for model_id in ACTIVE_MODELS:
            try:
                completion = client.chat.completions.create(
                    model=model_id,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a concise calculator backend. Return short numerical or formula outputs."
                        },
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    temperature=0.2,
                    max_tokens=100
                )
                res = completion.choices[0].message.content.strip()
                return jsonify({"result": res})
            except Exception as err:
                print(f"[ERROR] {model_id}: {err}")
                continue

        return jsonify({"result": "All active models failed"})

    except Exception as e:
        print(f"[CRITICAL SERVER ERROR]: {e}")
        return jsonify({"result": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)