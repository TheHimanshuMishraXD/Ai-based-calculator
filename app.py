import os
from flask import Flask, render_template, request, jsonify
from google import genai        
app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("warning GEMINI_API_KEY IS MISSING MAKE SURE TO IMPORT IT IN TERMINAL.")

client =genai.Client(api_key=GEMINI_API_KEY)

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
        response = client.models.generate_content(
            model = 'gemini-2.5-flash' ,
            contents=user_prompt,
            config={
                
            }
            
        )
        result = eval(user_prompt)
        return jsonify({"result": str(result)})

    except Exception:
        return jsonify({"result": "Invalid Expression"})

if __name__ == "__main__":
    app.run(debug=True)

# jsonify → Python ke result ko wapas JSON format mein JavaScript ke paas bhejne ke liye.