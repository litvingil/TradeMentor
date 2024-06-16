
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from pandas import Timestamp
from SMA_test import add_signal_columns as add_signal_columns_


def get_data(stock = 'AAPL', days=7):
    # Get data on this ticker
    tickerData = yf.Ticker(stock)

    # # Define the date range for the last week
    # end_date = datetime.now()
    # start_date = end_date - timedelta(days=days)

    # # Get the historical prices for this ticker
    # tickerDf = tickerData.history(period='1h', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    tickerDf = tickerData.history(period='6mo', interval='60m')
    # Create a new DataFrame with Date and Close columns
    data = tickerDf[['Close']].copy()
    # data.reset_index(inplace=True)

    # change the column names
    # data.columns = ['date', 'value']
    data.columns = ['value']

    return data

def get_points(data):
    # date_strings = ['2023-10-15 09:30:00-0500', '2023-11-15 09:30:00-0500', '2023-12-15 09:30:00-0500']
    dates = [pd.Timestamp('2024-06-07 15:30'),pd.Timestamp('2024-04-29 15:30'),pd.Timestamp('2024-01-12 15:30')]
    values = [196.9,173.5,185.92]


    green_points = pd.DataFrame({
        'date': dates,
        'value': values
    })

    dates = [pd.Timestamp('2024-05-21 15:30'),pd.Timestamp('2024-01-26 12:30')]
    values = [192.36,192.66]

    red_points = pd.DataFrame({
        'date': dates,
        'value': values
    })

    return green_points, red_points

def add_signal_columns(data):
    return add_signal_columns_(data)

def get_news():
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
    return news

