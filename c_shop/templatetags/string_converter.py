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
        