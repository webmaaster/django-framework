from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
  myDict = {
    "countryName":"Bangladesh"
  }
  return render(request,'templatesApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
  myDict = {
    "name":"Ranjit", "id": 101, "sal":"$100k", "dept":"Software Engineering"
  }

  return render(request, 'templatesApp/employeeTemplate.html', context=myDict)