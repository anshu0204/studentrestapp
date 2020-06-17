from rest_framework import serializers
from converter.models import StudentDetails, CSVFile

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ["rollNo","name","marks_subject1","marks_subject2","marks_subject3"]

class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = '__all__'

    