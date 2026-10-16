// 1. HTML Elements select karna
const display = document.getElementById('display');
const buttons = document.querySelectorAll('.buttons button');
const aiPrompt = document.getElementById('ai-prompt');
const aiBtn = document.getElementById('ai-btn');

// 2. Buttons click event handling
buttons.forEach(button => {
    button.addEventListener('click', (e) => {
        // Agar click galti se AI button par hua ho toh ignore karein
        if (button.id === 'ai-btn') return;

        const value = button.innerText.trim();

        if (value === 'C') {
            display.value = ''; // Display screen clear
        } else if (value === '=') {
            try {
                display.value = eval(display.value); // Basic math solve
            } catch (error) {
                display.value = 'Error';
            }
        } else {
            display.value += value; // Screen par append karna
        }
    });
});

// 3. Ask AI Button Event Handler
aiBtn.addEventListener('click', async () => {
    const query = aiPrompt.value.trim();

    if (!query) {
        alert('Kripya AI ke liye koi question type karein!');
        return;
    }

    display.value = 'Thinking...';

    try {
        const response = await fetch('/ask-ai', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: query })
        });

        const data = await response.json();
        if (data.result !== undefined) {
            display.value = data.result;
            aiPrompt.value = ''; // AI response aane par input box clear
        } else {
            display.value = 'Error';
        }
    } catch (err) {
        display.value = 'AI Error';
    }
});