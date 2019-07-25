
# coding: utf-8

# In[1]:


import csv
from res_map import responses
res = responses()

data_path = "C:\Users\GAURABH\Desktop\Chat Bot\data5.csv"
data = []
target=[]
i = 0
with open(data_path) as datafile:
    filereader = csv.reader(datafile,delimiter =',',quotechar='|')
    initial = 0
    for row in filereader:
        if initial == 0:
            initial = 1
            continue
        else:
            data.append(row[0])
            target.append(row[1])
    data = data[1:]
    target = target[1:]


# In[2]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
#import joblib

count_vect = CountVectorizer()
train_counts = count_vect.fit_transform(data)

clf_count = MultinomialNB(alpha=1,fit_prior='false').fit(train_counts,target)
'''
count_path = "trained_model/naive_count/count_vect.pkl"
clf_path = "trained_model/naive_count/clf_count.pkl"

joblib.dump(count_vect,count_path)
joblib.dump(clf_count,clf_path)
'''
joblib.dump(count_vect,'count_vect.pkl')
joblib.dump(clf_count,'clf_count.pkl')

# In[3]:


#test_example = ["will kissing cause hiv"]
#test_example_count = count_vect.transform(test_example)
'''
    def respond(self):
        print 'input your query'
        ask = raw_input()
        vec = self.vector(ask)
        no = self.clf.predict(vec)[0]
        no = int(no)
        return self.res[no]

print 'input your query'
ask = raw_input()
test_example = [ask]
test_example_count = count_vect.transform(test_example)
probs = clf_count.predict_proba(test_example_count)[0]
out = clf_count.predict(test_example_count)[0]
outn = int(out)
print res[outn]


# In[4]:


print out


# In[1]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

count_vect = joblib.load("trained_model/naive_count/count_vect.pkl")
clf_count = joblib.load("trained_model/naive_count/clf_count.pkl")
'''
'''
count_vect = joblib.load("count_vect.pkl")
clf_count = joblib.load("clf_count.pkl")
'''
# In[6]:

'''
test_example = ["will kissing cause hiv"]
test_example_count = count_vect.transform(test_example)
probs = clf_count.predict_proba(test_example_count)[0]
out = clf_count.predict(test_example_count)


# In[9]:


out = out[0]
'''
# In[11]:

'''
from map_englishu import mapping


# In[12]:


mapping[out]
'''
# In[ ]:




