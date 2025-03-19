from flask import Flask, request, jsonify
from flask_cors import CORS
from firecrawl import FirecrawlApp
import os
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Configure Gemini
genai.configure(api_key='<GEMINI_API_KEY>')
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400

        url = data.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Use hardcoded Firecrawl API key
        os.environ['FIRECRAWL_API_KEY'] = '<FIRECRAWL_API_KEY>'
        crawler = FirecrawlApp()
        scrape_result = crawler.scrape_url(url)
        
        if not scrape_result or 'markdown' not in scrape_result:
            return jsonify({'error': 'Failed to scrape content'}), 500
            
        # Use Gemini to generate summary and topics
        prompt = f"""
        Please analyze this text and provide:
        1. A concise summary (max 3 paragraphs)
        2. The primary topics/themes (max 5 bullet points)
        
        Text to analyze:
        {scrape_result['markdown']}
        """
        
        response = model.generate_content(prompt)
        
        return jsonify({
            'content': response.text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 