from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Category

class ListCategoriesView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        categories = Category.objects.filter(parent=None)

        result = []

        for category in categories:
            item = {
                'id': category.id,
                'name': category.name,
                'gender': category.get_gender_display(),
                'sub_categories': [],
            }

            for sub_category in category.children.all():
                sub_item = {
                    'id': sub_category.id,
                    'name': sub_category.name,
                    'gender': sub_category.get_gender_display(),
                    'sub_categories': [],
                }
                item['sub_categories'].append(sub_item)

            result.append(item)

        return Response({'categories': result}, status=status.HTTP_200_OK)
