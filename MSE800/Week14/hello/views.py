from django.http import HttpResponse

def hello(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello Django</title>
        <style>
            html {
                background: cyan;
            }

            p {
                color: green;
                font-size: 30px;
            }
        </style>
    </head>
    <body>
        <p>Hello Django</p>
    </body>
    </html>
    """)