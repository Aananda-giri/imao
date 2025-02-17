#///////////////////###########################\\\\\\\\\\\\\\\\\\\\\\\
#///////////////////***************************\\\\\\\\\\\\\\\\\\\\\\\
#/////////////********To extract Rating number:*********\\\\\\\\\\\\\\
#/////////////********     From wocka jokes:    *********\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\****************************/////////////////////
#\\\\\\\\\\\\\\\\\\\\############################/////////////////////
from bs4 import BeautifulSoup

from lxml import html
import requests
import json
import logging

logging.basicConfig(level=logging.ERROR)

def get_riddles():
    url_base = "https://parade.com/947956/parade/riddles/"
    response = requests.get(url_base)
    soup = BeautifulSoup(response.content)
    return(riddles)


''' --------------------- Output Format ----------------------------------
riddles = {'Math Riddles':[{'id':58, 'riddle':'I am an odd number. Take away a letter and I become even. What number am I?', 
'answer': Seven}], {......}}


'''
c0=0
c1=0
c2=0
c3=0
c4=0
c5=0
categories = [i.text for i in soup.findAll('h2')]
riddles = {}
ps=soup.findAll('p')
for p in ps:
    if('Riddle: ' in p.text):
        id = int(p.text.split('Riddle: ')[0].replace('.',''))
        riddle = p.text.split('Riddle: ')[1].split('Answer: ')[0].strip()
        answer = p.text.split('Riddle: ')[1].split('Answer: ')[1].strip()
        
        if(id<20):
            if(c0==0):
                riddles[categories[0]]=[]
            c0=1
            cat = categories[0]
        elif(id<35):
            if(c1==0):
                riddles[categories[1]]=[]
            c1=1
            cat = categories[1]
        elif(id<58):
            if(c2==0):
                riddles[categories[2]]=[]
            c2=1
            cat = categories[2]
        elif(id<70):
            if(c3==0):
                riddles[categories[3]]=[]
            c3=1
            cat = categories[3]
        elif(id<86):
            if(c4==0):
                riddles[categories[4]]=[]
            c4=1
            cat = categories[4]
        else:
            if(c5==0):
                riddles[categories[5]]=[]
            c=1
            cat = categories[5]
        
        riddles[cat].append({'id':id, 'riddle':riddle, 'answer':answer})

