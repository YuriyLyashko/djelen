from django.shortcuts import render

# Create your views here.
def index(request):
    print('index')
    #goods = Good.objects.all()
    #login_form = Login()
    return render(request, 'index.html',)# {'goods': goods, 'login_form': login_form})