from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from quality_control.views import html_str
from .models import Project, Task
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         projects_list_url = reverse('tasks:projects_list')
#         # another_page_url = reverse('tasks:another_page')
#         quality_control_url = reverse('tasks:quality_control')
#         html = (f"<h1>Страница приложения tasks</h1>"
#                     # f"<p><a href='{another_page_url}'>Перейти на другую страницу\n</a></p>"
#                     f"<p><a href = '{quality_control_url}'>Перейти на страницу контроля качества\n</a></p>"
#                     f"<p><a href='{projects_list_url}'>Список проектов</a></p>")
#         return HttpResponse(html)

# def index(request):
#     projects_list_url = reverse('tasks:projects_list')
#     another_page_url = reverse('tasks:another_page')
#     quality_control_url = reverse('tasks:quality_control')
#     html = (f"<h1>Страница приложения tasks</h1>"
#             f"<p><a href='{another_page_url}'>Перейти на другую страницу\n</a></p>"
#             f"<p><a href = '{quality_control_url}'>Перейти на страницу контроля качества\n</a></p>"
#             f"<p><a href='{projects_list_url}'>Список проектов</a></p>")
#     return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")


def quality_control(request):
    return HttpResponse(html_str(request))


# def projects_list(request):
#     projects = Project.objects.all()
#     projects_html = '<h1>Список проектов</h1><ul>'
#     for project in projects:
#         projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#     projects_html += "</ul>"
#     return HttpResponse(projects_html)


class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'


class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'


# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     tasks = project.tasks.all()
#     response_html = f'<h1>{project.name}</h1><p>{project.description}</p>'
#     response_html += '<h2>Задачи</h2><ul>'
#     for task in tasks:
#         response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
#     response_html += '</ul>'
#     return HttpResponse(response_html)
class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'

# def task_detail(request, project_id, task_id):
#     project = get_object_or_404(Project, id=project_id)
#     task = get_object_or_404(Task, id=task_id, project=project)
#     response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
#     return HttpResponse(response_html)