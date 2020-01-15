from celery import shared_task
from .models import Subscriber, Recipe, Story
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime, timedelta
from django.template.loader import render_to_string

@shared_task
def sen_mail_to_subscribers():
    subscribers = list(Subscriber.objects.values_list('email', flat=True))

    now = datetime.now()
    yesterday = datetime.now() - timedelta(days=1)
    recipes = Recipe.objects.filter(created_at__range=[yesterday, now]).order_by('-view_count')[:3]
    stories = Story.objects.filter(created_at__range=[yesterday, now]).order_by('-view_count')[:3]
    print(recipes)
    context = {
        'site_address': settings.SITE_ADDRESS,
        'recipes': recipes,
        'stories':stories
    }

    email_template = render_to_string('stories/email-subscribers.html', context)
    html_content = email_template
    msg = EmailMultiAlternatives(subject='Recent updates on our website', body=email_template, 
    from_email=settings.EMAIL_HOST_USER, to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    