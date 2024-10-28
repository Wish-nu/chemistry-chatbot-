document.getElementById("send-btn").addEventListener("click", sendMessage);

async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div>You: ${userInput}</div>`;

    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: userInput })
    });

    const data = await response.json();
    chatBox.innerHTML += `<div>Bot: ${data.answer}</div>`;
    document.getElementById("user-input").value = "";
}
