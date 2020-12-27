#import wolframalpha
import wikipedia
import requests

#appId = ''
#client = wolframalpha.Client(appId)

    

def search_wiki(keyword):
  # query=wikipedia.suggest(keyword)
  # if query!= None:
  #   keyword=query
  # # print(query)
  try:
    results = wikipedia.summary(keyword,sentences=2)
  except wikipedia.exceptions.DisambiguationError as e:
    results = wikipedia.summary(e.options[0])
  except wikipedia.exceptions.PageError as e:
    print("Here is what we found on google")
    webbrowser.open("https://google.co.in/search?q=%s" % keyword)
    pass
  except wikipedia.exceptions.HTTPTimeoutError as e:
    print("check your internet connection and try again") 
  print(results)


def search(text=''):
  res = client.query(text)
  print(res)
  if res['@success']==True:
    try:
      print("wolf")
      answer =next((res.results)).text
      print(answer)
    except StopIteration as e:
      # print("Wiki")
      pod0 = res['pod'][0]
      question = resolveListOrDict(pod0['subpod'])
      # removing unnecessary parenthesis
      question = removeBrackets(question)
      # searching for response from wikipedia
    #      print(question)
      search_wiki(question)
  else:
      # pod0 = res['pod'][0]
      # question = resolveListOrDict(pod0['subpod'])
      # # removing unnecessary parenthesis
      # question = removeBrackets(question)
      # # searching for response from wikipedia
      # #      print(question)
      search_wiki(text)
  
def removeBrackets(variable):
  return variable.split('(')[0]

def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']

def primaryImage(title=''):
    url = 'http://en.wikipedia.org/w/api.php'
    data = {'action':'query', 'prop':'pageimages','format':'json','piprop':'original','titles':title}
    try:
        res = requests.get(url, params=data)
        key = res.json()['query']['pages'].keys()[0]
        imageUrl = res.json()['query']['pages'][key]['original']['source']
        print(imageUrl)
    except Exception as err:
        print('Exception while finding image:= '+str(err))
 
 

if __name__ == '__main__':
  # search_wiki('Sharakuh khan')
  search('Who is Donald trump')
  search('What is 2+2')
