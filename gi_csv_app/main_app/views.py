import csv
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, UserDataSerializer
from .models import User


class CsvUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        
        # data = [
        #     {"name": "Jo", "age": 25, "email": "john@example.com"},  # Name < 3 characters
        #     {"name": "Alice", "age": 17, "email": "alice@example.com"},  # Age < 18
        #     {"name": "Mike", "age": 30, "email": "mike@example.net"},  # Email not ending with .com
        #     {"name": "John", "age": 25, "email": "john.doe@example.com"},  # Valid record
        #     {"name": "Sara", "age": 30, "email": "sara.smith@example.com"}  # Valid record
        # ]

        # with open('updated_records.csv', mode="w", newline="") as file:
        #     writer = csv.DictWriter(file, fieldnames=["name", "age", "email"])
        #     writer.writeheader()
        #     writer.writerows(data)

        if file_serializer.is_valid():
            valid_count = 0
            error_rec = []
            req_file = file_serializer.validated_data['csv_file']
            file = req_file.read().decode('utf-8').splitlines()
            csv_data = csv.DictReader(file)
            for data in csv_data:
                print(data)
                data = {key.lower(): value for key, value in data.items()}
                user_serializer = UserDataSerializer(data=data)
                if user_serializer.is_valid():
                    instance = user_serializer.save()
                    valid_count += 1
                else:
                    error_rec.append({"data": data, "error": user_serializer.errors})
            return Response({"success": f"{valid_count} records added", "error": error_rec}, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        User.objects.all().delete()
        return Response({"success": "All records deleted"}, status=status.HTTP_204_NO_CONTENT)