from openai import OpenAI
import pandas as pd
import numpy as np
import ast

class chatgpt:
    def __init__(self):
        self.client = OpenAI(api_key = 'api-key')
        self.rag_data = pd.read_csv("embeddings.csv")
        def convert_string_to_arrays(string):
            # Use ast.literal_eval to safely evaluate the string
            list_of_arrays = ast.literal_eval(string)

            return np.array(list_of_arrays, dtype=float)

        self.rag_data['embeddings'] = self.rag_data['embeddings'].apply(convert_string_to_arrays)

    def call_gpt(self, messages):
        response = self.client.chat.completions.create(
        model="gpt-4o",
        messages = messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        return response.choices[0].message.content
    
    def get_news_summary(self, news,date, companies_string, main_company):
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": f"you are an educator in a trading platform.\nhere are the news from the {date}\nabout {companies_string} \n\n\"\"\"\n{news}\n\n\"\"\"\nread the news and write a short paragraph summarising with emphasis on apple.\nat the end make an educated guess based on the news if the {main_company} stock will go up, down or cant tell\n"
                }
            ]
            },
        ]

        output = self.call_gpt(messages)

        messages.append({
            "role": "assistant",
            "content": [
                {
                "type": "text",
                "text": output
                }
            ]
        })
        messages.append(
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "summarize the above and highlight in bold the stock outcome"
                }
            ]
        })

        output = self.call_gpt(messages)
        return output

    def get_stock_summary(self, stock = "apple"):
        text = """-	There is No Golden or Death Cross in the last 5 dayes.
-   Following the Golden Cross in May, the stock price shows a substantial increase.
-	Both the 50-day and 200-day SMAs start trending upwards, with the 50-day SMA remaining above the 200-day SMA."""
        return text
    
    def get_feed_summary(self, feed ,date, main_company):
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": f"you are an educator in a trading platform.\nhere are the telegram feeds from the {date}\nabout {main_company} \n\n\"\"\"\n{feed}\n\n\"\"\"\nread the telegram feeds and write a short paragraph summarising with emphasis on {main_company}.\nat the end make an educated guess based on the news if the {main_company} stock will go up, down or cant tell\n"
                }
            ]
            },
        ]

        output = self.call_gpt(messages)

        messages.append({
            "role": "assistant",
            "content": [
                {
                "type": "text",
                "text": output
                }
            ]
        })
        messages.append(
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "summarize the above and highlight in bold the stock outcome"
                }
            ]
        })

        output = self.call_gpt(messages)
        return output

    def get_embeddings(self, text):
        response = self.client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
        )

        return response.data[0].embedding
    

    def rag_search(self, query):
        
        query_embedding = self.get_embeddings(query)
        # Calculate similarity scores for all embeddings
        similarity_scores = self.rag_data['embeddings'].map(
            lambda emb: np.dot(emb, query_embedding) / (
                np.linalg.norm(emb) * np.linalg.norm(query_embedding)
            )
        )

        # Get indices of the top 5 best matches
        top_5_indices = np.argsort(similarity_scores)[-5:][::-1]

        # Retrieve the sentences corresponding to the top 5 embeddings
        best_paragraphs = self.rag_data.iloc[top_5_indices]['sentences']

        rag_text = '\n\n'.join(best_paragraphs)

        return rag_text

    def rag_q(self, query):
        text = self.rag_search(query)

        user_profile = """The user profile describes a new trader with specific experiences and goals in the investment world. Last year, the user engaged in fewer than 10 stock trading activities and invested between $500 and $2000 in stocks. Their experience with cryptocurrencies is also minimal, having participated in fewer than 5 transactions last year, with an investment amount ranging from $1 to $500. The user has no experience with leverage. They have pursued education through online trading courses and have a particular interest in stocks. Typically, they hold positions for a few weeks to several months. Their financial strategy includes a deposit plan of $20,000 to $50,000 with a balanced risk-reward ratio of 10-10. The bio indicates that the user is new to trading and has a keen interest in stocks."""

        messages=[
            {
                "role": "user",
                "content": f"""

You are an assistant and educator for stock trading and question-answering tasks. You should answer based on the user profile. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

User Profile: {user_profile}    

Question: {query} 

Context: {text} 

Answer:"""
            },
        ]

        output = self.call_gpt(messages)

        return output

