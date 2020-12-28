from django.http import HttpResponse
from utils.common import load_env

env = load_env()


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
