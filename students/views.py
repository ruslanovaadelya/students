from django.shortcuts import render, redirect
from .forms import CommentsFormat
from .models import Students
from django.views.generic.base import View


class PostView(View):
    def get(self, request):
        post = Students.objects.all()
        return render(request, 'students.html', {'post_list': post})


class PostDetail(View):
    def get(self, request, pk):
        post = Students.objects.get(id=pk)
        return render(request, 'comment.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsFormat(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect('/')










