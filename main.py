from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

app = FirecrawlApp()

def scrape_and_save(url):
    scrape_result = app.scrape_url(url)
    markdown_content = scrape_result["markdown"]
    
    with open("llm.txt", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    return "Content saved to llm.txt"

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/DeepSeek"
    result = scrape_and_save(url)
    print(result)