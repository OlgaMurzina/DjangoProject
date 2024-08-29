from django.shortcuts import render, get_object_or_404
from .models import QuizTest, QuizQuestion, QuizCategory, Status
from django.http import Http404
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def index(request):
    """
    Главная страница с отображением доступных категорий квизов
    :param request: запрос с фронта
    :return: главная страница с категориями
    """
    # отбор всех опубликованных категорий для отображения на главной странице
    themes = QuizCategory.published.all()
    # отображение категорий в блоке контекст в цикле
    context = {'themes': sorted([(x.id, x.title, x.image) for x in themes])}
    print(themes[0].image)
    return render(request, 'first_quizz/index.html', context)


def quiz_test(request, id, tag_slug=None):
    """
    Все тесты из выбранной категории
    :param request: запрос с фронта
    :param id: id выбранной категории
    :return: страница с тестами из выбранной категории
    """
    # запрос выбранной категории по ее id
    category = QuizCategory.published.get(id=id)
    print(category.image)
    # image = QuizCategory.published.get(id=id)

    try:
        # запрос всех тестов по выбранной категории
        tests = QuizTest.published.filter(category=id, status=Status.PUBLISHED)
        questions = QuizQuestion.published.filter(category=id)
        print(questions)
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            tests = tests.filter(tags__in=[tag])
        context = {'category': (category.title, category.image),
                   'tests': sorted([(x.id, x) for x in tests]),
                   'questions': sorted([(x.id, x) for x in questions]),
                   'tag': tag}

        print(context)
        return render(request,
                      'first_quizz/test.html',
                      context)
    except Exception as e:
        raise Http404(f'{e}')


def quiz_question(request, id, qid, tag_slug=None):
    """
    Все вопросы из выбранного теста
    :param request: запрос с фронта
    :param id: id категории
    :param qid: id теста
    :return: страничка с выбранным тестом
    """
    # запрос выбранного теста по категории и его id
    test = QuizTest.published.get(category=id, id=qid)
    print(test)
    # image = QuizCategory.published.get(id=id)
    try:
        # запрос всех вопросов из теста
        questions = QuizQuestion.published.filter(test=test, status=Status.PUBLISHED)
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            questions = questions.filter(tags__in=[tag])
        context = {'category': QuizCategory.published.get(id=id),
                   'test': test,
                   'questions': sorted([(x.id, x) for x in questions]),
                   'tag': tag}
        print(context)
        return render(request,
                      'first_quizz/question.html',
                      context)
    except Exception as e:
        raise Http404(f'{e}')
