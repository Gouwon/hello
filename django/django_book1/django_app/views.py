import logging
from functools import wraps
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import Context, Template

from .models import Question, Choice


# Create your views here.
def route(fn):
    """
        fn, view function, should return tuple if render a template.
        if want to use request, then use route.req from view function.
    """
    route.req = None
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        route.req = request = args[0]
        result = fn(**kwargs)
        return render(request, *result) \
            if str(type(result)) == "<class 'tuple'>" else result
    return decorated_function

def find_templates(template_name):
    """
    return template location with appname.
    this will be used when django finds the template with given template name.
    when use this function, must add a app for specific template app to project
    setting.py which is to be found in 'TEMPLATES' list 'DIRS' order.
    the template directory is the django BASE_DIR/templates.
    """
    directory = globals().get('__package__', None)
    return directory + '/' + template_name

@route
def index():
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return find_templates('index.html'), context
    

@route
def detail(question_id):
    question = get_object_or_404(Question, pk=question_id)
    return find_templates('detail.html'), {'question': question}

@route
def vote(question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=route.req.POST['choice'])
    except (HttpResponseRedirect, Choice.DoesNotExist) as err:
        return find_templates('detail.html'), {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('django_app:results', \
            args=(question.id,)))

@route
def results(question_id):
    question = get_object_or_404(Question, pk=question_id)
    return find_templates('results.html'), {'question': question}

# settings.py에서 설정한 로거
logger = logging.getLogger('mylogger')

