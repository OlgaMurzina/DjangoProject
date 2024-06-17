from django.shortcuts import render


# Create your views here.
def index(request):
    themes = ['A', 'B', 'C', 'D', 'E', 'F']
    context = {'themes': [(i + 1, themes[i]) for i in range(len(themes))]}
    return render(request, 'first_quizz/index.html', context)
