# Web Page Summarizer Chrome Extension

A Chrome extension that uses Firecrawl to scrape web pages and Gemini AI to generate concise summaries and key topics.

## Features

- One-click webpage summarization
- AI-powered content analysis using Gemini
- Automatic summary generation with key topics
- Clean and user-friendly interface
- Error handling and status feedback

## Prerequisites

- Python 3.11 or higher
- Google Chrome browser
- pip (Python package installer)

## Installation

### 1. Backend Server Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv web-scrap
source web-scrap/bin/activate  # On Windows: web-scrap\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Start the Flask server:
```bash
python server.py
```

The server will start running on http://127.0.0.1:5000

### 2. Chrome Extension Setup

1. Open Google Chrome
2. Go to `chrome://extensions/`
3. Enable "Developer mode" in the top right corner
4. Click "Load unpacked"
5. Select the folder containing these files:
   - manifest.json
   - popup.html
   - popup.js

## Usage

1. Make sure the Flask backend server is running
2. Click the extension icon in Chrome
3. Click "Summarize This Page"
4. The extension will:
   - Scrape the current page using Firecrawl
   - Generate a concise summary using Gemini AI
   - Extract key topics from the content
   - Save the results to summary.txt in your downloads folder

## Project Structure

```
├── README.md           # Documentation
├── requirements.txt    # Python dependencies
├── server.py          # Flask backend server
├── manifest.json      # Chrome extension manifest
├── popup.html         # Extension popup UI
└── popup.js          # Extension frontend logic
```

## Configuration

The application uses two API keys that are currently hardcoded in server.py:
- Firecrawl API key: `fc-639175fcffc74bf79d9e68a6caec6510`
- Gemini API key: `AIzaSyAxm7LNV9OLy4_JUmcH8RBu85WBMyEqHE8`

For production deployment, you should:
1. Move these keys to environment variables
2. Use a secure secrets management system
3. Implement proper API key rotation

## Deployment

### Development Environment
The current setup is configured for local development with:
- Backend running on localhost:5000
- Chrome extension loading from local files
- Direct HTTP communication

### Production Deployment
For production deployment, consider:

1. Backend Server:
   - Deploy to a cloud platform (AWS, Google Cloud, Heroku)
   - Set up HTTPS with SSL/TLS certificates
   - Implement rate limiting and monitoring
   - Use environment variables for configuration

2. Chrome Extension:
   - Package the extension for Chrome Web Store
   - Update manifest.json with production URLs
   - Implement proper error handling
   - Add usage analytics (optional)

3. Security Considerations:
   - Use HTTPS for all API communications
   - Implement proper authentication
   - Add request validation
   - Set up logging and monitoring

## Troubleshooting

1. Backend Issues:
   - Verify server is running on port 5000
   - Check Python environment and dependencies
   - Review server logs for errors
   - Ensure required API keys are valid

2. Extension Issues:
   - Check Chrome's developer console (F12)
   - Verify extension permissions
   - Test backend connectivity
   - Clear extension cache if needed

3. Common Error Messages:
   - "Cannot connect to backend server": Check if server.py is running
   - "Failed to analyze page": Verify API keys and server logs
   - "Download failed": Check Chrome download permissions

## Development

To modify the extension:

1. Backend Changes:
   - Modify server.py for API changes
   - Update requirements.txt for new dependencies
   - Test API endpoints using Postman/curl

2. Frontend Changes:
   - Edit popup.html for UI changes
   - Modify popup.js for new functionality
   - Test in Chrome with Developer Tools

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details 