from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .serializer import StudentSerializer, RegistrationSerializer
from rest_framework.generics import CreateAPIView
import io

# Create your views here.
from api.models import Student
from api.models import Registration


@csrf_exempt
def getInfo(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        name = data.get('name')
        pass_ = data.get('password')
        try:
            stu = Registration.objects.get(name=name, password=pass_)
            foo = stu.__dict__
            del foo['_state']
            print(foo)
            return JsonResponse(foo)
        except:
            return JsonResponse({"msg": "Sorry wrong username or Password"})

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class saveInfo(CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
