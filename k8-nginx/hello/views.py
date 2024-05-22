import socket
from django.http import HttpResponse
import requests


def hello_world(request):
    # Get the hostname
    hostname = socket.gethostname()

    # Get the IP address
    ip_address = socket.gethostbyname(hostname)

    # Log the hostname and IP address
    print(f"Hostname: {hostname}, IP Address: {ip_address}")

    # Return the response
    return HttpResponse(f"VERSION 2: Hello from {hostname} ({ip_address})")


def nginx_proxy_view(request):
    # The URL of the API endpoint you want to call
    api_url = "http://nginx"

    try:
        # Make the GET request to the Nginx server
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the response body as HTML
            return HttpResponse(response.content, status=200, content_type='text/html')
        else:
            # Handle different status codes as needed
            return HttpResponse(f"<h1>Error {response.status_code}</h1><p>Failed to fetch data from Nginx</p>", status=response.status_code, content_type='text/html')
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        return HttpResponse(f"<h1>Request Exception</h1><p>{str(e)}</p>", status=500, content_type='text/html')