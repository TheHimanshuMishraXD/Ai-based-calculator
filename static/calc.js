async function askAI() {
    const display = document.getElementById("display"); // Calculator display element
    const userPrompt = display.value.trim();

    if (!userPrompt) {
        display.value = "Enter prompt!";
        return;
    }

    // Processing indicator set karo (Screen clear hone se roko)
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

        // Server ka final result display par show karo
        if (data.result) {
            display.value = data.result;
        } else {
            display.value = "Error";
        }
    } catch (error) {
        console.error("Error asking AI:", error);
        display.value = "Server Error";
    }
}