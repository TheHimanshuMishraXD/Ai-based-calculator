import os
from flask import Flask, render_template, request, jsonify
from google import genai        
app = Flask(__name__)

GEMINI_API_KEY

@app.route("/")
def home():
    return render_template("calc.html")

@app.route("/ask-ai", methods=["POST"])
def ask_ai():
    try:
        data = request.get_json()  # JavaScript se aaye JSON payload ko Python dict mein convert karta hai
        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({"result": "Empty prompt"})

        result = eval(user_prompt)
        return jsonify({"result": str(result)})

    except Exception:
        return jsonify({"result": "Invalid Expression"})

if __name__ == "__main__":
    app.run(debug=True)

# jsonify → Python ke result ko wapas JSON format mein JavaScript ke paas bhejne ke liye.