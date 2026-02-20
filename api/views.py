import time
from django.http import JsonResponse

# simple in-memory cache
cache = {}

def get_students(request):

    start_time = time.time()

    # check cache first
    if 'students' in cache:
        data = cache['students']
        source = "CACHE"
    else:
        time.sleep(1)  # simulate slow database
        
        data = [
            {"name": "Swagath", "age": 22, "course": "CSE"},
            {"name": "Rahul", "age": 23, "course": "ECE"},
            {"name": "Priya", "age": 21, "course": "IT"}
        ]
        
        cache['students'] = data  # store in cache
        source = "DATABASE"

    end_time = time.time()

    response_time = end_time - start_time

    return JsonResponse({
        "source": source,
        "response_time_seconds": response_time,
        "data": data
    })