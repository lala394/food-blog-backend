from django.urls import path, include
from .views import *


app_name = 'stories'

urlpatterns = [
    path('', home,name='home'),
    # path('about/', about,name='about'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(),name='contact'),
    # path('contact/', contact,name='contact'),
    path('create-story/', CreateStoryView.as_view(), name='create-story'),
    # path('recipes/', recipes,name='recipes'),
    path('recipes/', RecipeView.as_view(), name='recipes'),
    # path('recipes/stories/single/<int:pk>', single, name='single'),
    path('single/<int:pk>', RecipeDetailView.as_view(), name='single'),
    # path('stories/', stories,name='stories'),
    path('stories/', StoriesView.as_view(), name='stories'),
    path('user-profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('user-edit/<int:pk>/', UserEditView.as_view(), name='user-edit'), 
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),
    path('api/', include('stories.api.urls')),
]
