const menuIcon = document.getElementById('menu-icon');
const menu = document.getElementById('menu');
const closeIcon = document.getElementById('close-icon');

menuIcon.addEventListener('click', () => {
    menu.classList.toggle('active');
});

closeIcon.addEventListener('click', () => {
    menu.classList.toggle('active');
});

// chat bot
var userOptions = document.querySelectorAll('.user-option');
userOptions.forEach(function(option) {
    option.addEventListener('click', function() {
        var message = option.textContent;
        var chatMessages = document.querySelector('.chat-messages');
        var userMessage = document.createElement('div');
        userMessage.classList.add('user-message');
        userMessage.textContent = message;
        chatMessages.appendChild(userMessage);
    });
});

function selectOption(option) {
    // Get all option buttons
    const optionButtons = document.querySelectorAll('.option');

    // Hide all option buttons
    optionButtons.forEach((button) => {
        button.style.display = 'none';
    });

    // Display the selected option as a user message
    const chatMessages = document.querySelector('.chat-messages');
    const optionMessage = document.createElement('div');
    optionMessage.classList.add('message', 'user-message');
    optionMessage.innerHTML = `<p>${option}</p>`;
    chatMessages.appendChild(optionMessage);

    // Provide tips based on the selected option with a delay
    setTimeout(() => {
        const botMessages = getBotResponse(option);
        botMessages.forEach((message) => {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot-message');
            botMessage.innerHTML = `<p>${message}</p>`;
            chatMessages.appendChild(botMessage);
        });
    }, 1500); // Delay in milliseconds
}

function getBotResponse(option) {
    switch (option) {
        case 'I am feeling anxious':
            return ["You should do some breathing exercises!"];
        case 'I am feeling exhausted':
            return ["You should take a small break!"];
        case 'I want to feel motivated':
            return ["You should listen to some music!", "Suggested Song: 'Dream On' by Aerosmith"];
        default:
            return ["I'm here to help. Please choose an option."];
    }
}

function closeChatbot() {
    var chatWindow = document.getElementById('chatWindow');
    chatWindow.style.display = 'none';
    resetChatbot(); // Reset the chat when closing
}

function resetChatbot() {
    // Clear the chat history
    const chatMessages = document.querySelector('.chat-messages');
    chatMessages.innerHTML = '';

    // Show the initial message
    const initialMessage = document.createElement('div');
    initialMessage.classList.add('message', 'bot-message');
    initialMessage.innerHTML = `<p>Hi! How can I assist you today?</p>`;
    chatMessages.appendChild(initialMessage);

    // Show the options
    const optionsDiv = document.createElement('div');
    optionsDiv.classList.add('options');
    optionsDiv.innerHTML = `
        <button class="option" onclick="selectOption('I am feeling anxious')">I'm feeling anxious</button>
        <button class="option" onclick="selectOption('I am feeling exhausted')">I'm feeling exhausted</button>
        <button class="option" onclick="selectOption('I want to feel motivated')">I want to feel motivated</button>
    `;
    chatMessages.appendChild(optionsDiv);
}

