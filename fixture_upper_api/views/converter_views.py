from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([AllowAny])
def JSON_fixture_converter(request):
    '''Converts JSON data to Django fixtures

    Method arguments:
      request -- The full HTTP request object
    '''
    try:
        model_name = request.data['model']
        input_data = request.data['JSON']
        converted_data = []
        for obj in input_data:
             converted_obj = {
                  'model': model_name,
                  'pk': obj.pop('id'),
                  'fields': obj
             }
             converted_data.append(converted_obj)
        
        return Response(converted_data)
    except KeyError as ex:
            return Response({'message': f"{ex.args[0]} is required"}, status=status.HTTP_400_BAD_REQUEST)

