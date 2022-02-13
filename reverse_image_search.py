def urls_by_image(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    results = []
    
    if annotations.pages_with_matching_images:

        for page in annotations.pages_with_matching_images:

            if page.full_matching_images:
                results.append(['', '', -1])
                results[-1][0] = page.url
                
                success = False
                for image in page.full_matching_images:
                    try:
                        urllib.request.urlretrieve(image.url, "match.jpg")
                    except:
                        continue
                    results[-1][1] = image.url
                    success = True
                    break
                    
                if not success:
                    del(results[-1])

                if 'ebay' in page.url:
                    try:
                        results[-1][2] = get_ebay_price(url)
                    except:
                        pass
                
            if page.partial_matching_images:
                results.append(['', '', -1])
                results[-1][0] = page.url

                success = False
                for image in page.partial_matching_images:
                    try:
                        urllib.request.urlretrieve(image.url, "match.jpg")
                    except:
                        continue
                    results[-1][1] = image.url
                    success = True
                    break
                    
                if not success:
                    del(results[-1])
                    
                if 'ebay' in page.url:
                    try:
                        results[-1][2] = get_ebay_price(url)
                    except:
                        pass

    return results
