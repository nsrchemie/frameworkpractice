from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
import os

# def upload_to(instance, filename):
#     now = timezone_now()
#     filename_base, filename_ext = os.path.splitext(filename)
#     return 'blog/%s%s' % ( now.strftime("%Y/%m/%Y%m%d%H%M%S"),
#         filename_ext.lower(),)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone_now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture = models.ImageField(upload_to="%Y/%m/%d", blank=True, null=True)
    location = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#for forms
# from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post

# for views
# from django.shortcuts import redirect
# from django.shortcuts import render
# from forms import Post

# def add_post(request):
#     if request.method == "POST":
#         form = PostForm( data = request.POST,
#             files.request.FILES,
#             )
#         if form.is_valid():
#             blog = form.save()
#             return redirect("add_post_done")
#     else:
#         form = PostForm()
#     return render(request, "blog/templates/blog/change_post.html", {'form' : form})


# #template blog/templates/blog/base.html
# {% block doctype %}<!DOCTYPE html>{% endblock %}
# {% load i18n %}
# <html lang="{{ LANGUAGE_CODE }}"> 
# <head>
#     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <title>{% block title %}{% endblock %}{% trans "My Website" %}</title>
#     <link rel="icon" href="{{ STATIC_URL }}site/img/favicon.ico" type="image/png">
    
#     {% block meta_tags %}{% endblock %} 
    
#     {% block stylesheet %}
#         <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
#         <link href="{{ STATIC_URL }}site/css/style.css" rel="stylesheet" media="screen" type="text/css" />
#     {% endblock %}
    
#     <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
#     <script src="http://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
#     <script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>

#     {% block js %}{% endblock %}
#     {% block extrahead %}{% endblock %}
# </head>
# <body class="{% block bodyclass %}{% endblock %}">
#     {% block page %}
#         <div class="wrapper">
#             <div id="header" class="clearfix">
#                 <h1 class="text-center">{% trans "My Website" %}</h1>
#                 {% block header_navigation %}
#                 {% endblock %}
#                 {% block language_chooser %}
#                 {% endblock %}
#             </div>
#             {% block container %}
#                 <div class="container">
#                     <div class="row">
#                         <div id="content" class="col-md-12">
#                             {% block content %}
#                             {% endblock %}
#                         </div>
#                     </div>
#                 </div>
#             {% endblock %}
#             <div id="footer" class="clearfix">
#                 {% block footer_navigation %}
#                 {% endblock %}
#             </div>
#         </div>
#     {% endblock %}
#     <script type="text/javascript">
#         $(function() {
#             $("a[href^='http://']").attr("target", "_blank");           
#         });
#     </script>
#     {% block extrabody %}{% endblock %}    
# </body>
# </html>

#     #template blog/templates/blog/change_post.html
#     {% extends "base.html" %}
# {% load i18n %}

# {% block content %}
#     <form method="post" action="" enctype="multipart/form-data">
#     {% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">{% trans "Save" %}</button>
#     </form>
# {% endblock %}