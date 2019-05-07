from django.shortcuts import render

# Create your views here.
# response = render
# css, html을 통해서 render
# model DB와 상호작용
# DB 저장공간
# client 가 보낸 것을 model을 보내 데이터베이스에 저장
# model 추상적 개념 DB 구체적 개념
# post 모델링 - title - stirng content - string

def one(request):
    return render(request, 'first/one.html')
    
def two(request):
    return render(request, 'first/two.html')
    
def three(request):
    return render(request, 'first/three.html')
    