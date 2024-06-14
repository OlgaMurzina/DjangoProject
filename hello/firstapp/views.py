from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest
from datetime import datetime
from django.template.response import TemplateResponse


def index(request):
    return render(request, "firstapp/index.html")
    # data = {'header': 'Загрузка данных в шаблон',
    #         'message': 'Данные загружены в firstapp/index_app1.html'}
    # return render(request=request, template_name='firstapp/index_app1.html', context=data)
    # header = "Фильтры в шаблонах"
    # value_num = 5
    # value_date = datetime.now()
    # value_time = datetime.now()
    # value_upper = "это строка в верхнем регистре"
    # data = {"header": header,
    #         "value_num": value_num,
    #         "value_date": value_date,
    #         "value_time": value_time,
    #         "value_upper": value_upper}
    # return render(request, template_name="firstapp/index_app1.html", context=data)


def about(request):
    return render(request, "firstapp/about.html")


def contact(request):
    return render(request, "firstapp/contact.html")


def products(request, productid):
    output = f"<h2>Продукт № {productid}</h2>"
    return HttpResponse(output)


def users(request):
    id = request.GET.get('id', 'Not')
    name = request.GET.get('name', 'Not')
    output = f"<h2>Пользователь</h2><h3>id: {id} Имя: {name}</hЗ>"
    return HttpResponse(output)


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Heкoppeктныe данные")
    if age > 17:  # если возраст больше 17, то доступ разрешен
        return HttpResponse("Доступ разрешен")
    else:  # если нет, то возвращаем ошибку 403
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
