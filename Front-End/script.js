const menuIcon = document.getElementById('menu-icon');
const menu = document.getElementById('menu');
const closeIcon = document.getElementById('close-icon');

menuIcon.addEventListener('click', () => {
    menu.classList.toggle('active');
});

closeIcon.addEventListener('click', () => {
    menu.classList.toggle('active');
});
