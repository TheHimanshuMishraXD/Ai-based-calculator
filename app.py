from flask  import Flask , render_template , request , jsonify
app = Flask(__name__)
@app.route("/")
def home():
        return render_template("calc.html")
@app.route("/ask-ai" , methods=["POST"])
def ask_ai():
      try:
        data = request.get_json() #data = request.get_json() → JavaScript se aaye hue JSON payload ko Python dictionary mein badalta hai.
#       from this line ye frontend data ko read krega
        user_prompt = data.get("prompt" , " ")

        if not user_prompt: 
             return jsonify({"result": " Empty prompt"})
        result = eval(user_prompt)
        return jsonify({"result": str(result)})       

if __name__ == "__main__":
    app.run(debug=True)  


# jsonify → Python ke result ko wapas JSON format mein JavaScript ke paas bhejne ke liye.