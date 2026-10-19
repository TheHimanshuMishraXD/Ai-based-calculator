document.addEventListener("DOMContentLoaded", () => {
    const aiBtn = document.getElementById("ai-btn");
    const aiPromptInput = document.getElementById("ai-prompt");
    const display = document.getElementById("display");

    // Calculator normal buttons logic
    const buttons = document.querySelectorAll(".buttons .btn");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const value = button.innerText;
            if (value === "C") {
                display.value = "";
            } else if (value === "=") {
                try {
                    display.value = eval(display.value);
                } catch (e) {
                    display.value = "Error";
                }
            } else {
                display.value += value;
            }
        });
    });

    // Ask AI Click Event
    if (aiBtn) {
        aiBtn.addEventListener("click", askAI);
    }

    if (aiPromptInput) {
        aiPromptInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") askAI();
        });
    }

    async function askAI() {
        const userPrompt = aiPromptInput.value.trim();

        if (!userPrompt) {
            alert("Pehle prompt input box mein text type karo!");
            return;
        }

        display.value = "Thinking...";

        try {
            const response = await fetch("/ask-ai", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ prompt: userPrompt })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            if (data && data.result) {
                display.value = data.result;
            } else {
                display.value = "No Result";
            }
        } catch (error) {
            console.error("AI Request Failed:", error);
            display.value = "Error: " + error.message;
        }
    }
});