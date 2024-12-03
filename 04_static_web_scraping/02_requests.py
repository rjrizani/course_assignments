import requests
import json

# Task 1: Get HTML Content
def fetch_html_content():
    """Fetch HTML content and save to a file."""

    url = "https://example.com"
    output_file = "example.html"

    # TODO: Use requests to fetch the URL (url)    
    # TODO: Save response string to a file (output_file)
    # TODO: Print a message indicating the file has been saved
    

# Task 2: Download an Image
def download_image():
    """Download an image and save it locally."""

    # image_url = "https://via.placeholder.com/150"
    image_url = "https://i.etsystatic.com/19635104/r/il/887285/2591051093/il_570xN.2591051093_f2sk.jpg"
    output_file = "image.png"
    subfolder = "images"

    # TODO: Use requests to download the image binary (image_url)    
    # You can change the image url to any image you like
    # TODO: Write the image binary to a file (output_file)
    # TODO: Locate the image file in a sub-folder
    # You can use PIL or any other library to process the image
    # TODO: Print a message indicating the file has been saved
    

# Task 3: Get Response from an API
def fetch_api_data():
    """Fetch data from an API and print the JSON response."""

    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    # TODO: Use requests to fetch data from the API (api_url)    
    # TODO: Print the JSON response
    # TODO: Validate the output is a JSON object or a dictionary
    

# Task 4: Handle Errors
def check_error_handling(url):
    """Check error handling for a failed request."""

    url = "https://httpstat.us/404"

    # TODO: Use requests to fetch the URL (url)
    # TODO: Handle HTTP error and print the error message
    # TODO: Handle all other exceptions (RequestException)

# Task 5: Get Your Public IP
def get_public_ip():
    """Fetch and print your public IP address."""

    api_url = "https://api.ipify.org?format=json"

    # TODO: Use requests to fetch your IP from the API (api_url)
    # TODO: Extract the IP address from the JSON response
    # TODO: Print your IP

# Task 6: Use Payload Data
def post_with_payload(api_url, payload):
    """Send a POST request with payload data and print the response."""

    api_url = "https://httpbin.org/post"
    payload = {"name": "Your Name", "age": 40}

    # TODO: Replace name value with your name in the payload
    # TODO: Use requests.post() to send payload (payload) to the API (api_url)
    # TODO: Print the JSON response from the POST request and print back your payload data

# Task 7: Save JSON Response to a File
def save_json_to_file():
    """Fetch data from an API and save the JSON response to a file."""

    api_url = "https://jsonplaceholder.typicode.com/posts"
    output_file = "posts.json"

    # TODO: Use requests.get() to fetch JSON data from the API (api_url)
    # TODO: Write the JSON response to a file (output_file)
    # TODO: Print a message indicating the file has been saved


if __name__ == "__main__":
    """Test your code"""
    fetch_html_content()
    # download_image()
    # fetch_api_data()
    # check_error_handling()
    # get_public_ip()
    # post_with_payload()
    # save_json_to_file()
    