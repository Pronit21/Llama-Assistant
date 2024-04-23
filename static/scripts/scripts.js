const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');

startBtn.addEventListener('click', () => {
    fetch('/start_assistant', { method: 'POST' })
        .then(response => response.json())
        .then(data => console.log(data.message));
});

stopBtn.addEventListener('click', () => {
    fetch('/stop_assistant', { method: 'POST' })
        .then(response => response.json())
        .then(data => console.log(data.message));
});
