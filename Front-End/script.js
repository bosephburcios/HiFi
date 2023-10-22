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
    initialMessage.innerHTML = `<p>Hi! Let us know how you are feeling today?</p>`;
    chatMessages.appendChild(initialMessage);

    // Show the options
    const optionsDiv = document.createElement('div');
    optionsDiv.classList.add('options');
    optionsDiv.innerHTML = `
    <!-- Heart rate -->
    <p>Heart Rate:</p>
    <input type="number" step="0.1" id="heartRate">

    <!-- Hours worked -->
    <p>Hours Worked:</p>
    <input type="number" step="0.1" id="hoursWorked">

    <!-- Weather options -->
    <p>Weather:</p>
    <div class="buttons">
        <button onclick="setWeather('Cloudy')">Cloudy</button>
        <button onclick="setWeather('Rainy')">Rainy</button>
        <button onclick="setWeather('Snowy')">Snowy</button>
        <button onclick="setWeather('Sunny')">Sunny</button>
    </div>
    <!-- Location options -->
    <p>Location:</p>
    <div class="buttons">
        <button onclick="setLocation('Urban')">Urban</button>
        <button onclick="setLocation('Suburban')">Suburban</button>
        <button onclick="setLocation('Rural')">Rural</button>
    </div>
    <button onclick="submitAnswers()">Submit</button> 
    `;
    chatMessages.appendChild(optionsDiv);
}

function changeLanguage() {
    // Get the selected language from the dropdown
    var selectedLanguage = document.querySelector(".language-select").value;

    // Get all elements with data-lang attribute
    var elements = document.querySelectorAll("[data-lang]");

    // Loop through the elements and show/hide text based on the selected language
    elements.forEach(function (element) {
        // Get the language of the element
        var elementLanguage = element.getAttribute("data-lang");

        // Show/hide the element based on the selected language
        if (elementLanguage === selectedLanguage) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
}

let selectedWeather = null;
let selectedLocation = null;

function setWeather(weather) {
    selectedWeather = weather;
}

function setLocation(location) {
    selectedLocation = location;
}

function submitAnswers() {
    const heartRateValue = parseFloat(document.getElementById('heartRate').value);
    const hoursWorkedValue = parseFloat(document.getElementById('hoursWorked').value);
    const chatMessages = document.querySelector('.chat-messages');

    // Validate all answers are provided
    if (isNaN(heartRateValue) || isNaN(hoursWorkedValue) || !selectedWeather || !selectedLocation) {
        alert("Please answer all questions.");
        return;
    }

    // Construct data for API call
    const data = {
        heartRate: heartRateValue,
        hoursWorked: hoursWorkedValue,
        weather: selectedWeather,
        location: selectedLocation
    };
    console.log("UPDATEEEEEEE");

    // Make an API call
    fetch("http://localhost:3000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            const predictedLabel = data.label;
            alert("Predicted label: " + predictedLabel);
            console.log("Predicted label: " + predictedLabel);
        
            // Check if the predicted label is "Meditation" and then open "meditation.html"
            if (predictedLabel === "Meditation") {
                window.location.href = "meditation.html";
            } else {
                console.log("Predicted label is not 'Meditation'");
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });

    // const botMessages = getBotResponse('Heartbeat'); // Call the getBotResponse function
    // botMessages.forEach((message) => {
    //     const botMessage = document.createElement('div');
    //     botMessage.classList.add('message', 'bot-message');
    //     botMessage.innerHTML = `<p>${message}</p>`;
    //     chatMessages.appendChild(botMessage);
    // });
}


function getBotResponse(option) {
    // if (option === 'Heartbeat' && selectedWeather === 'Sunny' && selectedLocation === 'Rural') {
    //     return ["You have a good heart rate, the weather is sunny, and you're in a rural area. How about going for a nice walk? It's a great way to enjoy the weather and stay active!"];
    // } else {
    //     return ["I'm sorry, I couldn't find a suitable suggestion based on your input. Please provide more information for personalized recommendations."];
    // }
    window.location.href = "meditation.html";
}

