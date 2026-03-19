function analyzeSpam() {
    const message = document.getElementById('messageInput').value;
    const btn = document.getElementById('analyzeBtn');
    const resultBox = document.getElementById('resultBox');
    
    if (!message.trim()) {
        alert("Please enter a message to analyze.");
        return;
    }
    
    // UI Loading state
    btn.disabled = true;
    btn.querySelector('.btn-text').textContent = "Analyzing...";
    resultBox.classList.add('hidden');
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
            return;
        }
        
        // Show Results
        resultBox.classList.remove('hidden');
        resultBox.className = 'result-box ' + (data.result.prediction === 1 ? 'fraud' : 'legit');
        
        const icon = data.result.prediction === 1 ? '<i class="fa-solid fa-triangle-exclamation"></i>' : '<i class="fa-solid fa-check-circle"></i>';
        const title = data.result.prediction === 1 ? 'Potential FRAUD / SPAM Detected' : 'Message appears LEGITIMATE';
        const colorClass = data.result.prediction === 1 ? 'text-danger' : 'text-success';
        
        resultBox.innerHTML = `
            <h3 class="${colorClass}">${icon} ${title}</h3>
            <div class="probs">
                <p>Fraud Probability: <strong>${(data.result.fraud_probability * 100).toFixed(2)}%</strong></p>
                <p>Legit Probability: <strong>${(data.result.legit_probability * 100).toFixed(2)}%</strong></p>
            </div>
            <div style="margin-top: 1.5rem;">
                <a href="${data.pdf_url}" target="_blank" class="btn-primary">
                    <i class="fa-solid fa-file-pdf"></i> Download Official Report
                </a>
            </div>
        `;
        
        // Refresh page after a short delay to update history or just append to history list (Reloading for simplicity for now)
        // setTimeout(() => location.reload(), 5000); 
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while analyzing.");
    })
    .finally(() => {
        btn.disabled = false;
        btn.querySelector('.btn-text').textContent = "Analyze Now";
    });
}