if __name__ == "__main__":
    gpt = chatgpt()
    news = """Query: Apple
    Title: Android clearly inspired Apple's newest iOS 18 features
    Description: At WWDC, Apple announced customization features that borrow heavily from Android
    Content: Summary iOS 18 will introduce an app locking system and themed home screen icons, mirroring features already familiar to Android users.
    The app locking system in iOS 18 will simplify securing sensitive data and offer Face ID, Touch ID, or password au... [3543 chars]

    Title: Apple expected to enter AI race with ambitions to overtake the early leaders
    Description: Apple’s annual World Wide Developers Conference on Monday is expected to herald the company’s move into generative artificial intelligence, marking its 
    late arrival to a technological frontier that’s expected to be as revolutionary as the invention of the iPhone.
    Content: Apple’s annual World Wide Developers Conference on Monday is expected to herald the company’s move into generative artificial intelligence, marking its late arrival to a technological frontier that’s expected to be as revolutionary as the invention o... [4687 chars]

    Title: WWDC 2024: How to watch Apple’s keynote on iOS 18, AI and more
    Description: You can watch Apple’s WWDC keynote event in a number of ways, including via the company’s YouTube page. Apple’s likely to reveal iOS18, among other software updates.
    Content: Apple’s Worldwide Developers Conference (WWDC) keynote is imminent. The festivities kick off later today — Monday, June 10 at 1PM ET. The keynote address is available to the public and you can watch it via Apple’s event website or on the company’s Yo... [2486 chars]

    Title: WWDC 2024: How to Watch and What to Expect, From iOS 18 to 'Apple Intelligence'
    Description: WWDC starts tomorrow and we expect new AI features and an update to Siri, as well as the anticipated refresh of iOS, MacOS, iPadOS and more.
    Content: We are less than a day away from Apple's annual Worldwide Developers Conference. For fans of the Cupertino company, there's always anticipation leading up to the company's WWDC keynote. This year, that suspense is in high gear, as the world awaits Ap... [6229 chars]

    Title: Today in Apple history
    Description: On June 9, 2002, Apple launched its "Switch" ad campaign, with real people like 15-year-old Ellen Feiss talking about going from PCs to Macs.
    Content: June 9, 2002: Apple launches its “Switch” advertising campaign, featuring real people talking about their reasons for switching from PCs to Macs. Apple’s biggest marketing effort since the “Think different” ad campaign a few years earlier, one “Switc... [5287 chars]
    Query: Microsoft
    Title: Microsoft's New Xbox Console Options Include Galaxy Black Special Edition
    Description: Microsoft has unveiled three new variations of its latest-generation Xbox console series, including a limited production version with a special design. 
    Content: Microsoft's New Xbox Console Options Include Galaxy Black Special Edition
    Microsoft is bringing a trio of new console configurations to shelves this holiday season. The most notable addition to the portfolio is the Xbox Series X Digital Edition, whic... [1144 chars]

    Query: Google
    Title: Google Chrome is the fastest browser in Speedometer 3.0 history
    Description: Discover how Google Chrome became the fastest browser ever in the Speedometer 3.0 test, setting a new benchmark in web performance.
    Content: Google Chrome has once again taken the crown as the world’s fastest browser, achieving the highest score ever in the Speedometer 3.0 test. This milestone marks a significant achievement for the browser, which has consistently pushed the boundaries of... [6200 chars]

    Title: Google Pixel 8a vs. Pixel 9: Buy Now or Wait?
    Description: Should you buy the Google Pixel 8a now or wait for the rumored Pixel 9? Discover the key features that could influence your choice.
    Content: Upgrading your phone can be exciting but also daunting. The fear of missing out on the “next big thing” can leave you wondering if you should hit pause and 
    wait. After all, a brand new Google Pixel 8a sits enticingly at a sub-$500 price point. And fo... [5550 chars]
    """
    date = "10/06/2024"
    companies_string= "Apple, Microsoft and Google"
    main_company = "Apple"

    feed = """"""

    print(gpt.get_news_summary(news,date, companies_string, main_company))