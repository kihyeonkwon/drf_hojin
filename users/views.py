from django.shortcuts import render
from rest_framework.views import APIView

from users.models import MyUser
from users.serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.



# 회원가입을 위한 class형 뷰 작성할 예정

class UserView(APIView):
    def get(self, request):
        # get user info
        print(request.user)
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return Response({'message': '로그인이 필요합니다.'})


    def post(self, request):
        # 1. request data를 받는다

        # 2. 받은 데이터를 가지고 user를 생성한다
        # 3. 생성한 user를 serializer를 통해 json으로 변환한다
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        # 4. json으로 변환한 데이터를 response에 담아서 보낸다
            return Response(serializer.data)
        
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)

