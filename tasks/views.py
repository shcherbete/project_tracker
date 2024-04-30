from django.http import HttpResponse
from django.urls import reverse
from quality_control.views import html_str

def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_url = reverse('tasks:quality_control')
    html = (f"<h1>Страница приложения tasks</h1>"
            f"<a href='{another_page_url}'>Перейти на другую страницу\n</a>"
            f"<a href = '{quality_control_url}'>Перейти на страницу контроля качества")
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")

def quality_control(request):
    return HttpResponse(html_str(request))
# Create your views here.
