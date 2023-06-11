from django.shortcuts import render
from django.http import HttpResponse
from .search import terra_search
from .search_parser import parse_checker
from django.utils.safestring import mark_safe
# Create your views here.

def index(req):
    return render(req, './Home/index.html')

def query_search(req):
    query = req.GET.get('query')
    res= terra_search(query)
    result=parse_checker(res)
    # print(result)
    params={'re':result}
    return render(req,'./Home/Home.html',params)
