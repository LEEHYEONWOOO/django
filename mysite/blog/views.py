from django.shortcuts import render
from django.http import HttpResponse
from .models import Board1
from django.core import serializers
from django.http import JsonResponse
from .forms import Board1Form
import json
from django.db.models import Max
import datetime


# Create your views here.3

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'}
]
def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href=/read/{topic["id"]}>{topic["title"]}</a></li>'
    return HttpResponse(1)

def get_BoardList(request):
    bid_value = request.GET.get('Bid')
    if bid_value != '0':
        print(f'get boardList = {bid_value}')
        post = Board1.objects.values('num','title','writer','regdate','readcnt')
        filtered_data = post.filter(boardid=bid_value)
        post_list = list(filtered_data)
        return JsonResponse(post_list, safe=False)
    else:
        print('전체 글 보기')
        post = Board1.objects.values('num','title','writer','regdate','readcnt')
        json_post = list(post)
        return JsonResponse(json_post, safe=False)
    
def get_BoardDetail(request):
    bnum_value = request.GET.get('Bnum')
    print(f'get boardDetail = {bnum_value}')
    post = Board1.objects.values('num','title','writer','regdate','readcnt','content')
    filtered_data = post.filter(num=bnum_value)
    post_list = list(filtered_data)
    return JsonResponse(post_list, safe=False)

def Board_write(request):
    data = json.loads(request.body)
    max_num = Board1.objects.aggregate(Max('num'))
    max_value = max_num['num__max']
    data['num']=max_value+1
    data['boardid']=2
    data['regdate']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['readcnt']=0
    form = Board1Form(data)
    if form.is_valid():
        form.save()
        print(f'{max_value}번글 글작성 완료')
        return JsonResponse({'success': True, 'message': 'Data saved successfully'})
    else:
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
def Pass_chk_Submit(request):
    data = json.loads(request.body)
    num_value = data['num']
    pass_field_value = data['pass_field']
    print(data)  # This will print all POST data
    print(num_value)
    print(pass_field_value)
    post = Board1.objects.values('num','content','pass_field')
    filter_post = post.filter(num=num_value)
    for item in filter_post:
        db_pass_field = item.get('pass_field')
    if db_pass_field==pass_field_value:
        return JsonResponse({'success': True, 'message': 'pass'})
    else:
        return JsonResponse({'success': False, 'message': 'wrong pass'})
    

        
    
    
    
    
    
    



