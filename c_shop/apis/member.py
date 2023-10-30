from c_shop.models import Member
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect


def create(request):
    try:
        Member.objects.create(
            _id=request.POST['id'],
            pw=request.POST['pw'],
            name=request.POST['name']
        )
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=400)
    
def login(request):
    try:
        user = get_object_or_404(Member, pk=request.POST['id'], pw = request.POST['pw'])
        request.session['id'] = user._id
        request.session['name'] = user.name
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)
def logout(request):
    try:
        request.session['id'] = None
        request.session['name'] = None
        return redirect('/')
    except:
        return redirect('/')
    
def update(request):
    try:
        data = {}
        post = request.POST
        for key in post.keys():
            data[key] = post[key]
        del data['csrfmiddlewaretoken']
        print(data)
        Member.objects.filter(pk=request.session['id']).update(**data)
        # get_object_or_404(Member, pk=request.session['id']).update(post)
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
    

# def read(pk):
#     try:
#             question = get_object_or_404(Question, pk=question_id)

#         result = Member.objects.filter(pk=pk)
#         if(result < 1):
#             return NOT_FOUND_USER
#         return result
#     except:
#         return UNKNOWN_ERROR

# def update(member):
#     try:
#         member.save()
#         return SUCCESS # true: 성공, false: 실패
#     except:
#         return UNKNOWN_ERROR
    
# def delete(pk):
#     try:
#         result = Member.objects.filter(pk=pk)
#         if(result < 1):
#             return NOT_FOUND_USER
        
#         result.delete()
#         return SUCCESS # true: 성공, false: 실패
#     except:
#         return UNKNOWN_ERROR
