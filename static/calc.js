document.addEventListener("DOMContentLoaded", () => {
    const aiBtn = document.getElementById("ai-btn");
    const aiPromptInput = document.getElementById("ai-prompt");
    const display = document.getElementById("display");

    // 1. Calculator Normal Buttons Event Handling
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

    // 2. Ask AI Button Event Handling
    if (aiBtn) {
        aiBtn.addEventListener("click", askAI);
    }

    // Optional: Enter key dabane par bhi AI trigger hoga
    if (aiPromptInput) {
        aiPromptInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                askAI();
            }
        });
    }

    async function askAI() {
        const userPrompt = aiPromptInput.value.trim();

        if (!userPrompt) {
            alert("Pehle input box mein question type karo!");
            return;
        }

        // Screen clear hone se roko, processing indicator do
        display.value = "Thinking...";

        try {
            const response = await fetch("/ask-ai", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ prompt: userPrompt })
            });

            const data = await response.json();

            if (data.result) {
                // Backend se mila hua output main result screen par aayega
                display.value = data.result;
            } else {
                display.value = "Error getting response";
            }
        } catch (error) {
            console.error("Fetch Error:", error);
            display.value = "Server Error";
        }
    }
});