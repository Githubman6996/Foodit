document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signupForm');
    const usernameField = document.getElementById('username');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');

    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission

        let valid = true;

        // Clear previous errors
        document.getElementById('usernameError').textContent = '';
        document.getElementById('emailError').textContent = '';
        document.getElementById('passwordError').textContent = '';

        // Validate username
        if (usernameField.value.trim() === '') {
            valid = false;
            document.getElementById('usernameError').textContent = 'Username is required.';
            usernameField.classList.add('error');
        } else {
            usernameField.classList.remove('error');
        }

        // Validate email
        if (emailField.value.trim() === '') {
            valid = false;
            document.getElementById('emailError').textContent = 'Email is required.';
            emailField.classList.add('error');
        } else if (!validateEmail(emailField.value.trim())) {
            valid = false;
            document.getElementById('emailError').textContent = 'Email is invalid.';
            emailField.classList.add('error');
        } else {
            emailField.classList.remove('error');
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
            alert('Sign-up successful!');
            // Redirect to the stats page
            window.location.href = 'stats.html';
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
