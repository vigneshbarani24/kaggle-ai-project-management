import requests
from bs4 import BeautifulSoup
import json
import os

class Tools:
    def __init__(self):
        # In a real scenario, we would initialize API clients here
        pass

    def search_web(self, query: str) -> str:
        """
        Simulates a web search. In a production environment, this would call 
        Google Search API, Serper, or Tavily.
        """
        print(f"  [Tool] Searching web for: {query}")
        
        # Mock responses for demonstration purposes if no API key is present
        # This allows the user to run the code immediately without setup
        mock_results = [
            {
                "title": f"About {query}",
                "snippet": f"Detailed information about {query}. They are a leading company in their industry.",
                "link": f"https://www.{query.replace(' ', '').lower()}.com"
            },
            {
                "title": f"{query} Financials",
                "snippet": f"{query} reported strong growth last quarter. Revenue is estimated at $500M+.",
                "link": f"https://finance.yahoo.com/quote/{query.split()[0]}"
            },
            {
                "title": f"{query} Technology Stack",
                "snippet": f"{query} is currently using legacy SAP ECC and looking to modernize.",
                "link": f"https://techstack.com/{query.replace(' ', '').lower()}"
            }
        ]
        return json.dumps(mock_results)

    def scrape_website(self, url: str) -> str:
        """
        Fetches text content from a URL.
        """
        print(f"  [Tool] Scraping URL: {url}")
        try:
            # Simple request with timeout and headers
            headers = {'User-Agent': 'Mozilla/5.0'}
            # For demonstration, we won't actually hit external URLs to avoid blocking/errors
            # response = requests.get(url, headers=headers, timeout=10)
            # response.raise_for_status()
            # soup = BeautifulSoup(response.text, 'html.parser')
            # return soup.get_text()[:5000]
            
            return f"Simulated content for {url}. This page contains details about the company's operations, leadership, and recent news."
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"
