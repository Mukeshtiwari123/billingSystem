# app/utils.py
import tempfile
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import os
import requests
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings


def render_to_pdf(template_src, context_dict={}):
    html_string = render_to_string(template_src, context_dict)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating HTTP response
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="document.pdf"'
    return response


def send_email_with_pdf_attachment(subject, message, from_email, recipient_list, pdf_url):
    # Fetch the PDF content from the URL
    response = requests.get(pdf_url)
    if response.status_code == 200:
        pdf_content = response.content
    else:
        raise Exception(f"Failed to fetch PDF from {pdf_url}. Status code: {response.status_code}")

    # Assuming the URL ends with the PDF file name or you can extract the filename in another manner
    file_name = os.path.basename(pdf_url)

    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach(file_name, pdf_content, 'application/pdf')  # MIME type for PDF is application/pdf

    # Send the email
    email.send()

# def send_email_to_client():
#     subject=""
#     message=""
#     from_email=""
#     recipient_list=
