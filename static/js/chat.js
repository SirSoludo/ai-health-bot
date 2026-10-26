const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatWindow = document.getElementById("chatWindow");
const newTopicBtn = document.getElementById("newTopicBtn");
const clearHistoryBtn = document.getElementById("clearHistoryBtn");

function appendMessage(text, sender, isEmergency = false) {
    const div = document.createElement("div");
    div.classList.add("message", sender === "user" ? "user-message" : "bot-message");
    if (isEmergency) {
        div.classList.add("emergency-message");
    }
    div.textContent = text;
    chatWindow.appendChild(div);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = messageInput.value.trim();
    if (!text) return;

    appendMessage(text, "user");
    messageInput.value = "";

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text }),
        });
        const data = await response.json();
        const isEmergency = data.result && data.result.type === "emergency";
        appendMessage(data.reply, "bot", isEmergency);
    } catch (err) {
        appendMessage("Sorry, something went wrong connecting to the assistant.", "bot");
    }
});

newTopicBtn.addEventListener("click", async () => {
    await fetch("/api/new-topic", { method: "POST" });
    appendMessage("Okay, let's talk about a new concern. What's bothering you?", "bot");
});

clearHistoryBtn.addEventListener("click", async () => {
    await fetch("/api/clear-history", { method: "POST" });
    chatWindow.innerHTML = "";
    appendMessage("History cleared. What's bothering you today?", "bot");
});
