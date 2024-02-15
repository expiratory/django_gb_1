from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Это главная страница сайта, созданного с использованием Django.</p>
    """

    logger.info('Посещение главной страницы')

    return HttpResponse(html)


def about(request):
    html = """
    <h1>Об авторе</h1>
    <p>Привет! Меня зовут Александр. Я начинающий веб-разработчик и создал этот сайт, чтобы изучить Django.</p>
    <p>В будущем здесь вы найдете немного информации обо мне и о моих навыках в программировании.</p>
    """

    logger.info('Посещение страницы "О себе"')

    return HttpResponse(html)
