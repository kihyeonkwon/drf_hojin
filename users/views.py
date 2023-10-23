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


class UserDetailView(APIView):
    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)



class FollowView(APIView):
    def get(self, request, user_id):
        user = MyUser.objects.get(id=user_id)
        # 유저의 팔로워들
        follower_serializer = UserSerializer(user.followers, many=True)
        # 유저가 팔로잉하고 있는 사람들
        following_serializer = UserSerializer(user.following, many=True)
        data = {
            'followers': follower_serializer.data,
            'following': following_serializer.data,
        }
        return Response(data)
    
    def post(self, request, user_id):
        if request.user.is_anonymous:
            return Response({'message': '로그인이 필요합니다.'}, status=401)
        me = request.user
        you = MyUser.objects.get(id=user_id)

        if you.followers.filter(id=me.id).exists():
            me.following.remove(you)
            me.save()
            return Response({'message': '언팔로우 완료!'})
        else:
            me.following.add(you)
            me.save()
            return Response({'message': '팔로우 완료!'})
    
    def delete(self, request, user_id):
        if request.user.is_anonymous:
            return Response({'message': '로그인이 필요합니다.'}, status=401)
        me = request.user
        you = MyUser.objects.get(id=user_id)
        me.following.remove(you)
        me.save()

        return Response({'message': '언팔로우 완료!'})