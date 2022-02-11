from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def result(request):
    word=request.GET['word']
    dictionary=PyDictionary()
    meaning=dictionary.meaning(word)
    synonyms=dictionary.synonym(word)
    antonyms=dictionary.antonym(word)
    data={
        'word':word,
        'meaning':meaning,
        'synonyms':synonyms,
        'antonyms':antonyms,
    }
    return render(request, 'webpages/result.html',data)