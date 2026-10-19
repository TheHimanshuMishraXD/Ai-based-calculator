document.addEventListener("DOMContentLoaded", () => {
    const aiBtn = document.getElementById("ai-btn");
    const aiPromptInput = document.getElementById("ai-prompt");
    const display = document.getElementById("display");
    const historyList = document.getElementById("history-list");
    const clearHistoryBtn = document.getElementById("clear-history-btn");

    let history = [];

    // Helper: Calculate expression
    function calculateResult() {
        if (!display.value.trim()) return;
        const expr = display.value;
        try {
            const res = eval(expr);
            addHistoryItem(expr, res);
            display.value = res;
        } catch (e) {
            display.value = "Error";
        }
    }

    // Helper: Add History Item
    function addHistoryItem(expression, result) {
        history.unshift({ expression, result });
        renderHistory();
    }

    // Helper: Render History List
    function renderHistory() {
        if (history.length === 0) {
            historyList.innerHTML = `<li class="empty-history">No calculations yet</li>`;
            return;
        }

        historyList.innerHTML = "";
        history.forEach(item => {
            const li = document.createElement("li");
            li.className = "history-item";
            li.innerHTML = `
                <div class="history-expression">${item.expression}</div>
                <div class="history-result">= ${item.result}</div>
            `;
            li.addEventListener("click", () => {
                display.value = item.result;
            });
            historyList.appendChild(li);
        });
    }

    // Clear History Event
    if (clearHistoryBtn) {
        clearHistoryBtn.addEventListener("click", () => {
            history = [];
            renderHistory();
        });
    }

    // Calculator Buttons Click
    const buttons = document.querySelectorAll(".buttons .btn");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const value = button.innerText;
            if (value === "C") {
                display.value = "";
            } else if (value === "=") {
                calculateResult();
            } else {
                display.value += value;
            }
        });
    });

    // Keyboard Shortcuts Listener
    document.addEventListener("keydown", (e) => {
        // Skip shortcuts if user is typing in AI input box
        if (document.activeElement === aiPromptInput) return;

        const key = e.key;

        if (key >= "0" && key <= "9") {
            display.value += key;
        } else if (["+", "-", "*", "/"].includes(key)) {
            display.value += key;
        } else if (key === "." || key === ",") {
            display.value += ".";
        } else if (key === "Enter" || key === "=") {
            e.preventDefault();
            calculateResult();
        } else if (key === "Backspace") {
            display.value = display.value.slice(0, -1);
        } else if (key === "Escape" || key === "c" || key === "C") {
            display.value = "";
        }
    });

    // Ask AI Event Listeners
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
                addHistoryItem(userPrompt, data.result);
                aiPromptInput.value = "";
            } else {
                display.value = "No Result";
            }
        } catch (error) {
            console.error("AI Request Failed:", error);
            display.value = "Error: " + error.message;
        }
    }
});