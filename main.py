import tweepy
import json
from textblob import TextBlob
from flask import Flask
app = Flask(__name__)
app.debug= True
@app.route('/')
def index():
    return"<h1 style='color: red'>hello flask app</h1>"
@app.route('/name/<name>')
def show_name(name):
    return"<h1 style='color: red'>%s</h1>" %name
@app.route('/topic/<topic>')
def api(topic):
    counter=0
    consumer_key="1Q3L2puibfh1NnUcZutJPSnfk"
    consumer_secret="gEivx0bjCOTFqkadLNhowOSjUw13uj2LY0WDD3llEhJ4zEpxDC"
    access_token="952154526416437249-LnWHZ20jtID50kR23VYADszNBFcpJen"
    access_token_secret="Cmrt1ufccXgsxTI98V1TxzoL0RkAMxGc99Rrx3t1Dnzj7"
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    public_tweets=api.search(topic,count=100)
    ptive=0.0
    ntive=0.0
    neut=0.0

    for tweet in public_tweets:
        encoded=(tweet.text)
        en=encoded.encode("utf-8", errors='ignore')
        analysis=TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            ptive+=1
        elif analysis.sentiment.polarity < 0:
            ntive+=1
        elif analysis.sentiment.polarity == 0:
            neut+=1
    result_dict={'TotalTweets':100,'PossitiveTweets':ptive,'NegativeTweets':ntive,'NeutralTweets':neut}
    return json.dumps(result_dict)

if __name__=="__main__":
    app.run()
    dump()
