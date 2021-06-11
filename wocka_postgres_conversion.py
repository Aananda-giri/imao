from jokes.models import WockaJokes

jokes=[]
joke={}

objects = WockaJokes.objects.all()
for obj in objects:
    joke['id'] = obj.id
    joke['title'] = obj.title
    joke['body'] = obj.body
    joke['author'] = obj.author
    joke['votes'] = obj.votes
    joke['funney'] = obj.funney
    joke['rating_letters'] = obj.rating_letters
    joke['category'] = obj.category
    joke['shares'] = obj.shares
    joke['pub_date'] = obj.pub_date
    joke['read'] = obj.id
    
    jokes.append(joke)

with open("wocka_postgres.json", "a") as f:
                    json.dump(jokes, f, indent=4, sort_keys=True)

#jokes=[{'id':'1','title':'cow',...},{}]


#To load:
import json
from jokes.models import WockaJokes
from django.utils import timezone

jokes=[]
with open('/home/intelligence/Music/jokeleopedia/wocka.json', "r") as f:
    jokes = json.load(f)

for joke in jokes:
    j = WockaJokes(
    id = joke['id'],
    title = joke['title'],
    body = joke['body'],
    funney = joke['funney'],
    rating=joke['rating'],
    category = joke['category'],
    pub_date = timezone.now(),
    )
    j.save()
    print('saved: ' + str(joke['id']))

jokes_catogaries=postgreas...
for category in catogeries:
    cat.append({category:shorted_ranking_list})
    
