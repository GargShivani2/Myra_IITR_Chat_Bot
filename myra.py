from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
count_vect = joblib.load("count_vect.pkl")
clf_count = joblib.load("clf_count.pkl")

from res_map import responses
res = responses()

print 'input your query'
ask = raw_input()
test_example = [ask]
test_example_count = count_vect.transform(test_example)
probs = clf_count.predict_proba(test_example_count)[0]
out = clf_count.predict(test_example_count)[0]
outn = int(out)
print res[outn]

print out