from c_shop.models import Member, Project, ProjectLike, ProjectImages
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
            'team' : request.POST['team'], #100
            'teammate' : request.POST['teammate'], #200
            'summary' : request.POST['summary'],
            'content' : request.POST['content'],
            'category' : request.POST['category'],
            'link' : request.POST['link'],
        }        
        new_project = Project.objects.create(**data)
        
        
        if ( 'file' in request.FILES and request.FILES['file'] is not None):
            print(request.FILES['file'])
            img_file = request.FILES['file']
            project_img = ProjectImages.objects.create(project=new_project, photo=img_file, filename=img_file.name)
            print(project_img)
            
        print(new_project)
        
        add_exp = user.plantExp + 30
        
        if add_exp >= 100:
            add_exp = add_exp % 100
            user.plantRebirth += 1
            user.currentCoin += 1
            user.sumCoin += 1
          
        user.plantExp = add_exp
        user.save()
        
        
        # return HttpResponse(status=200)
        return redirect('/project')
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
        delproject = Project.objects.get(pk=id, user=user)     
        print(delproject)
        
        
        if ProjectImages.objects.filter(project=delproject).exists():
            imgpath = BASE_DIR + '/media/' + str(get_object_or_404(ProjectImages, project=delproject).photo)
            print(imgpath)
            if os.path.isfile(imgpath):
                os.remove(imgpath)
                print('remove the file: ', imgpath)

        delproject.delete()
        
        return redirect('/project')
    except Exception as e :
        print(e)
        return HttpResponse(status=400)    
    
    
    
