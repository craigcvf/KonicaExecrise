#classLogin

import jwt,json
import classsUser
from classsUser import User
from rest_framework import views
from rest_framework.response import Response
from models import User

class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400")

        username = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid email/password"}, status="400")
        if user:
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
              json.dumps(jwt_token),
              status=200,
              content_type="application/json"
            )
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )