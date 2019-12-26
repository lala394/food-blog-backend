from django.shortcuts import render
from django.views.generic.edit import FormMixin, UpdateView
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from stories.models import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy

# Create your views here.

# def about(request):
#     context = {}
#     if request.method == 'GET':
#         context['content'] = AboutPage.objects.last()

#     return render(request, 'stories/about.html', context)

class AboutView(TemplateView):
    template_name = 'stories/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = AboutPage.objects.last()
        return context

# def contact(request):
#     form = ContactForm()

#     context = {
#         'form':form
#     }

#     if request.method == "POST":
#         print(request.POST)
#         f = ContactForm(data=request.POST) #word data is not mandatory
#         if f.is_valid():
#             f.save()
#             context['message'] = 'Your message was successfully sent'
#         else:
#             context['form'] = f
            
#     # context = {
#     #     'form':form
#     # }
#     # return render(request, 'contact_test.html', context)
#     return render(request, 'stories/contact.html', context)


class ContactView(CreateView):
    model=Contact
    template_name = 'stories/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('stories:contact')  #this stories represents namespace from urls.py

# def create_story(request):
#     return render(request, 'stories/create_story.html')

class CreateStoryView(CreateView):
    model = Story
    form_class = StoryForm
    template_name = 'stories/create_story.html'

    def form_valid(self, form):
        story = form.save(commit=False)
        story.owner = self.request.user
        story.save()
        self.success_url = reverse_lazy('stories:user-profile', kwargs={'pk': self.request.user.id})
        return super().form_valid(form)

def home(request):
    return render(request, 'stories/index.html')

# def recipes(request):
#     page = request.GET.get('page', 1)
#     recipes = Recipe.objects.all()
#     p = Paginator(recipes, 2)

#     if not page.isdigit():
#         page = 1
#     elif int(page) > p.num_pages:

#         page = p.num_pages

#     recipe_list = p.page(page)
#     context= {
#         'recipes':recipe_list
#     }
#     return render(request, 'stories/recipes.html', context)

class RecipeView(ListView):
    model = Recipe
    template_name = 'stories/recipes.html'
    context_object_name = 'recipes'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        return context


# def single(request, pk):
#     recipe = Recipe.objects.get(id=pk)
#     context = {
#         'recipe_data' : recipe,
#     }
#     return render(request, 'stories/single.html', context)

class RecipeDetailView(FormMixin, DetailView):
    model = Recipe
    template_name = "stories/single.html"
    context_object_name = "recipe_data"
    form_class = CommentForm
    

    def post(self, request, *args, **kwargs):
        self.object =self.get_object()
        self.replied_comment = request.POST.get('reply_comment')
        form= self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.recipe = self.object
        if not self.replied_comment is None and self.replied_comment.isdigit():
            r_comment = Comment.objects.get(id=int(self.replied_comment))
            comment.reply_comment = r_comment
        comment.save()
        self.success_url = reverse_lazy('stories:single', kwargs = 
        {'pk': self.object.id })
        return super().form_valid(form)


# def stories(request):
#     return render(request, 'stories/stories.html')

class StoriesView(ListView):
    model = Story
    template_name = 'stories/stories.html'
    context_object_name = 'stories'
    paginate_by = 6


def user_profile(request):
    return render(request, 'stories/user_profile.html')

class UserProfileView(DetailView):
    model = User
    template_name = 'stories/user-profile.html'


class UserEditView(UpdateView):
    model = User
    template_name = 'stories/user-edit.html'
    form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('stories:user-profile', kwargs={'pk': self.object.pk})
