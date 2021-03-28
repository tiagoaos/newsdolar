


import nltk
import tweepy
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import tokens_tt
import re
from datetime import datetime

tweets = [] # Lista vazia para armazenar scores
tweets_text = []
twets_date = []
tweets_witout_url = []

currDate = datetime.now()

def lasttweet () :
        auth = tweepy.OAuthHandler(tokens_tt.consumer_key, tokens_tt.consumer_secret)
        auth.set_access_token(tokens_tt.access_token, tokens_tt.access_token_secret)
        api = tweepy.API(auth)  
        nltk.download('punkt')
        nltk.download('stopwords')

        stopwords = nltk.corpus.stopwords.words('portuguese')
        print(stopwords)
        public_tweets = api.search('dolar lang:pt (from:InvestingBrasil OR from:valoreconomico OR from:UOLEconomia)',count =30)
        for tweet in public_tweets:
                tweet_tnk_date = []
                dt_obj  = ""
                # analysis = tb(tweet.text)
                
                # print("tran:"+translator.translate(tweet.text))
                # print(analysis.detect_language())
                # polarity = analysis.sentiment.polarity
                # tweets.append(polarity)
                without_url = re.sub(r'http\S+', "", tweet.text)
                without_url =re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', without_url).lower()
                tokens = word_tokenize(without_url)
                filtered_sentence = [w for w in tokens if not w in stopwords]  
                if(datetime.now() - tweet.created_at ).days <3:
                        tweets_text.append(filtered_sentence)
        
        return tweets_text
             


