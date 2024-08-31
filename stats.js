document.addEventListener('DOMContentLoaded', () => {
    // Placeholder values. Replace these with actual data from your backend or local storage
    const username = 'JohnDoe';
    const tokenBalance = 1250;
    const recentActivity = 'Logged In';
    const highestScore = 95;
    const profilePicUrl = 'profile-pic.jpg'; // Path to the user's profile picture

    // Update profile information
    document.getElementById('username').textContent = username;
    document.getElementById('tokenBalance').textContent = tokenBalance;
    document.getElementById('recentActivity').textContent = recentActivity;
    document.getElementById('highestScore').textContent = highestScore;
    document.getElementById('profilePic').src = profilePicUrl;
});
