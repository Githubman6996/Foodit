document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('loginForm');
    const usernameField = document.getElementById('username');
    const passwordField = document.getElementById('password');

    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission

        let valid = true;

        // Clear previous errors
        document.getElementById('usernameError').textContent = '';
        document.getElementById('passwordError').textContent = '';

        // Validate username
        if (usernameField.value.trim() === '') {
            valid = false;
            document.getElementById('usernameError').textContent = 'Username is required.';
            usernameField.classList.add('error');
        } else {
            usernameField.classList.remove('error');
        }

        // Validate password
        if (passwordField.value.trim() === '') {
            valid = false;
            document.getElementById('passwordError').textContent = 'Password is required.';
            passwordField.classList.add('error');
        } else {
            passwordField.classList.remove('error');
        }

        if (valid) {
            // Handle successful form submission
            alert('Login successful!');
            // Redirect to the stats page
            window.location.href = 'stats.html';
        }
    });
});
