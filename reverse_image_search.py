import urllib

from bs4 import BeautifulSoup
import urllib.request
import requests

from google.cloud import vision
import io


def urls_by_image(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    page_urls = []
    img_urls = []
    
    if annotations.pages_with_matching_images:

        for page in annotations.pages_with_matching_images:

            if page.full_matching_images:
                page_urls.append(page.url)
                
                success = False
                for image in page.full_matching_images:
                    try:
                        urllib.request.urlretrieve(image.url, "match.jpg")
                    except:
                        continue
                    img_urls.append(image.url)
                    success = True
                    break
                    
                if not success:
                    del[page_urls[-1]]

                    
                    partial_matching_images
                    
            if page.partial_matching_images:
                page_urls.append(page.url)

                success = False
                for image in page.partial_matching_images:
                    try:
                        urllib.request.urlretrieve(image.url, "match.jpg")
                    except:
                        continue
                    img_urls.append(image.url)
                    success = True
                    break
                    
                if not success:
                    del[page_urls[-1]]
    return (page_urls, img_urls)
