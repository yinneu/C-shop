from django import template

register = template.Library()

@register.filter
def teamCategory(value):
    if(value == 0):
        result = '코어(임베디드)'
    elif(value == 1):
        result = '텐서(AI)'
    elif(value == 2):
        result = '라떼(앱)'
    elif(value == 3):
        result = '태그(웹)'
    elif(value == 4):
        result = '라온(게임)'
    elif(value == 5):
        result = '실드(보안)'
    else:
        result = ''
        
    return result
        
    
    
@register.filter
def communityCategory(value):
    if(value == -1):
        result = 'Community'
    elif(value == 0):
        result = '최신 늬우스'
    elif(value == 1):
        result = '같이 프로젝트 할 사람!'
    elif(value == 2):
        result = 'OB가 구하는 직군'
    elif(value == 3):
        result = 'YB가 구하는 직군'
    elif(value == 4):
        result = '저를 소개합니다.'
    elif(value == 5):
        result = '주의사항'
    elif(value == 6):
        result = '행사'
    elif(value == 7):
        result = '동아리의 시작 ~ 90년대'
    elif(value == 8):
        result = '00년대'
    elif(value == 9):
        result = '10년대'
    elif(value == 10):
        result = '20년대'
    else:
        result = ''
        
    return result    


@register.filter
def categoryExp(value):
    if(value == -1):
        result = '씨애랑 학우분들을 위한 게시판입니다!'
    elif(value == 0):
        result = '씨애랑의 최신 소식을 접해보세요.'
    elif(value == 1):
        result = '같이 프로젝트, 공부할 동료들을 구해보세요.'
    elif(value == 2):
        result = 'OB가 구하는 직군입니다.'
    elif(value == 3):
        result = 'YB가 구하는 직군입니다.'
    elif(value == 4):
        result = '자신을 소개해보세요.'
    elif(value == 5):
        result = '주의사항'
    elif(value == 6):
        result = '행사 안내입니다.'
    elif(value == 7):
        result = '동아리의 시작 ~ 90년대의 씨애랑'
    elif(value == 8):
        result = '00년대의 씨애랑'
    elif(value == 9):
        result = '10년대의 씨애랑'
    elif(value == 10):
        result = '20년대의 씨애랑'
    else:
        result = ''
        
    return result 



    
@register.filter
def sub(value, arg):
    return value - arg