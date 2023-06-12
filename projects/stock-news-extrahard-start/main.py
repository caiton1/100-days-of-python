# Imports
import os
import requests
from twilio.rest import Client
import os

# What stock to watch and company name to search for on news
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

# endpoints and authorization
stock_endpoint = "https://www.alphavantage.co/query"
stock_key = os.getenv("ALPVANKEY")

news_key = os.getenv("NEWSKEY")
news_endpoint = "https://newsapi.org/v2/top-headlines"

twilio_account_id = os.getenv("TWILIO_ACC")
twilio_auth = os.getenv("TWILIO_TOKEN")

# percent threshold to detect when a significant change in stock price occurs
perecent_threshold = .04

# parameters for api call
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_key,
    "outputsize": "compact"
}

news_params = {
    "apiKey": news_key,
    "q": COMPANY_NAME,
    "pageSize": "3",
    "country": "us"
}

# get stock data
stocks = requests.get(stock_endpoint, params=stock_params)
stocks.raise_for_status()
stock_data = stocks.json()["Time Series (Daily)"]
data_list = [value for (key,value) in stock_data.items()]

yesterday_closing = float(data_list[0]["4. close"])
day_before_closing = float(data_list[1]["4. close"])

difference = (day_before_closing - yesterday_closing)/day_before_closing

# check for significant difference between two days
if abs(difference) > perecent_threshold:
    # get newest relavant news articles
    news = requests.get(news_endpoint, params=news_params)
    news.raise_for_status
    news_list = news.json()["articles"]
    
    # format percent
    percent_change = int(difference * 100)

    # for each article, sned a SMS message to desired phone number
    for article in news_list:
        title = article["title"]
        description = article["description"]

        
        if difference < 0:
            message = f"{STOCK} 🔻 {percent_change}%\nHeadline: {title}\nBrief: {description}\n"
        else:
            message = f"{STOCK} 🔺 {percent_change}%\nHeadline:{title}\nBrief:{description}\n"

        print(message)

        client = Client(twilio_account_id, twilio_auth)
        message = client.messages.create(
            body=message,
            from_="+18339092852",
            to=os.getenv("MY_CELL")
            )


