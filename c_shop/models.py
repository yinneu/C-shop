from django.db import models
import os
from uuid import uuid4

class Member(models.Model):
    _id = models.CharField(max_length=200, primary_key=True)
    pw = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    github = models.CharField(max_length=200, default="")
    isOB = models.BooleanField(default=False)
    currentCoin = models.IntegerField(default = 0)
    sumCoin = models.IntegerField(default = 0)
    email = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    postalCode = models.TextField(max_length=200, default="")
    aboutMe = models.TextField(max_length=200, default="")
    plantName = models.TextField(default="애랑이")
    plantExp = models.IntegerField(default = 0)
    plantRebirth = models.IntegerField(default = 0)
    
    
 
def rename_imagefile_to_uuid(instance, filename): 	# instance : Feed 모델에서 __str__로 반환해주는 값 현재는 title로 지정
    												# filename : 원본 파일명
    upload_to = f'project/' 			# 파일 저장 위치 설정
    ext = filename.split('.')[-1]        			# 원본 파일명 text.jpg->[text, jpg]로 나누어주고 -1 번째 값만 ext에 담아주기
    uuid = uuid4().hex                   			# 50da5daca34d4802a771047ee463c234 이런 형식에 임의에 이름 생성
    filename = '{}.{}'.format(uuid, ext) 			# '{uuid}.{ext}' -> 50da5daca34d4802a771047ee463c234.jpg
										 			# format(uuid, ext) -> uuid = 파일명, ext = 파일 형식
    return os.path.join(upload_to, filename)		# DB에 저장할 값을 리턴



class Board(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.TextField(default="")
    content = models.TextField(default="")
    category = models.IntegerField()
    link = models.CharField(max_length=400)
    anonymous = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    
    
class BoardLike(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    
         
class BoardImages(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="board", null=True)
    filename = models.CharField(max_length=64, null=True)
    

    

    
    
class Project(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    teammate = models.CharField(max_length=200, default="")
    summary = models.TextField(default="")
    content = models.TextField(default="")
    category = models.IntegerField() # 소속팀명 (태그 등등)
    link = models.CharField(max_length=400, default="")
    anonymous = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
class ProjectLike(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    
         
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to=rename_imagefile_to_uuid, null=True)   
    filename = models.CharField(max_length=64, null=True)

    
    
    
class Company(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    obName = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    summary = models.TextField(default="")
    effect = models.TextField(default="")
    price = models.TextField(default="")
    logoImages = models.TextField(default="")
    backgroundImages = models.TextField(default="")
    

