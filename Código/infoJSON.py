import json

comments = json.load(open('Data/comments.json'), encoding='utf-8')

comentarios = []

try:
  for feed in comments['feed']['data']:
    for comment in feed['comments']['data']:
      print(comment['message'])
      comentarios.append(comment['message'])
except:
  pass

feed = json.load(open('Data/feed.json', encoding='utf-8'))
try:
  for comment in feed['feed']['data']:
    print(comment['message'])
    comentarios.append(comment['message'])
except:
  pass

with open("salida.csv", "a") as f:
    for c in comentarios:
        f.write(c)
        f.write('\n')
