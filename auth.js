function showSignup() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('signup-form').style.display = 'block';
}

function showLogin() {
    document.getElementById('signup-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
}

function login() {
    event.preventDefault();  // Остановка перезагрузки страницы
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    // Простая проверка данных для примера
    if (email === "user@google.com" && password === "password123") {
        // Перенаправление на другой сайт после успешного входа
        window.location.href = "https://.com";
    } else {
        alert("Invalid login credentials.");
    }
}

function signup() {
    event.preventDefault();  // Остановка перезагрузки страницы
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;

    if (email && password) {
        alert("Signup successful! Please log in.");
        showLogin();
    } else {
        alert("Please fill in all fields.");
    }
}
