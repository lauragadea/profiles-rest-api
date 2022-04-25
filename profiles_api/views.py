from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

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


    def post(self, request):
        """Create a hello message with our name"""
        # we retrieve the serializer and pass in the data that was sent in the request
        serializer = self.serializer_class(data=request.data)

        # in this case, it checks the name max length is 10
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    #in pk we shoud the id of the object that we are updating. Remplace the object with the one that is being passed
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    # updates an object with only the fields provided in the request
    def patch(self, request, pk=None):
        """Hadle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
