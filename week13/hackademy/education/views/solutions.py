from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from education.models import Solution


def list(request):
    return render(request, 'solutions/list.html', {'solutions': Solution.objects.all()})


def detail(request, solution_id):
    solution = get_object_or_404(Solution, id=solution_id)
    return render(request, 'solutions/detail.html', {'solution': solution})


class SolutionCreateView(CreateView):
    model = Solution
    fields = ['date', 'task', 'url']
    template_name = 'solutions/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:solutions:detail', kwargs={'solution_id': self.object.id})