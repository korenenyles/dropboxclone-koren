from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'landingpage.html')

def file_list(request):
        return render(request, 'filelist.html')

        


# error views for custom error pages 

def error_404(request, exception):
        return render(request,'404.html', status=404)

def error_500(request):
        return render(request,'500.html', status=500)


