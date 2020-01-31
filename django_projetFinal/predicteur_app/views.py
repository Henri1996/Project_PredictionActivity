from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

#from .models import House
#from .serializers import HouseSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):
    ## une vue
    return HttpResponse('Voici mon API 😊')

def petittest(request):
    return HttpResponse('petit test',status=200)


def predict_activity(data):
    from sklearn.externals import joblib
    colonnes = ['Gender_m', 'Gender_f', 'Age', 'Height', 'Skin', 'Sport', 'ACC_chest_0',
       'ACC_chest_1', 'ACC_chest_2', 'ACC_wrist_0', 'ACC_wrist_1',
       'ACC_wrist_2', 'BVP', 'ECG', 'Resp', 'Labels']
    data = [[data[colonne] for colonne in colonnes ]]
    path_to_model   = "./random_forest2.sav"
    model           = joblib.load(path_to_model)
    activity        = model.predict(data)
    return activity

@csrf_exempt
def predict(request):
    
    if request.method == 'GET':
        return JsonResponse({'error':'method not allowed!!'}, status=400)

    elif request.method == 'POST':
        print("its good")
        data        = JSONParser().parse(request)
        data["Activity"] = int(predict_activity(data))
        
        return     JsonResponse(data, status=200)