riddles={'Easy Riddles':[









from bs4 import BeautifulSoup

#from lxml import html
import requests
import json
#import logging

def extract_joke_ratings_sub(id):
    """Download and parse a single joke rating and funney level."""

    url_base = "https://www.riddles.com/{}"
    response = requests.get(url_base.format(id))
    soup = BeautifulSoup(response.content)
    
    title = soup.findAll('h1','panel-title riddle_title lead inline')[0].text
    riddle = soup.findAll('p')[0].text
    solutions = soup.findAll('p')[1:-10]
    solutions = [s.text for s in solutions]
    answer = '\n'.join(solutions)
    
    upvotes = int(str(soup.findAll('div','btn btn-lg btn-block share_box_purple text-center mar_bot_10')[0]).split('votes')[2].split('\"')[1])
    downvotes = int(str(soup.findAll('div','btn btn-lg btn-block share_box_purple text-center mar_bot_10')[1]).split('votes')[2].split('\"')[1])
    return(title, riddle, answer, upvotes, downvotes)
























RELATED: Trivia Questions for Kids

Funny Riddles
35. Riddle: What has lots of eyes, but can’t see?
Answer: A potato

36. Riddle: What has one eye, but can’t see?
Answer: A needle

37. Riddle: What has many needles, but doesn’t sew?
Answer: A Christmas tree

38. Riddle: What has hands, but can’t clap?
Answer: A clock

39. Riddle: What has legs, but doesn’t walk?
Answer: A table

40. Riddle: What has one head, one foot and four legs?
Answer: A bed

41. Riddle: What can you catch, but not throw?
Answer: A cold

42. Riddle: What kind of band never plays music?
Answer: A rubber band

43. Riddle: What has many teeth, but can’t bite?
Answer: A comb

44. Riddle: What is cut on a table, but is never eaten?
Answer: A deck of cards

45. Riddle: What has words, but never speaks?
Answer: A book

46. Riddle: What runs all around a backyard, yet never moves?
Answer: A fence 

47. Riddle: What can travel all around the world without leaving its corner?
Answer: A stamp

48. Riddle: What has a thumb and four fingers, but is not a hand?
Answer: A glove

49. Riddle: What has a head and a tail but no body?
Answer: A coin

50. Riddle: Where does one wall meet the other wall?
Answer: On the corner

51. Riddle: What building has the most stories?
Answer: The library 

52. Riddle: What tastes better than it smells?
Answer: Your tongue

53. Riddle: What has 13 hearts, but no other organs?
Answer: A deck of cards

54. Riddle: It stalks the countryside with ears that can’t hear. What is it?
Answer: Corn

55. Riddle: What kind of coat is best put on wet?
Answer: A coat of paint

56. Riddle: What has a bottom at the top?
Answer: Your legs

57. Riddle: What has four wheels and flies?
Answer: A garbage truck

RELATED: 101 Funny Quotes

Math Riddles
58. Riddle: I am an odd number. Take away a letter and I become even. What number am I?
Answer: Seven

59. Riddle: If two’s company, and three’s a crowd, what are four and five?
Answer: Nine

60. Riddle: What three numbers, none of which is zero, give the same result whether they’re added or multiplied?
Answer: One, two and three

61. Riddle: Mary has four daughters, and each of her daughters has a brother. How many children does Mary have?
Answer: Five—each daughter has the same brother.

62. Riddle: Which is heavier: a ton of bricks or a ton of feathers?
Answer: Neither—they both weigh a ton.

63. Riddle: Three doctors said that Bill was their brother. Bill says he has no brothers. How many brothers does Bill actually have?
Answer: None. He has three sisters.

64. Riddle: Two fathers and two sons are in a car, yet there are only three people in the car. How?
Answer: They are a grandfather, father and son.

65. Riddle: The day before yesterday I was 21, and next year I will be 24. When is my birthday?
Answer: December 31; today is January 1.

66. Riddle: A little girl goes to the store and buys one dozen eggs. As she is going home, all but three break. How many eggs are left unbroken?
Answer: Three

67. Riddle: A man describes his daughters, saying, “They are all blonde, but two; all brunette but two; and all redheaded but two.” How many daughters does he have?
Answer: Three: A blonde, a brunette and a redhead

68. Riddle: If there are three apples and you take away two, how many apples do you have?
Answer: You have two apples.

69. Riddle: A girl has as many brothers as sisters, but each brother has only half as many brothers as sisters. How many brothers and sisters are there in the family?
Answer: Four sisters and three brothers

Related: 101 Fun Facts

Word Riddles
70. Riddle: What five-letter word becomes shorter when you add two letters to it?
Answer: Short

71. Riddle: What begins with an “e” and only contains one letter?
Answer: An envelope

72. Riddle: A word I know, six letters it contains, remove one letter and 12 remains. What is it?
Answer: Dozens

73. Riddle: What would you find in the middle of Toronto?
Answer: The letter “o”

74. Riddle: You see me once in June, twice in November and not at all in May. What am I?
Answer: The letter “e”

75. Riddle: Two in a corner, one in a room, zero in a house, but one in a shelter. What is it?
Answer: The letter “r”

Related: Would You Rather Questions

76. Riddle: I am the beginning of everything, the end of everywhere. I’m the beginning of eternity, the end of time and space. What am I?
Answer: Also the letter “e”

77. Riddle: What 4-letter word can be written forward, backward or upside down, and can still be read from left to right?
Answer: NOON

78. Riddle: Forward I am heavy, but backward I am not. What am I?
Answer: The word “not”

79. Riddle: What is 3/7 chicken, 2/3 cat and 2/4 goat?
Answer: Chicago

80. Riddle: I am a word of letters three; add two and fewer there will be. What word am I?
Answer: Few

81. Riddle: What word of five letters has one left when two are removed?
Answer: Stone

82. Riddle: What is the end of everything?
Answer: The letter “g”

83. Riddle: What word is pronounced the same if you take away four of its five letters?
Answer: Queue

84. Riddle: I am a word that begins with the letter “i.” If you add the letter “a” to me, I become a new word with a different meaning, but that sounds exactly the same. What word am I?
Answer: Isle (add “a” to make “aisle”)

85. Riddle: What word in the English language does the following: The first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word?
Answer: Heroine

Related: 101 Funny Puns

Really Hard Riddles
86. Riddle: What is so fragile that saying its name breaks it?
Answer: Silence.

87. Riddle: What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?
Answer: A river

88. Riddle: Speaking of rivers, a man calls his dog from the opposite side of the river. The dog crosses the river without getting wet, and without using a bridge or boat. How?
Answer: The river was frozen.

89. Riddle: What can fill a room but takes up no space?
Answer: Light

90. Riddle: If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?
Answer: A mirror

Parade Daily
Celebrity interviews, recipes and health tips delivered to your inbox.

Email Address
 
91. Riddle: The more you take, the more you leave behind. What are they?
Answer: Footsteps

92. Riddle: I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?
Answer: A key

93. Riddle: People make me, save me, change me, raise me. What am I?
Answer: Money

94. Riddle: What breaks yet never falls, and what falls yet never breaks?
Answer: Day, and night

95. Riddle: What goes through cities and fields, but never moves?
Answer: A road

96. Riddle: I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?
Answer: Fire

97. Riddle: The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?
Answer: A coffin

98. Riddle: A man looks at a painting in a museum and says, “Brothers and sisters I have none, but that man’s father is my father’s son.” Who is in the painting?
Answer: The man’s son

99. Riddle: With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?
Answer: A stapler

100. Riddle: I have lakes with no water, mountains with no stone and cities with no buildings. What am I?
Answer: A map

101. Riddle: What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?
Answer: Nothing
