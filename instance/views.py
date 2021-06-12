from django.shortcuts import render
 
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
 
from instance.helpers.instance_helper import create_deploy_instance, get_instance_state
 
class CreateInstanceAPIView(APIView):
   def post(self, request):
       data = request.data
       print(data)
       instance = create_deploy_instance(data['instance_type'])
       return Response({"instance_id": instance})
 
class GetInstanceState(APIView):
   def get(self, request, instance_id):
       try:
           data = {}
           data['instance_id'] = instance_id
           state = get_instance_state(instance_id)
           data['code'] = state['Code']
           data['state'] = state['Name']
           return Response(data)
       except Exception as e:
           return Response({"msg": str(e)})