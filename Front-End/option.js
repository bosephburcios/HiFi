// Function to toggle service details on small screens
const serviceTitles = document.querySelectorAll('.service-title');

serviceTitles.forEach(function (title) {
    title.addEventListener('click', function () {
        var service = title.closest('.service');
        service.classList.toggle('active');

        // Hide other service details
        document.querySelectorAll('.service').forEach(function (otherService) {
            if (otherService !== service) {
                otherService.classList.remove('active');
            }
        });
    });
});

// Function to handle the button click to show service details on small screens
const serviceButtons = document.querySelectorAll('.get-started-button');

serviceButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        var service = button.closest('.service');
        service.classList.toggle('active');

        // Hide other service details
        document.querySelectorAll('.service').forEach(function (otherService) {
            if (otherService !== service) {
                otherService.classList.remove('active');
            }
        });
    });
});