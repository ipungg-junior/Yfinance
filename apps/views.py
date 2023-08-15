from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

@method_decorator(cache_control(no_cache=True, must_revalidate=True), name='dispatch')
class Landing(View):

    def main(request):
        return HttpResponse(status=200)