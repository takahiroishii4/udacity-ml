from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

string1 = "hi Taka the self driving car will be late Best Roger"
string2 = "hi roger the machine learning class will be great great great Best Taka"
string3 = "hi Taka the machine learning class will be most excellent"
email_list = [string1, string2, string3]

bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
print (vectorizer.vocabulary_.get("great"))
