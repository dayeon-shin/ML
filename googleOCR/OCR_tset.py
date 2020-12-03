# google-api-python-client
# google-cloud-vision
# google-cloud-speech

# https://console.developers.google.com/apis/api/vision.googleapis.com/overview?project=511619749144
# Cloud Vision API 사용해제 : https://console.cloud.google.com/apis/library/vision.googleapis.com?project=ai-service-test
# 프로젝트의 결제 사용 설정(결제계정등록):
# QR 코드 만들기 : http://chart.apis.google.com/chart?cht=qr&chs=350x350&chl={STR}



from google.cloud import vision
import io
import os

credential_path = "springsaturday-d6504b76ac76.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# from google.cloud import storage

# def implicit():
#     storage_client = storage.Client()
#     buckets = list(storage_client.list_buckets())
#     print(buckets)


def detect_text(IMG_PATH):
    client = vision.ImageAnnotatorClient()

    with io.open(IMG_PATH, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception('error : {}'.format(response.error.message))


def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception('error : {}'.format(response.error.message))

detect_text('img1.jpg')