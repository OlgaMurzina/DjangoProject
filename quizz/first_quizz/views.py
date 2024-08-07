from django.shortcuts import render, get_object_or_404
from .models import QuizTest, QuizQuestion, QuizCategory, Status
from django.http import Http404


# Create your views here.
def index(request):
    # отбор всех опубликованных категорий для отображения на главной странице
    themes = QuizCategory.published.all()
    # отображение категорий в блоке контекст в цикле
    context = {'themes': [(i + 1, themes[i]) for i in range(len(themes))]}

    return render(request, 'first_quizz/index.html', context)


def quiz_test(request, id):
    # запрос выбранной категории по ее id
    category = QuizCategory.published.get(id=id)
    print(category)
    # image = QuizCategory.published.get(id=id)
    try:
        # запрос всех тестов по выбранной категории
        tests = QuizTest.published.filter(category=category, status=Status.PUBLISHED)
        context = {'category': category,
                   'tests': [(i + 1, tests[i]) for i in range(len(tests))]}
        print(context)
        return render(request,
                      'first_quizz/test.html',
                      context)
    except Exception as e:
        raise Http404(f'{e}')


def quiz_question(request, id, qid):
    # запрос выбранной категории по ее id
    category = QuizCategory.published.get(id=id)
    print(category)
    # запрос выбранного теста по его id
    test = QuizTest.published.get(id=qid)
    print(test)
    # image = QuizCategory.published.get(id=id)
    try:
        # запрос всех вопросов из теста
        questions = QuizQuestion.published.filter(test=test, status=Status.PUBLISHED)
        context = {'category': category,
                   'test': test,
                   'questions': [(i + 1, questions[i]) for i in range(len(questions))]}
        print(context)
        return render(request,
                      'first_quizz/question.html',
                      context)
    except Exception as e:
        raise Http404(f'{e}')
