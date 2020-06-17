from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from converter.models import StudentDetails, CSVFile
from converter.serializers import StudentDetailsSerializer, CSVFileSerializer
import os
import pandas as pd
import json

@api_view(["GET","PUT"])
def details_list(request):
    ob = CSVFile.objects.all()
    fileobj = CSVFileSerializer(ob[0])
    df= pd.read_csv(fileobj.data['CSVFile'])
    
    if request.method == "GET":
        jsonstring = json.loads(df.to_json(orient='records'))
        return Response(jsonstring)

    elif request.method == "PUT" :
        serializer = StudentDetailsSerializer(data = request.data)
        if serializer.is_valid():
            temp = pd.DataFrame(request.data,index=[0])
            if int(temp['rollNo']) in list(df['rollNo']):
                df = df.set_index('rollNo')
                df = df.drop(temp['rollNo'])
                df = df.reset_index()
            print(temp['rollNo'])
            df = df.append(temp)
            df.to_csv(fileobj.data['CSVFile'],index=False)
            return Response(status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET","DELETE"])
def detail_individual(request,pk):
    ob = CSVFile.objects.all()
    fileobj = CSVFileSerializer(ob[0])
    df= pd.read_csv(fileobj.data['CSVFile'])

    if request.method == "GET" :
        jsonstring = json.loads(df[df['rollNo']==int(pk)].to_json(orient="records"))
        return Response(jsonstring)

    elif request.method == "DELETE":
        df = df.set_index('rollNo')
        if int(pk) in df.index:
            df=df.drop(int(pk))
            df.to_csv(fileobj.data['CSVFile'])
            print("DONE")
            return Response(status = status.HTTP_200_OK) 
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def addfile(request):
    serializer = CSVFileSerializer(data = request.data)
    if serializer.is_valid():
        oldFiles = CSVFile.objects.all()
        serializer2 = CSVFileSerializer(oldFiles[0])
        if os.path.isfile(serializer2.data['CSVFile']):     #check if file exists
            os.remove(serializer2.data['CSVFile'])          #remove file
        oldFiles.delete()                                   #remove previous file entries in file database
        serializer.save()                                   #add the new file to database
        return Response(status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)
