from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # created list so that the api returns something
        an_apiview = [
        'Users HTTP methods as function (get, post, pastch, put, delete)',
        'is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]
        #the Response class converts a list or a dictionary to a json object
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
