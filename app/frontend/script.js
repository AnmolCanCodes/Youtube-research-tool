const form = document.getElementById('outline-form');
const topicInput = document.getElementById('topic');
const statusEl = document.getElementById('status');
const resultEl = document.getElementById('result');

const API_BASE = window.location.port === '8000' ? '' : 'http://127.0.0.1:8000';

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const topic = topicInput.value.trim();
    if (!topic) {
        statusEl.textContent = 'Please enter a topic first.';
        return;
    }

    statusEl.textContent = 'Generating your outline...';
    resultEl.innerHTML = '';

    try {
        const response = await fetch(`${API_BASE}/api/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title: topic }),
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || 'Something went wrong.');
        }

        const data = await response.json();

        resultEl.innerHTML = `
            <div><span class="label">Title:</span> ${data.title}</div>
            <div><span class="label">Hook:</span> ${data.hook}</div>
            <div><span class="label">Description:</span> ${data.description}</div>
            <div><span class="label">Sections:</span></div>
            <ul>${(data.sections || []).map((item) => `<li>${item}</li>`).join('')}</ul>
            <div><span class="label">Examples:</span></div>
            <ul>${(data.examples || []).map((item) => `<li>${item}</li>`).join('')}</ul>
            <div><span class="label">CTA:</span> ${data.cta}</div>
        `;
        statusEl.textContent = 'Outline generated successfully.';
    } catch (error) {
        statusEl.textContent = error.message;
        resultEl.innerHTML = '<p>Unable to generate an outline right now.</p>';
    }
});
