import json
import urllib.request
from datetime import datetime, timedelta

apikey = "YOUR_API_KEY"

def fetch_articles(query, date_time):
    # Calculate from_date and to_date
    to_date = date_time
    from_date = to_date - timedelta(days=1)

    # Format dates as required by GNews API
    from_date_str = from_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    to_date_str = to_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Construct API request URL
    url = f"https://gnews.io/api/v4/search?q={query}&from={from_date_str}&to={to_date_str}&lang=en&country=us&max=10&apikey={apikey}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            articles = data.get("articles", [])
            return articles
    except Exception as e:
        print(f"Error fetching articles: {str(e)}")
        return []

def format_articles_to_prompt(articles):
    prompt = ""
    for article in articles:
        title = article.get('title', 'No title')
        description = article.get('description', 'No description')
        content = article.get('content', 'No content')
        prompt += f"Title: {title}\nDescription: {description}\nContent: {content}\n\n"
    return prompt

def format_articles_to_prompt(articles, query):
    prompt = f"Query: {query}\n"
    for article in articles:
        title = article.get('title', 'No title')
        description = article.get('description', 'No description')
        content = article.get('content', 'No content')
        prompt += f"Title: {title}\nDescription: {description}\nContent: {content}\n\n"
    return prompt

def generate_prompt_for_queries(queries, date_time):
    full_prompt = ""
    for query in queries:
        articles = fetch_articles(query, date_time)
        query_prompt = format_articles_to_prompt(articles, query)
        full_prompt += query_prompt
    return full_prompt

if __name__ == "__main__":
    queries = ["Google"]
    date_time_str = "2024-06-10T12:00:00Z"  # Example date and time
    date_time = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%SZ")

    prompt = generate_prompt_for_queries(queries, date_time)

    # Now you can use this prompt with an LLM
    print(prompt)
