from telethon import TelegramClient
import datetime
import asyncio
from translate import translate_mixed_languages_to_english

# Your API ID and hash
api_id = ''
api_hash = ''
phone_number = ''

client = TelegramClient('session_name', api_id, api_hash)

async def get_telegram_messages(group_link, end_date):
    await client.start()
    
    # Convert start_date and end_date to datetime objects
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    end_date = end_date.replace(tzinfo=datetime.timezone.utc)
    start_date = (end_date - datetime.timedelta(days=1))
    
    # Get the chat entity using the group link
    chat = await client.get_entity(group_link)
    
    # Fetch messages in chunks of 50
    messages = []
    async for message in client.iter_messages(chat, min_id=1, reverse=False):
        if message.date > end_date:
            continue  # Skip messages that are newer than end_date
        if message.date < start_date:
            break  # Stop fetching messages once we go before start_date
        messages.append(message)
    
    return messages

async def get_tweets(group_link, end_date):
    messages = await get_telegram_messages(group_link, end_date)

    await client.disconnect()

    return messages

def check_queries_in_text(text, queries):
    for query in queries:
        if query in text:
            return True
    return False

if __name__ == "__main__":

    end_time = '2024-06-10 15:00:00'
    queries = ["BTC", "bitcoin"]
    #queries = ["apple", "AAPL"]

    queries = [query.lower() for query in queries]
    group_links = [
        't.me/VGSTOCKRESEARCH', 
        't.me/khmrchk', 

        't.me/CryptoInnerCircle_ViP', 
        't.me/cryptoinnercircle', 
        't.me/InnerCircle_Free', 
        't.me/BinanceKiller_Official', 
        't.me/Wolf_of_tradings', 
        't.me/wolfoftrading_Live', 
        't.me/wallstreetqueenofficial', 
        't.me/BitcoinBullets', 
        't.me/RocketWallets_Official', 
        't.me/crypto_tradingn', 
        't.me/BeInCryptoCommunity/1', 
        't.me/beincrypto_ru/1', 

        't.me/Etoro_Forex_Signallfx', 
        't.me/Gold_SignalsOfficials', 

        "t.me/CapitalVia"
        ]
    
    prompt = ""
    for group_link in group_links:
        try:
            messages = client.loop.run_until_complete(get_tweets(group_link, end_time))
            #print(group_link, len(messages))
            
            if len(messages)>0:
                group_prompt = f"Group: {group_link}\n\n"
                for message in messages:
                    group_prompt += f"Time: {message.date.strftime('%H:%M:%S')}\n"
                    group_prompt += f"Text: {translate_mixed_languages_to_english(message.text)}\n"
                group_prompt += f"\n\n"

                lower_group_prompt = group_prompt.lower()
                print(group_link, len(messages))
                if check_queries_in_text(lower_group_prompt, queries):
                    print("found")
                    prompt += group_prompt
        except Exception as e:
            print(e)
            continue
    
    print("\n\n")
    print(prompt)