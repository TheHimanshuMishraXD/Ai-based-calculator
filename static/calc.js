const display = document.getElementById('display');
const buttons = document.querySelectorAll('.buttons buttons');
const aiprompt = document.getElementById('ai-prompt');
const aiBtn = document.getElementById('ai-Btn');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.innerText;

        if (value === 'C') {
            display.value = ''; // Display clear karne ke liye
        } else if (value === '=') {
            try {
                display.value = eval(display.value); // Math calculation
            } catch (error) {
                display.value = 'Error';
            }
        } else {
            display.value += value; // Numbers/operators screen par jodna
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
        } else {
            display.value = 'Error';
        }
    } catch (err) {
        display.value = 'AI Error';
    }
});