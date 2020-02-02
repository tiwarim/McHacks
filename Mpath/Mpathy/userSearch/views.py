from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.views import APIView

from .models import User_Account, Supervisee

from userSearch.models  import User_Account, Supervisee
from userSearch.serializers  import *
from rest_framework import generics
from utils.twitter_helper import get_users

import twitter
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

class UserListCreate(generics.ListCreateAPIView):
    queryset= User_Account.objects.all()
    serializer_class=UserSerializer

class ListMatchedTwitterID(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user=request.user
        content = {
            'user': str(user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        try:
            twitter_name = request.GET.get('twitter')
            if user is not None:
                login(request, user)
                query_set = Supervisee.objects.filter(user=user, screen_name=twitter_name)
                #print(query_set._meta.fields)
                if query_set:
                    ss = SuperviseeSerializer(query_set, many=True)
                    query_result = ss.data
                if not query_set:
                    query_result = get_users(twitter_name)

        except ObjectDoesNotExist:
            return HttpResponse(
                    status=501,
                )
        except KeyError as e:
            print(e)
            return HttpResponse("Key Error: {0} not found".format(e))


        if query_result:
            return Response(query_result)
        else:
            return Response({'detail': 'Not Found'})