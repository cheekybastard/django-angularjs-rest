from models import Snippet
from django.contrib.auth.models import User
from serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    """
    list all snippets, or create a new snippet.
    """
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve, update or delete a snippet instance
    """
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class SnippetHighlight(generics.SingleObjectAPIView):
    model = Snippet
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)




















