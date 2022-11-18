from rest_framework.views import APIView
from rest_framework.response import Response
class Get(APIView):
    def get(self, request):
        name = "Rekruto!"
        message = "Давай дружить!"
        return Response(f'Hello {name}{message}')
# Create your views here.
