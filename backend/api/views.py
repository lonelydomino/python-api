import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    #request.body
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)