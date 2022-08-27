import base64
import os
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Guest
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'pk'
    paginate_by = 8


class PostDetail(DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        current_user = self.request.user
        if not (current_user.is_authenticated and current_user.is_superuser):
            return redirect('/diary/')
        else:
            response = super(PostCreate, self).form_valid(form)
            return response


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']

    template_name = 'diary/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def delete_post(request, pk):
    post = Post.objects.filter(pk=pk)
    if post:
        post.delete()
        return redirect('/diary/')


@login_required
def guest_book(request):
    guest_list = Guest.objects.all().order_by('-created_at')
    paginator = Paginator(guest_list, 7)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diary/guest_book.html', {'page_obj': page_obj})


def guest_write(request):
    guest = Guest()
    guest.author = request.POST['author']
    guest.content = request.POST['content']
    guest.sticker = request.POST['sticker']
    guest.save()

    return HttpResponseRedirect('guest_book')


def guest_delete(request, pk):
    guest = Guest.objects.filter(pk=pk)
    if guest:
        guest.delete()
    return redirect('/diary/guest_book')


@login_required
def avatar(request):
    return render(request, 'diary/avatar.html')


@csrf_exempt
def avatar_profile(request):
    data = request.POST.__getitem__('data')

    data = data[22:]

    path = str(os.path.join('single_pages' + settings.STATIC_URL, 'single_pages/css/images/'))
    filename = 'profile.png'

    image = open(path + filename, "wb")
    image.write(base64.b64decode(data))
    image.close()

    return HttpResponseRedirect('avatar')