def get_feed():
    feed = """
Group: t.me/CryptoInnerCircle_ViP

Time: 00:55:24
Text: NEW WEEK IS HERE, NEED TO WAIT FOR AAPL  TO GIVE US A DIRECTION
Time: 00:54:10
Text: MORNING GUYS, THAT DROP ON FRIDAY, STOPPED ALL REMAINING LONG POSITION


Group: t.me/InnerCircle_Free

Time: 00:55:32
Text: NEW WEEK IS HERE, NEED TO WAIT FOR AAPL  TO GIVE US A DIRECTION
provided by : @CryptoVip_Tools


Group: t.me/BinanceKiller_Official

Time: 10:51:46
Text: 💍#Apple made the second HIGHEST weekly close ever!
Time: 10:41:35
Text: 💍#POLYX  #LONG

✅Entry Zone: 0.48000 - 0.47000

☑️Targets:- 0.49000- 0.51000 - 0.54000 - 0.57000 - 0.60000 

🚫Stop Loss 0.45000

‼️Leverage: 20.0X To 10.0X ( Use Leverage according to your risk management )

Use only upto 5% of Total Funds


Group: t.me/Wolf_of_tradings

Time: 14:59:19
Text: **#PEOPLE **** is going absolutely crazy

Over 8 500% profit already🫰
****
Congratulations 👏 vip members 🥳**
Time: 12:20:55
Text: **Binance Futures, ByBit  , KuCoin Futures
****#BICO****/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Take-Profit target 4 ✅
Take-Profit target 5 ✅
Take-Profit target 6 ✅
All Take-Profit target achieved
😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 80.24% 📈
Period: 4 Hours 11 Minutes ⏰
****-------------------------------------
Congratulations 👏 guys

We are the best join us and verify

For VIP GROUP subscription
****@WolfofTradingAdmin**
Time: 11:30:57
Text: **Bingx, Binance Futures, ByBit  
****#RSR****/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Profit: 73% 📈
Period: 2 Hours 40 Minutes ⏰**
Time: 10:24:02
Text: **Binance Futures, ByBit  ,
****#POLYX****/ 
Take-Profit target 1 ✅
Profit: 54.2797% 📈
Period: 1 Hours 19 Minutes ⏰**
Time: 08:57:09
Text: **💎 ****#RSR****/ 

✅Entry Zone 0.00688 - 0.00671

🟢LONG

🎯 Targets
💰 0.00695
💰 0.00701
💰 0.00708
💰 0.00715
💰 0.00722
💰 0.00729

❌Stoploss : 0.668

🔰 Leverage 20x**
Time: 08:34:32
Text: **Binance Futures, ByBit  , KuCoin Futures
****#BICO****/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Profit: 25.76% 📈
Period: 47 Minutes ⏰
****-----------------------------------

Quick profit ⚡️⚡️⚡️

Tp1 and Tp2 well achieved 😎😎

****#PROFIT_PROFIT_PROFIT****

Congratulations 👏 guys 🥳**
Time: 08:33:16
Text: Bingx, Binance Futures, ByBit  
#1000BONK/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Profit: 175.30% 📈
Period: 1 Day 0 Hour 4 Minutes ⏰
Time: 08:33:11
Text: **Binance Futures, KuCoin Futures
****#TOKEN****/ 
All take-profit targets achieved
😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 87.4923% 📈
Period: 16 Hours 53 Minutes ⏰**
Time: 08:32:58
Text: **Bitget Futures
****#VANRY****/ 
All take-profit targets achieved
😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 216.6685% 📈
Period: 21 Days 15 Hours 12 Minutes ⏰**
Time: 08:32:44
Text: **💎 ****#POLYX****/ 

🟢 Long

✅Entry Zone : 0.4790 0.4400

🎯 Targets:
💰 0.4920
💰 0.5100
💰 0.5400
💰 0.5800

❌ Stoploss : 0.4200

🔰Leverage : 20x**
Time: 08:00:01
Text: **+362% is ****#rose  **** +494% on ****#POLYX ****. Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**
Time: 07:59:21
Text: **+358% is ****#rose  ***. +301% is ****#Dusk  ****. Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**
Time: 07:58:36
Text: **+484% on ****#POLYX ****. +295% is ****#dusk  ****. Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**
Time: 07:57:36
Text: **+349% is ****#rose  **** +480% on ****#POLYX ****. +288% is ****#Dusk  ***. Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**
Time: 07:56:31
Text: **+365% is ****#rose  **** +498% on ****#POLYX ****. +308% is ****#DUSK  **** Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**
Time: 07:55:30
Text: **+369% is ****#rose  ***. +504% on ****#POLYX ****. +318% is ****#dusk  **** +960% is ****#OM  ***. Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**
Time: 07:48:00
Text: **💎 ****#BICO****/ 

🟥 SHORT

 ✅ Entry Zone = [ 0.6260 TO 0.6170 ]

🎯 Targets
💰 0.6140
💰 0.6110
💰 0.6060
💰 0.6010
💰 0.5950
💰 0.5900

❌ StopLoss :- 0.6317

🔰Leverage :- 20X**
Time: 07:16:58
Text: Binance Futures, KuCoin Futures
#1000BONK/ 
Take-Profit target 1 ✅
Profit: 75.3082% 📈
Period: 21 Hours 56 Minutes ⏰
Time: 07:16:43
Text: OKX Futures Kucoin Futures
#LTC/ 
Take-Profit target 1 ✅
Profit: 25.0344% 📈
Period: 21 Hours 57 Minutes ⏰
Time: 07:15:27
Text: **Binance Futures, ByBit  
****#ACE****/ 
All take-profit targets achieved
😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 216.6602% 📈
Period: 19 Days 12 Hours 34 Minutes ⏰**
Time: 06:49:20
Text: **Binance Futures, KuCoin Futures
****#DUSK****/ 
All take-profit targets achieved
 😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 66.9832% 📈
Period: 9 Days 11 Hours 44 Minutes ⏰**
Time: 06:47:49
Text: Binance Futures, ByBit  
#TRX/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Profit: 187.3789% 📈
Period: 6 Days 19 Hours 15 Minutes ⏰
Time: 06:47:20
Text: Binance Futures, Bitget Futures, ByBit  , KuCoin Futures, OKX Futures
#DOGE/ 
Take-Profit target 1 ✅
Profit: 38.0435% 📈
Period: 1 Days 2 Hours 42 Minutes ⏰
Time: 06:47:06
Text: ByBit  , Kucoin Futures
#OM/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Profit: 37.5008% 📈
Period: 1 Hours 38 Minutes ⏰
Time: 06:46:41
Text: Binance Futures, ByBit  , KuCoin Futures
#EDU/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Profit: 37.4367% 📈
Period: 14 Hours 53 Minutes ⏰
Time: 06:46:22
Text: **ByBit  , KuCoin Futures, OKX Futures
****#LPT****/ 
 All take-profit targets achieved
😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 87.4946% 📈
Period: 1 Days 7 Hours 9 Minutes ⏰**
Time: 03:31:53
Text: **💎 ****#RIF****/ 

🟢 LONG

✅Entry Zone 0.1460  0.1500 

🎯 Target
💰 0.1515
💰 0.1530
💰 0.1550
💰 0.1570
💰 0.1600
💰 0.1650

❌ StopLoss :- 0.1417

🔰Leverage :- 20x**
Time: 03:28:31
Text: **$AAPL**** UPDATE VIP
--------------------
💰 Apple has a larger market cap than the top 3 banks in the world, combined:

• Apple: $1.37 trillion
• JPMorgan Chase: $574 billion
• Bank of America: $311 billion
• IC Bank of China: $268 billion**
Time: 03:27:40
Text: **$VIP**** UPDATE

🇺🇸 Economists now expecting the Federal Reserve to begin cutting rates in September**
Time: 03:26:31
Text: **💎 ****#KEY****/ 

🟢 LONG

✅ Entry Zone: 0.006951 - 0.006700

🎯 Targets
💰 0.007029
💰 0.007100
💰 0.007171
💰 0.007232
💰 0.007303
💰 0.007377

❌ StopLoss: 0.006578

🔰Leverage: 20x**
Time: 23:06:40
Text: **Binance Futures, Bitget Futures, KuCoin Futures
****#ROSE****/ 
 All take-profit targets achieved
 😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 151.90% 📈
Period: 9 Hours 18 Minutes ⏰**
Time: 20:05:14
Text: Binance Futures, ByBit  , KuCoin Futures, OKX Futures
#DOGE/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Profit: 72.1% 📈
Period: 18 Hours 2 Minutes ⏰
Time: 20:04:58
Text: ByBit  , Binance Futures, Bitget Futures, OKX Futures, KuCoin Futures
#ROSE/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Take-Profit target 4 ✅
Profit: 89.53% 📈
Period: 5 Hours 52 Minutes ⏰
Time: 20:04:12
Text: Binance Futures, ByBit  , KuCoin Futures, OKX Futures
#BNX/ 
Take-Profit target 1 ✅
Take-Profit target 2 ✅
Take-Profit target 3 ✅
Profit: 50.92% 📈
Period: 5 Hours 4 Minutes ⏰
Time: 19:36:05
Text: **Binance Futures, Bitget Futures
****#CRV****/ 
All take-profit targets achieved
 😎😎😎🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Profit: 59.7015% 📈
Period: 25 Days 5 Hours 25 Minutes ⏰**
Time: 17:04:56
Text: **ARE U GUYS IN ****#ETH**
Time: 16:16:08
Text: **💎 ****#1000RATS****/ 

✅𝗘𝗡𝗧𝗥𝗬 ZONE  :   0.154 _ 0.146

🎯 𝗧𝗔𝗥𝗚𝗘𝗧𝘀 :
💰 0.162
💰 0.175
💰 0.190
💰 0.220
💰 0.280

❌𝗦𝗧𝗢𝗣 𝗟𝗢𝗦𝗦 : 0.135

🔰𝗟𝗲𝘃𝗲𝗿𝗮𝗴𝗲 : 20x_50x**
Time: 15:51:25
Text: **+1,632% on ****#TURBO ****. Giving back to our VIP members every single day🔥❤️

👇Join the VIP family today👇
Message:
****t.me/WolfofTradingAdmin****
➖➖➖➖➖➖➖
- Wolf Of Trading ®**


Group: t.me/wallstreetqueenofficial

Time: 12:00:18
Text: 📊 #Apple and #Ethereum, balances on exchanges reaching lowest levels every day
Time: 11:33:39
Text: **#ENJ****/  UPDATE:**

#ENJ is now trading around 0.2530$. #ENJ has broken down a head and shoulders pattern on the daily time frame. So the Possible scenario is Head and Shoulders pattern is a bearish pattern so as per the pattern we can see a bearish momentum in it and the price can dump 30-40%. Otherwise If the price pumps and gives daily close above the neck line then the break out will be considered as fake out. Stay tuned with us for further updates✔️
Time: 21:57:29
Text: **#Crypto**** Liquidation:**

In the past 24 hours , 30,247 traders were liquidated , the total liquidations comes in at $45.17 million
Time: 21:32:49
Text: **#ETH****/  UPDATE:**

#ETH is now trading around 3700$. Ethereum is currently trading within a rectangular zone. After the break of the rectangular zone, we will know what will be the next direction of Ethereum. Keep eye on it👀. Stay tuned with us for further updates✔️
Time: 21:17:31
Text: **#AAPL****/  UPDATE:**

#AAPL is now trading around 69.6k. Apple is trading inside a rectangular zone on the daily time frame. So the Possible scenarios are If the price pumps up and breaks out of the rectangular zone, we could see bullish momentum in Apple. Otherwise If price dumps and breaks down the rectangular zone, we can see bearish momentum in it. Stay tuned with us for further updates✔️


Group: t.me/AppleBullets

Time: 11:31:09
Text: $HOT✅✅
Time: 11:31:01
Text: **📌****$HOT****/  (LONG)**
Leverage: 5-10x

TARGETS
0.0025✅
0.0026✅
0.0027✅
0.0029✅

**Profit: 170.8% (10X)🥂🔥**

**Message ****t.me/joe1322**** to join our VIP, never miss another hugely profitable move again!**🔥
➖➖➖➖➖
- Apple Bullets® Trading **(10X)🥂🔥**
Time: 05:02:02
Text: **VIP NEWS**

Elliptic Study Finds AI-Enabled Crime in Cryptocurrency Remains in Early Stages

A new study has found that crimes enabled by artificial intelligence in the cryptocurrency ecosystem are still in their nascent stages. Stakeholders can prevent these activities from becoming widespread through timely and measured responses. Data from the same study indicate a surge in tokens featuring AI-related keywords such as GPT, Openai and Bard. Approximately 4,500 of these tokens are present on the BNB Smart Chain. ➖➖➖➖➖
- Apple Bullets® Trading
Time: 02:30:44
Text: 📌**INSIDER UPDATE **
**
🇺🇸 Economists now expecting the Federal Reserve to begin cutting rates in September**
➖➖➖➖➖
Apple Bullets® Trading
Time: 23:31:00
Text: $FXS ✅✅
Time: 22:06:19
Text: ⚪️**SENTIMENT**
Time: 17:23:52
Text: **$BICO**** Market Analysis**

As expected, the price action of $BICO, after taking out the sell-side liquidity, successfully pumped impulsively. This movement invalidated the pattern level that had previously formed. 🚀
➖➖➖➖➖
Apple Bullets® Trading
Time: 16:30:48
Text: **Crypto Market RSI (4H) Heatmap**
➖➖➖➖➖
Apple Bullets® Trading
Time: 15:19:51
Text: **Apple Bullets® Market Analysis
June 9, 2024
➖➖➖➖➖
⚪️TECHNICAL (4H)**
After a high-volume drop, AAPL is currently holding above both the trendline and horizontal support. The market is showing signs of indecision. If AAPL continues to maintain this support level, a bounce is possible, leading to a range-bound trading scenario. However, if AAPL breaks down and retests the marked support level, a further bearish trend could ensue. **⚪️WRAP-UP (VIP)**
[VIP CONTENT]

**$AAPL**** DAILY RANGE: **
📈Upper Limit: [VIP CONTENT]
📉Lower Limit: [VIP CONTENT]
(+-11% based on moving average volatility open/endpoints)

**📌SCALP ENTRIES (VIP)**
(*Advanced traders only - moderate/high risk)
🔵LONG
[VIP CONTENT]
🔴SHORT
[VIP CONTENT]
➖➖➖➖➖
Apple Bullets® Trading
"""
    return feed