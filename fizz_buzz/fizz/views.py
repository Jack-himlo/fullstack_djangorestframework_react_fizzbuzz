from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class FizzBuzzView(APIView):
    def post(self, request):
        number = request.data.get("number")
        try:
            number =int(number)
        except(TypeError, ValueError):
            return Response({"error": "Invalid number"}, status =400) 
        
        if number < 1:
            return Response({"error": "Number must be a positive number."}, status=400)
        
        result = []
        for num in range(1,number + 1):
                if num % 3 == 0 and num % 5 == 0:
                    result.append(f"FizzBuzz")

                elif num % 5 == 0:
                    result.append(f"Buzz")

                elif num % 3 == 0:
                    result.append(f"Fizz")
                else:
                    result.append(f"{num}")
        return Response({"result": result}, status=200)
