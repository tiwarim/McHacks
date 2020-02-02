from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.views import APIView

from .models import User_Account, Supervisee

import logging
import urllib.request
import os

@csrf_exempt
def userSearch(request):
    try:
        url_status = urllib.request.urlopen(request.body.decode("utf-8") ).getcode()
        print(url_status)
    except:
        return HttpResponse(":( Url is Not Working")
    if (url_status == 200):
        return HttpResponse("Yey! URL is Working")
    return HttpResponse(":( Url is Not Working")

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn/npm
    run build`).
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def search_twitter(self, request, matching_pattern:str):
        query_result = User_Account.objects.filter(user_name=matching_pattern)
        context = {
            'query result': query_result
        }
        return render(request, 'frontend/public/index.html', context)

    def get(self, request, format=None):
            # content = {
            #     'user': str(request.user), #django.contrib.auth.user instance
            #     'auth': str(request.auth),
            # }
            print(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html'))
            try:
                with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                    return HttpResponse(f.read())
            except FileNotFoundError:
                logging.exception('Production build of app not found')
                return HttpResponse(
                    """
                    This URL is only used when you have built the production
                    version of the app. Visit http://localhost:3000/ instead, or
                    run `yarn run build` to test the production version.
                    """,
                    status=501,
                )