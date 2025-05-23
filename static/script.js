function addMessage(content, isUser) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `max-w-[80%] p-4 rounded-lg ${
        isUser ? 'bg-blue-100 ml-auto text-right' : 'bg-gray-200 mr-auto'
    }`;
    messageDiv.innerHTML = content;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const query = userInput.value.trim();
    if (!query) return;

    addMessage(query, true);
    userInput.value = '';

    try {
        const response = await fetch('/api/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });
        const data = await response.json();
        let reply = '<h3 class="text-lg font-semibold mb-2">Here are some suggestions for you:</h3><div class="grid gap-4">';
        data.books.forEach(book => {
            reply += `
                <div class="book-card bg-white p-4 rounded-lg shadow-md">
                    <h4 class="font-bold text-blue-700">${book.title}</h4>
                    <p class="text-sm text-gray-700">Author: ${book.author || 'Không rõ'}</p>
                    <p class="text-sm text-gray-700">Price: ${book.price} USD</p>
                    <p class="text-sm text-gray-700">Category: ${book.category || 'Không rõ'}</p>
                    <p class="text-sm text-gray-700">Description: ${book.description || 'Không có mô tả'}</p>
                </div>`;
        });
        reply += '</div>';
        addMessage(reply, false);
    } catch (error) {
        addMessage('<p class="text-red-500">Something went wrong. Please try again.</p>', false);
    }
}

document.getElementById('userInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
