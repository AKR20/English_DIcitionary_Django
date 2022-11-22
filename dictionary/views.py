from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dict = Dictionary(search)
    meanings_list = dict.meanings()
    synonyms_list = dict.synonyms()
    antonyms_list = dict.antonyms()
    context = {
        'search': search,
        'meanings' : meanings_list,
        'synonyms' : synonyms_list,
        'antonyms' : antonyms_list,
    }
    return render(request, 'word.html', context)

