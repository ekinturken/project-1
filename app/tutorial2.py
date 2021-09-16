import tweepy

from authorization_tokens import *

import random

message = ""

#option1
#phrase_list = ["hi", "ciao", "hola"]
#message = random.choice(phrase_list)



#option2: A simple mad lib

#string_template = "Some people like {} but I like {}."
#word_list = [ "sports", "skorts", "meatloaf", "monsters", "hockey", "badminton" ]
#word1 = random.choice(word_list)
#word2 = random.choice(word_list)
#message = string_template.format(word1,word2)


#Option 3 = a list of possible mad libs
#template_list = [ "My name is {} and I like {}.",
#                  "People say I look like {} but only when I'm {}.",
#                  "I think {} is the best at {}." ]
#word_list1 = [ "Gritty", "Rory", "Nicolas Cage" ]
#word_list2 = [ "playing hockey", "coding", "acting" ]

#template = random.choice(template_list)
#word1 = random.choice(word_list1)
#word2 = random.choice(word_list2)
#message = template.format(word1,word2)


#Option4 = Logic
string_template = "Hi there, I'm {}, master of {}."

word_list1 = [ "Gritty", "Nicolas Cage" ]
word_list2_a = [ "monsters", "playing hockey", "scaring people" ]
word_list2_b = [ "movies", "acting", "saying 'woah'" ]

if word1 == "Gritty":
    word2 = random.choice(word_list2_a)
elif word1 == "Nicolas Cage":
    word2 = random.choice(word_list2_b)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)

print("Done.")
