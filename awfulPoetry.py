#!python3
#awfulPoetry.py
import random

articles = ['the','a','my', 'their', 'someones']
subjects = ['cat','dog','man', 'woman','gorila']
verbs    = ['sang','ran','jumped', 'farted','burped']
adverbs  = ['loudly','quietly','smelly', 'badly','boldly']

i=0
while i < 5:
  print(articles[random.randint(0,4)],
        subjects[random.randint(0,4)],
        verbs[random.randint(0,4)],
        adverbs[random.randint(0,4)])
  i += 1

print('\nThe End')
