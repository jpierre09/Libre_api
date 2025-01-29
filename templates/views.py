from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Templates, Content
from .serializers import TemplateSerializer, ContentSerializer

# Listar y crear plantillas
class TemplateListCreateAPIView(APIView):
    def get(self, request):
        templates = Templates.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Obtener, actualizar parcialmente o completamente una plantilla específica
class TemplateDetailAPIView(APIView):
    def get(self, request, pk):
        template = get_object_or_404(Templates, pk=pk)
        serializer = TemplateSerializer(template)
        return Response(serializer.data)

    def patch(self, request, pk):
        template = get_object_or_404(Templates, pk=pk)
        serializer = TemplateSerializer(template, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ContentListCreateAPIView(APIView):
    def get(self, request, template_id):
        contents = Content.objects.filter(template_id=template_id)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def post(self, request, template_id):
        request.data["template"] = template_id  # Vincula el contenido a la plantilla
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ContentDetailAPIView(APIView):
    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def patch(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        serializer = ContentSerializer(content, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)