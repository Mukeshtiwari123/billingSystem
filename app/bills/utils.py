# app/utils.py
import tempfile
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

def render_to_pdf(template_src, context_dict={}):
    html_string = render_to_string(template_src, context_dict)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating HTTP response
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="document.pdf"'
    return response
