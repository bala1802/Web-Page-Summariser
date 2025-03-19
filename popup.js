document.addEventListener('DOMContentLoaded', () => {
    const scrapeButton = document.getElementById('scrapeButton');
    const statusDiv = document.getElementById('status');
    const BACKEND_URL = 'http://127.0.0.1:5000';

    scrapeButton.addEventListener('click', async () => {
        statusDiv.textContent = 'Analyzing page...';
        statusDiv.className = '';
        scrapeButton.disabled = true;

        try {
            // Get current tab URL
            const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
            
            // Check if backend is running
            try {
                const healthCheck = await fetch(`${BACKEND_URL}/health`);
                if (!healthCheck.ok) {
                    throw new Error('Backend server is not running');
                }
            } catch (error) {
                throw new Error('Cannot connect to backend server. Please make sure it is running on port 5000');
            }

            // Send request to backend
            const response = await fetch(`${BACKEND_URL}/scrape`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: tab.url
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Failed to analyze page');
            }

            const data = await response.json();

            // Create and download file
            const blob = new Blob([data.content], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            
            await chrome.downloads.download({
                url: url,
                filename: 'summary.txt',
                saveAs: false
            });

            statusDiv.textContent = 'Summary saved to summary.txt!';
        } catch (error) {
            statusDiv.textContent = 'Error: ' + error.message;
            statusDiv.className = 'error';
        } finally {
            scrapeButton.disabled = false;
        }
    });
}); 