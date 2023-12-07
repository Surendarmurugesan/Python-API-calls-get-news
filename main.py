import requests
from send_mail import send_email

api_key = "<API_KEY_DAILY_NEWS>"
url = "https://newsapi.org/v2/everything?q=google&" \
    "sortBy=publishedAt&apiKey=" \
    "<API_KEY_DAILY_NEWS>"

# make a request to get the news information using api call
request = requests.get(url)

# store a dictionary with data
context = request.json()

body = ""
# Execute the each articles.
for article in context["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + \
            str(article["description"]) + 2*"\n"
body = body.encode("utf-8")
send_email(daily_news=body)
