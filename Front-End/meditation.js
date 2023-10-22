const song = document.querySelector(".song");
const video = document.querySelector(".vid-container video");
//Duration

var typed = new Typed(".auto-type", {
    strings: ["For how long would you like to meditate       (in minutes)?"],
    typeSpeed: 40
})

// script.js
document.addEventListener("DOMContentLoaded", function () {
    const userInput = document.getElementById("userInput");
    const timer = document.getElementById("timer");
    const countdown = document.getElementById("countdown");
    const restartButton = document.getElementById("restartButton");
    const meditationAudio = document.getElementById("meditationAudio");

    userInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            const minutes = parseInt(userInput.value);
            if (!isNaN(minutes) && minutes > 0) {
                startCountdown(minutes * 60); // Convert minutes to seconds
            }
        }
    });

    restartButton.addEventListener("click", function () {
        const confirmRestart = confirm("Would you like to meditate again?");
        if (confirmRestart) {
            userInput.value = "";
            userInput.disabled = false;
            timer.classList.add("hidden");
            restartButton.classList.add("hidden");
            stopMeditationAudio(); // Stop the meditation audio on restart
        }
    });

    function startCountdown(seconds) {
        userInput.disabled = true;


        playMeditationAudio(); // Play the meditation audio

        let remainingSeconds = seconds;
        countdown.textContent = formatTime(remainingSeconds);

        const interval = setInterval(function () {
            remainingSeconds--;
            countdown.textContent = formatTime(remainingSeconds);

            if (remainingSeconds <= 0) {
                clearInterval(interval);
                restartButton.classList.remove("hidden");
                stopMeditationAudio(); // Stop the meditation audio on timer completion
            }
        }, 1000);
    }

    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    }

    function playMeditationAudio() {
        meditationAudio.play();
    }

    function stopMeditationAudio() {
        // Add fading out logic here, e.g., using the Web Audio API
        // For a simple fade-out, you can use the "volume" property
        const fadeOutInterval = setInterval(function () {
            if (meditationAudio.volume > 0) {
                meditationAudio.volume -= 0.05; // Adjust the rate of fading as needed
            } else {
                meditationAudio.pause();
                clearInterval(fadeOutInterval);
            }
        }, 200); // Adjust the interval as needed
    }
});

