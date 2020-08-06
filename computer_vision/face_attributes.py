import asyncio
import io
import glob
import os
import sys
import time
import uuid
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType


# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
KEY = os.environ['FACE_SUBSCRIPTION_KEY']

# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = os.environ['FACE_ENDPOINT']

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


# Detect a face in an image that contains a single face, return attributes for age, gender and emotion
face_file_path = './Picknick.jpg'
detected_faces = face_client.face.detect_with_stream(open(face_file_path, 'rb'), return_face_attributes=['age','gender','emotion'])

if not detected_faces:
    raise Exception('No face detected from image {}'.format(face_file_path))


# For each face returned print attributes
for face in detected_faces:
    print (face.face_attributes)
