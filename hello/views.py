from django.http import JsonResponse
import pickle

def home(request):
    x1 = request.GET['x1']
    x2 = request.GET['x2']
    emp_pkl3 = pickle.load(open("./cal3.pkl", "rb"))
    result = emp_pkl3.getTest(int(x1), int(x2))
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)
