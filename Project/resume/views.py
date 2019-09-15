from django.shortcuts import render
# import pdfcrowd
import sys
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def resume_download(request):

    try:
        # create the API client instance
        # client = pdfcrowd.HtmlToPdfClient('vishnut', 'd7ae7949d35aa613b3638b5d8485d78a')

        # # run the conversion and write the result to a file
        # client.convertUrlToFile('https://stockmaintain.herokuapp.com/', 'vishnu_resume.pdf')
        file_path = os.path.join(settings.DATA_DIR, 'vishnu_resume.pdf')
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    except Exception as e:
        pass
    # except Error as why:
    #     # report the error
    #     sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    #     # handle the exception here or rethrow and handle it at a higher level
    #     raise
