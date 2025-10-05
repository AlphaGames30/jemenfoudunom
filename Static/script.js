const socket = io();

socket.on('new_message', data => {
    const chat = document.getElementById('chat');
    chat.innerHTML += `<p><b>${data.user}:</b> ${data.content}</p>`;
});

function sendMessage() {
    const input = document.getElementById('message');
    const msg = input.value;
    socket.emit('send_message', {user: 'WebUser', content: msg});
    input.value = '';
}
