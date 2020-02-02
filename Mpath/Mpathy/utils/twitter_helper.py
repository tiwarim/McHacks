import twitter
from rest_framework import serializers


api = twitter.Api(consumer_key='ERrmPv9BYVFMSpS4aKgjGr9LQ',
                  consumer_secret='fqx1i8dhnzn7En80EKnp6X6rqyUJgDPL31JSpED1WZ07IWvbXp',
                  access_token_key='1220534378960506881-3pVl6qJ86954vdZxmrK1rzBygJl13K',
                  access_token_secret='qcnXNeonbD6DqOxM56LSZsDryxrRgOYNRaP4xoI1fSi6A')

def get_tweets():
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """
    return api.GetUserTimeline(screen_name='twitter_screen_name', exclude_replies=True, include_rts=False)  # includes entities


def get_users(pattern):

    result=api.GetUser(screen_name=str(pattern))
    return result.AsJsonString()

# class TwitterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = twitter.User
#         fields = '__all__'
