from django.shortcuts import render

# Create your views here.
def hello(request):
    # users = User.objects.all()
    context = {
        'hello': "hello",
    }
    return render(request, 'pages/hello.html', context)
