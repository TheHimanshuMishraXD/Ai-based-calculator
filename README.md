# 🧮 AI-Powered Glassmorphism Calculator

An ultra-modern, glassmorphic calculator web application powered by **Flask** and **Groq AI**. Features real-time AI problem solving, an interactive history panel, full keyboard shortcut integration, and a terminal-style developer footer.

🚀 **Live Demo:** [https://ai-based-calculator-wymb.vercel.app/](https://ai-based-calculator-wymb.vercel.app/)

---

## ✨ Key Features

- **🤖 Groq AI Assistance:** Ask complex word problems or natural language math questions in the prompt box.
- **🎨 Glassmorphism UI:** Neon gradient accents, clean typography, and a dark glass aesthetic.
- **📜 Interactive History Panel:** Keep track of past calculations and click any result to reuse it.
- **⌨️ Keyboard Shortcuts:** Complete numpad, operator, backspace (`Backspace`), clear (`Esc`), and evaluate (`Enter`) support.
- **💻 Developer Terminal Footer:** Live pulse status indicator and custom Git-style branding.
- **📱 Fully Responsive:** Smooth experience across desktop, tablet, and mobile devices.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12, Flask, Groq SDK, Gunicorn
- **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript (ES6+)
- **Deployment:** Vercel (@vercel/python)

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/TheHimanshuMishraXD/Ai-based-calculator.git](https://github.com/TheHimanshuMishraXD/Ai-based-calculator.git)
cd Ai-based-calculator

2. Install Dependencies
Bash
pip install -r requirements.txt

3. Set Up Your Groq API Key
Get your free API key from Groq Console.

On Linux / macOS (Terminal):
Bash
export GROQ_API_KEY="gsk_your_actual_groq_api_key_here"
python3 app.py

On Windows (Command Prompt / CMD):
DOS
set GROQ_API_KEY=gsk_your_actual_groq_api_key_here"
python app.py


On Windows (PowerShell):
PowerShell
$env:GROQ_API_KEY="gsk_your_actual_groq_api_key_here"
python app.py

Then open http://localhost:5000 in your browser.

Running on Android (Termux)
If you want to run the server locally on an Android phone:
Install Termux and run:
Bash
pkg update && pkg upgrade -y
pkg install python git -y

Clone repo and install requirements:

1.Bash
git clone [https://github.com/TheHimanshuMishraXD/Ai-based-calculator.git](https://github.com/TheHimanshuMishraXD/Ai-based-calculator.git)
cd Ai-based-calculator
pip install -r requirements.txt

2.Export Key & Run:

Bash
export GROQ_API_KEY="your_groq_api_key_here"
python app.py

👨‍💻 Developer & Author
Designed & Built with ❤️ by Himanshu Mishra

GitHub: @TheHimanshuMishraXD

Live App: AI Calculator on Vercel

---

### Terminal Commands to Update README on GitHub:

run this command on vs code terminal:

```bash
# 1. README.md file
git add README.md

# 2. Commit 
git commit -m "Docs: Update README with Vercel live demo, local setup, and mobile guide"

# 3. Push to GitHub
git push origin main
