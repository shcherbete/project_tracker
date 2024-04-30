from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .models import BugReport, FeatureRequest


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = (f"<h1>Система контроля качества</h1>"
                f'<p><a href="{bug_list_url}">Список всех багов</a></p>'
                f'<p><br /><a href="{feature_list_url}">Запросы на улучшение</a></p>')
        return HttpResponse(html)

# def index(request):
#     bug_list_url = reverse('quality_control:bug_list')
#     feature_list_url = reverse('quality_control:feature_list')
#     html = (f"<h1>Система контроля качества</h1>"
#             f'<p><a href="{bug_list_url}"><p>Список всех багов</a></p>'
#             f'<p><br /><a href="{feature_list_url}">Запросы на улучшение</a></p>')
#     return HttpResponse(html)
def html_str(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"""
                <a href='{bug_list_url}'>Список всех багов</a>
                <a href='{feature_list_url}'>Запросы на улучшение</a>
                """)
    return html


# def bug_list(request):
#     return HttpResponse(f"<h1>Список отчетов об ошибках</h1>")

# def feature_list(request):
#     return HttpResponse(f"<h1>Список запросов на улучшение</h1>")

# def bug_detail(request, bug_id):
#     return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")

# def feature_detail(request, feature_id):
#     return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")

# Create your views here.
def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Bugs list</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a>, Status: {bug.status}</li>'
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = (f'<h1>{bug.title}</h1><p>{bug.description}</p>'
                         f'Статус: {bug.status} <br/>Приоритет: {bug.priority}')
        response_html += f'<p>Проект: {bug.project.name}</p>'
        response_html += f'<p>Задача: {bug.task.name}</p>'
        response_html += '</ul>'
        return HttpResponse(response_html)

# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     response_html = (f'<h1>{bug.title}</h1><p>{bug.description}</p>'
#                      f'Статус: {bug.status} <br/>Приоритет: {bug.priority}')
#     response_html += f'<p>Проект <a href="{bug.project.id}/">{bug.project.name}</a></p>'
#     response_html += f'<p>Задача <a href="{bug.task.id}/">{bug.task.name}</a></p>'
#     response_html += '</ul>'
#     return HttpResponse(response_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Feature list</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a>, Status: {feature.status}</li>'
    features_html += "</ul>"
    return HttpResponse(features_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = (f'<h1>{feature.title}</h1><p>{feature.description}</p>'
                         f'Статус: {feature.status} <br/>Приоритет: {feature.priority}')
        response_html += f'<p>Проект: {feature.project.name}</p>'
        response_html += f'<p>Задача: {feature.task.name}</p>'
        response_html += '</ul>'
        return HttpResponse(response_html)