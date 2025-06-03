from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def show_index(request):
    return render(request, 'index.html')

#def show_error_page(request, exception):
#	return render(request, 'error.html')

def handler400(request, exception, template_name="400.html"):
    response = render_to_response(template_name)
    response.status_code = 400
    return response

def handler403(request, exception, template_name="403.html"):
    response = render_to_response(template_name)
    response.status_code = 403
    return response

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
