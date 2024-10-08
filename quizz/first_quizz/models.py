from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Status(models.TextChoices):
    """
    Класс статусов - метериал еще черновик или готов к опубликованию
    """
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'


# конкретно-прикладные менеджеры для классов модели данных
# отбирают данные по статусу ОПУБЛИКОВАН
class PublishedManager(models.Manager):
    """
    Конкретно-прикладной менеджер
    """

    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Status.PUBLISHED)


class QuizCategory(models.Model):
    """
    Класс категорий - крупные темы для объединения тестов по схожей тематике
    """
    # название категории
    title = models.CharField(max_length=100)
    # описание категории
    detail = models.TextField()
    # рисунок для иллюстрации
    image = models.ImageField(upload_to='images/cat_imgs/')
    # автор категории (related_name - имя обратной связи, от User к category)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='first_quizz_quizcategory',
                               default=1, )
    # дата-время публикации
    publish = models.DateTimeField(default=timezone.now)
    # дата-время создания
    created = models.DateTimeField(auto_now_add=True)
    # дата-время обновления
    updated = models.DateTimeField(auto_now=True)
    # статус категории - черновик или опубликована
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # подключение менеджеров
    # менеджер, применяемый по умолчанию
    objects = models.Manager()
    # конкретно-прикладной менеджер
    published = PublishedManager()

    class Meta:
        """
        Дополнительные внутренние настройки класса
        """
        # множественное число
        verbose_name_plural = 'Категории'
        # порядок сортировки по дате публикации?
        ordering = ['-publish']

    def __str__(self):
        return self.title


class QuizTest(models.Model):
    """
    Класс Тест - конкретный тест в обозначенной категории.
    """
    # категория, к которой относится тест - связь многие к одному с классом Категории
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    # название теста
    title = models.CharField(max_length=100)
    # автор теста (related_name - имя обратной связи, от User к test)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='first_quizz_quiztest',
                               default=1, )
    # описание теста
    detail = models.TextField()
    # рисунок для иллюстрации теста
    image = models.ImageField(upload_to='images/test_imgs/')
    # выдача вопросов не по порядку номеров (по умолчанию отключена)
    random_issue = models.BooleanField(default=False)
    # дата-время публикации теста
    publish = models.DateTimeField(default=timezone.now)
    # дата-время создания теста
    created = models.DateTimeField(auto_now_add=True)
    # дата-время обновления теста
    updated = models.DateTimeField(auto_now=True)
    # статус теста - черновик или опубликован
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # подключение менеджеров
    # менеджер, применяемый по умолчанию
    objects = models.Manager()
    # конкретно-прикладной менеджер
    published = PublishedManager()
    # менеджер тегов
    tags = TaggableManager()

    class Meta:
        """
        Дополнительные внутренние настройки класса
        """
        # множественное число
        verbose_name_plural = 'Тесты'
        # порядок сортировки по дате публикации
        ordering = ['-publish']

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    """
    Класс вопросов
    """
    category = models.ForeignKey(QuizCategory,
                                 on_delete=models.CASCADE,
                                 default=1)
    # тест/тесты, к которым относится вопрос (один вопрос может относиться к одному или нескольким тестам и наоборот)
    test = models.ManyToManyField(QuizTest)
    # автор вопроса (related_name - имя обратной связи, от User к question)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='first_quizz_quizquestion',
                               default=1, )
    # текст вопроса
    question = models.TextField()
    # варианты ответа
    opt_1 = models.CharField(max_length=200)
    opt_2 = models.CharField(max_length=200)
    opt_3 = models.CharField(max_length=200)
    opt_4 = models.CharField(max_length=200)
    # уровень вопроса - начальный, средний, сложный
    level = models.CharField(max_length=100)
    # временной лимит для ответа на вопрос, по умолчанию 30 с
    time_limit = models.IntegerField(default=30)
    # правильный ответ/ответы
    right_opt = models.CharField(max_length=100)
    # дата-время публикации
    publish = models.DateTimeField(default=timezone.now)
    # дата-время создания
    created = models.DateTimeField(auto_now_add=True)
    # дата-время обновления
    updated = models.DateTimeField(auto_now=True)
    # статус вопроса - черновик или опубликован
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # подключение менеджеров
    # менеджер, применяемый по умолчанию
    objects = models.Manager()
    # конкретно-прикладной менеджер
    published = PublishedManager()
    # менеджер тегов
    tags = TaggableManager()

    class Meta:
        """
        Дополнительные внутренние настройки класса
        """
        # множественное число
        verbose_name_plural = 'Вопросы'
        # порядок сортировки по номерам вопросов
        ordering = ['id']

    def __str__(self):
        return self.question
