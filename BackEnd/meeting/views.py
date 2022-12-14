import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import MemberSerializer
from .models import RoomMember

from vacantes.models import AgendaEntrevista

# Create your views here.
class GetTokenView(APIView):

    permission_classes = [ IsAuthenticated ]

    def get(self, request, *args, **kwargs):

        appId = "9c01a7dc56604b15b8a428063b7a4148"
        appCertificate = "2f90641900454ead8cb8c81b9d421b77"
        uid = random.randint(1, 230)
        expirationTimeInSeconds = 3600
        currentTimeStamp = int(time.time()) 
        privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
        role = 1
        
        try:
            channelName = self.kwargs['room_id']

            token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
        except:
            return Response({'data':None, 'status':status.HTTP_400_BAD_REQUEST, 'exito':False, 'error_message': 'Debes proporcionar un nombre para la sala de reunión'})
        
        return Response({'data': {'token': token, 'uid': uid}, 'status':status.HTTP_200_OK, 'exito':True})

class MemberView(APIView):
    
    #permission_classes = [ IsAuthenticated ]
    serialiser_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        
        uid = self.kwargs['uid']
        room_id = self.kwargs['room_id']

        member = get_object_or_404(RoomMember, uid=uid, room_id=room_id)
        serializer = self.serialiser_class(member, many=False)

        return Response({'data':serializer.data, 'status':status.HTTP_200_OK, 'exito': True})

    def post(self, request, *args, **kwargs):
        
        serializer = self.serialiser_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'data': serializer.data, 'status':status.HTTP_200_OK, 'exito':True})
        return Response({'data':None, 'status':status.HTTP_400_BAD_REQUEST, 'exito':False, 'error_message': 'Debes proporcionar un nombre para la sala de reunión'})

    def delete(self, request, *args, **kwargs):
        
        uid = request.data['uid']
        room_id = request.data['room_name']
        
        member = get_object_or_404(RoomMember, uid=uid, room_id=room_id)

        member.delete()

        return Response({'data': 'El miembro a sido eliminado', 'status': status.HTTP_200_OK, 'exito': True})

class AccesoMiembroView(APIView):

    permission_classes = [ IsAuthenticated ]

    def get(self, request, *args, **kwargs):

        staff = self.kwargs['staff']
        usuario_id = self.kwargs['id_usuario']
        room_id = self.kwargs['room_id']

        print(staff, usuario_id, room_id)

        try:
            if staff == 1:
                channelName = AgendaEntrevista.objects.get(empresa=usuario_id, room_id=room_id)
            else:
                channelName = AgendaEntrevista.objects.get(candidato=usuario_id, room_id=room_id)

            return Response({'status': status.HTTP_200_OK, 'exito': True})    
        except:

            return Response({'status': status.HTTP_400_BAD_REQUEST, 'exito': False})

class RoomMembersView(APIView):

    permission_classes = [ IsAuthenticated ]
    serialiser_class = MemberSerializer

    def get(self, request, *args, **kwargs):

        room_name = self.kwargs['room_id']

        rooms = RoomMember.objects.filter(room_id=room_name)

        data = []

        for room in rooms:

            serializer = self.serialiser_class(room, many=False)

            data.append(serializer.data)

        return Response({'data': data, 'status': status.HTTP_200_OK, 'exito': True})
