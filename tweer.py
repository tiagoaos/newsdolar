def lasttweet(){
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)  
        nltk.download('stopwords')
        stopwords = nltk.corpus.stopwords.words('portuguese')
        print(stopwords)
        
        
}
