from c_shop.models import Member, Board, BoardImages, BoardLike
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect
import os.path 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def create(request):
    
    try:
#        
        if request.session['id'] == None:
            return redirect('/login')
        
        user = get_object_or_404(Member, pk=request.session['id'])
        
        data = {
            'user' : user,
            'title' : request.POST['title'], #200
            'content' : request.POST['content'],
            'category' : request.POST['category']
        }        
        new_board = Board.objects.create(**data)
        
        if ( 'file' in request.FILES and request.FILES['file'] is not None):
            print(request.FILES['file'])
            file = request.FILES['file']
            board_file = ProjectImages.objects.create(project=new_board, photo=file, filename=file.name)
            print(board_file)
            
        print(new_board)
        
        return HttpResponse(status=200)
        # return redirect('/project')
    except Exception as e :
        print(e)
        return HttpResponse(status=400)
    

    
    
# 보류 헤헹
def update(request):   
    try:       
        print('update')
        
        return HttpResponse(status=200)
    except Exception as e :
        print(e)
        return HttpResponse(status=400)   
    
    
    
def delete(request, id):   
    try:
        if request.session['id'] == None:
            return redirect('/login')
        
        print('delete')
        
        user = get_object_or_404(Member, pk=request.session['id'])    
        delboard = Board.objects.get(pk=id, user=user)     
        print(delboard)

        delboard.delete()
        
        return redirect('/community/list')
    except Exception as e :
        print(e)
        return HttpResponse(status=400)    
    
    
    
