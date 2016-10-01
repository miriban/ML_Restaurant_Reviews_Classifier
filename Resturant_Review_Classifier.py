"""
    Resturant Reviews Classifier
    Created By Mohammed J. AbuIriban
"""
import graphlab

# loading data ( avaliable on https://d396qusza40orc.cloudfront.net/phoenixassets/course1-for-students/amazon_baby.gl.zip)
products = graphlab.SFrame("amazon_baby.gl/")

# Calculating word counts of each of reviews
products['word_count'] = graphlab.text_analytics.count_words(products['review'])

# words I'm interested in counting
selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']

# selected words count
def selected_words_count(d):
    wordDic = {}
    for word in selected_words:
        if word in d:
            wordDic[word] = d[word]
        else:
            wordDic[word] = 0
    return wordDic

# we will create new column called selected words count
products["selected_words_count"] = products["word_count"].apply(selected_words_count)

"""
This part is for coursera assignment it shows how frequently words appear in reviews
The Result is:
{'fantastic': 932, 'love': 42065, 'bad': 3724, 'awesome': 2090, 'great': 45206, 'terrible': 748, 'amazing': 1363, 'horrible': 734, 'awful': 383, 'hate': 1220, 'wow': 144}

# return value from dict
def word_count(d,word):
    return d[word]

# The most common word
for word in selected_words:
    products[word] = products["selected_words_count"].apply(lambda i: word_count(i, word))


# sumOfValues
total = {}
for word in selected_words:
    total[word] = products[word].sum()

# print total
print total
"""
#ignore all 3 rating
products = products[products['rating'] != 3]
#positive sentiment
products['sentiment'] = products['rating'] >=4
# splitting data
train_data,test_data = products.random_split(0.8,seed=0)

# building the Classifier model
sentiment_classifier = graphlab.logistic_classifier.create(train_data,target="sentiment",features=['selected_words_count'],validation_set=test_data)

# selected words
print sentiment_classifier.evaluate(test_data)

# test
print sentiment_classifier.predict(products[0], output_type='probability')
