from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm

from .models import BugReport, FeatureRequest


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


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
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = "bug_id"
    template_name = 'quality_control/bug_detail.html'


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
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    #
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     feature = self.object
    #     response_html = (f'<h1>{feature.title}</h1><p>{feature.description}</p>'
    #                      f'Статус: {feature.status} <br/>Приоритет: {feature.priority}')
    #     response_html += f'<p>Проект: {feature.project.name}</p>'
    #     response_html += f'<p>Задача: {feature.task.name}</p>'
    #     response_html += '</ul>'
    #     return HttpResponse(response_html)


def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/add_bug.html', {'form': form})

def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/add_feature.html', {'form': form})