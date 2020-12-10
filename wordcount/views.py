from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    #return HttpResponse('Hello')
    return render(request,'home.html',{"name":"Shivoy Dixit"})
def about(request): return render(request,'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    worddict={}
    for word in fulltext.split():worddict[word]=worddict.get(word,0)+1
    sortedwords=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'sortedwords':sortedwords})
