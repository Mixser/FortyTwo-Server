from django.utils.datetime_safe import datetime
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from base.models import ApplicationUser
from base.serializers import UserSerializer, ScoreSerializer


@api_view(['POST'])
@permission_classes((AllowAny, ))
def api_signin(request):
    data = request.DATA
    try:
        email = data['email']
        user = ApplicationUser.objects.get(email=email)
        password = data['password']

        if user.check_password(password):
            content = {"status": "ok", "token": user.get_token().key}
            user.last_login = datetime.now()
            user.save()
            return Response(content, status=200)
        else:
            raise Exception
    except KeyError:
        content = {'errors': {"message": ['Wrong json format']}, 'status': 'error'}
    except ApplicationUser.DoesNotExist:
        content = {'errors': {"email": ["User does not exist or password is not correct"]}, 'status': 'error'}
    except Exception:
        content = {'errors': {"email": ["User does not exist or password is not correct"]}, 'status': 'error'}
    return Response(content, status=400)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def api_signout(request):
    try:
        request.auth.delete()
        result = {"status": "ok"}
        return Response(result, status=200)
    except KeyError:
        result = {'errors': {"message": ['Wrong json format']}, 'status': 'error'}
    except Token.DoesNotExist:
        result = {'errors': {"token": ['Wrong token']}, 'status': 'error'}
    return Response(result, status=400)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def api_create_user(request):
    serializer = UserSerializer(data=request.DATA)
    if serializer.is_valid():
        user = serializer.save(password=request.DATA['password'])

        result = {"status": "ok", "token": user.get_token().key}
        return Response(result, status=201)
    result = {"status": 'error', "errors": serializer.errors}
    return Response(result, status=400)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def api_save_score(request):

    data = request.DATA.copy()
    data['user'] = request.user.id
    serializer = ScoreSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        result = {'status': 'ok'}
        return Response(result, status=201)
    result = {'status': 'error', 'errors': serializer.errors}
    return Response(result, status=400)
