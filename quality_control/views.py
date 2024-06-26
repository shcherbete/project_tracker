from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView
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



# def add_bug(request):
#     if request.method == 'POST':
#         form = BugReportForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:bug_list')
#     else:
#         form = BugReportForm()
#     return render(request, 'quality_control/add_bug.html', {'form': form})

# def add_feature(request):
#     if request.method == 'POST':
#         form = FeatureRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:feature_list')
#     else:
#         form = FeatureRequestForm()
#     return render(request, 'quality_control/add_feature.html', {'form': form})

class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/add_bug.html'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/add_feature.html'
    success_url = reverse_lazy('quality_control:feature_list')

# def update_bug(request, bug_id):
#     bug = get_object_or_404(BugReport, pk=bug_id)
#     if request.method == 'POST':
#         form = BugReportForm(request.POST, instance=bug)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:bug_detail', bug_id=bug.id)
#     else:
#         form = BugReportForm(instance=bug)
#     return render(request, 'quality_control/bug_update.html',
#                   {'form': form, 'bug': bug})

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')

# def update_feature(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, pk=feature_id)
#     if request.method == 'POST':
#         form = FeatureRequestForm(request.POST, instance=feature)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:feature_detail', feature_id=feature.id)
#     else:
#         form = FeatureRequestForm(instance=feature)
#     return render(request, 'quality_control/feature_update.html',
#                   {'form': form, 'feature': feature})

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')


# def delete_bug(request, bug_id):
#     bug = get_object_or_404(BugReport, pk=bug_id)
#     bug.delete()
#     return redirect('quality_control:bug_list')
#
# def delete_feature(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, pk=feature_id)
#     feature.delete()
#     return redirect('quality_control:feature_list')
#

class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')
    template_name = 'quality_control/bug_confirm_delete.html'

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')
    template_name = 'quality_control/feature_confirm_delete.html'