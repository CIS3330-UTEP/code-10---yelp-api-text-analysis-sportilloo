# Servando Portillo - ID: South Carolina
# CIS 3330
# CODE 10 - Yelp API Text Analysis

import nltk
from yelpapi import YelpAPI
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


stop_words = set(stopwords.words('english'))
analyzer = SentimentIntensityAnalyzer()


def main():
    # API Key
    api_key = "Y1RKEfzmlZ8Ds6p5EknBUIaJx3Xyti9YcTtbNj8gEAPCWf6unE7zefBpu1y7wwmgGeaKYrkOlZpz2jZF4IhEM8WxPdaZYr4M7jBV9ctY1JXlad87vwRZDmttp_4yZHYx"


    # API Variable
    yelp_api = YelpAPI(api_key)
    

    # Search query
    search_term = "Mexican"
    search_location = "El Paso, TX"
    search_sort_by = "review_count"   
    search_limit = 20
    aliases_list = []

    for i in range(4):
        search_offset = i * 20
        search_results = yelp_api.search_query(term=search_term, location=search_location, sort_by=search_sort_by, limit=search_limit, offset=search_offset)
    
        for business in search_results['businesses']:
            #print(business['name'])
            #print(business['alias'])
            aliases_list.append(business['alias'])
            #print("\n")


    # Reviews Query, vaderSentiment to filter reviews with negative scores, tokenization and stop words.
    negative_reviews = []
    for alias in aliases_list:
        reviews = yelp_api.reviews_query(alias)
        for review in reviews['reviews']:
            text = review['text']
            sentiment = analyzer.polarity_scores(text)
            if sentiment['neg'] > sentiment['pos']:
                text_tokens = word_tokenize(text)
                text_without = [word for word in text_tokens if word.lower() not in stop_words]
                without_stop_string = ' '.join(text_without)
                negative_reviews.append(without_stop_string)
    
    print("Negative Reviews for all 80 restaurants: ")
    print("\n")

    for review in negative_reviews:
        print(review)
        print("\n")


if __name__ == "__main__":
    main()