import os
import io
import uuid
from PIL import Image
import base64  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
BASE_DIR = settings.BASE_DIR
from YoloApi import *

class DETECTION(APIView):
    def post(self, request):
        try:
            img=request.data['img']
            decode=base64.b64decode(img)
            img=Image.open(io.BytesIO(decode))
            filename="uploaded.jpg"
            pathofimage=os.path.join(BASE_DIR, "media", filename)
            img.save(pathofimage)
            name=os.path.basename(pathofimage)
            fname=uuid.uuid4()
            imageoutput = detectDC(pathofimage,name,fname)         
            return Response({
                "output_image":imageoutput,
            },status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            print(e)

        

