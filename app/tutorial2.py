"""
  A. Ekin Turken
  Radical Software, Fall 2021
  Project 1
  Sept 23, 2021
  python3
"""


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




#Option4 = Logic
#string_template = "Hi there, I'm {}, master of {}."

#word_list1 = [ "Gritty", "Nicolas Cage" ]
#word_list2_a = [ "monsters", "playing hockey", "scaring people" ]
#word_list2_b = [ "movies", "acting", "saying 'woah'" ]

#if word1 == "Gritty":
#    word2 = random.choice(word_list2_a)
#elif word1 == "Nicolas Cage":
#    word2 = random.choice(word_list2_b)

#message = string_template.format(word1,word2)




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

template_list = [ "Today you are {} poorer in TRY, {}.",
                  "Today you are {} richer in TRY, {}." ]
word_list1 = [ "0.6%", "0.54%", "0.73%", "0.22%", "0.66%", "0.94%", "3.2%", "2.4%", "1.1%" ]
word_list2 = [ "yay!!", "too bad", "awesome!" ]

template = random.choice(template_list)
word1 = random.choice(word_list1)
word2 = random.choice(word_list2)
message = template.format(word1,word2)

api.update_status(message)

print("Done.")
