class google_ocr:
    
    def image_crop(path):
        from PIL import Image
        im = Image.open(path)
        im=im.resize((2480,3500))
        crop_rectangle = (size)
        cropped_im = im.crop(crop_rectangle)
        cropped_im.save(path)
            
    #구글 라벨링 OCR 메서드입니다.
    def detect_labels(path):
        """Detects labels in the file."""
        import os
        from google.cloud import vision
        import io

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="your.json"
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations
    #     print(labels)
        result=[]
        logo_score=100
        for label in labels:
            result.append(label.description)
            if label.description=="Logo":
                logo_score=label.score*100
                print(logo_score)

        print(result)    
        if "Calligraphy" in result:
            with open("", "w") as f:
                f.write("캘리그래피 있어서 사인입니다.")

        elif "White" in result and "Black" in result:
             with open("", "w") as f:
                f.write("화이트 블랙으로 사인이아닙니다.(1)")

        elif "Black-and-white" in result:
             with open("", "w") as f:
                f.write("화이트 블랙으로 사인이아닙니다.(2)")

        elif logo_score < 70:
    #         print(logo_score)
             with open("", "w") as f:
                f.write("로고 정확도가 낮아서 사인입니다.")
        elif result==[]:
             with open("", "w") as f:
                f.write("라벨링이 아무것도 없으면 사인입니다.")
        else:
             with open("", "w") as f:
                f.write("로고 정확도가 높아서 사인이 아닙니다.")

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
    
      #구글  OCR 메서드입니다. 위에 구글 라벨링 OCR은 해당 메서드에서 호출됩니다.
    def google_OCR(input_file):
        import requests
        import win32api
        import base64
        import json
        import sys
        import config as cfg
       
        api_key = ''

        input_data = open(input_file).readlines()
        for line in input_data:
            print(line +"의 OCR을 수행합니다.")
            image_filename= line.lstrip().split(' ')[0]
            with open(image_filename, 'rb') as image_file:
                content_json_obj = {
                    'content': base64.b64encode(image_file.read()).decode('UTF-8')
                }

            feature_json_obj = []
            feature_json_obj.append({
                'type': 'TEXT_DETECTION',
                'maxResults': int(10),
            })

            sum_list = []

            sum_list.append({
                'features': feature_json_obj,
                'image': content_json_obj,
            })

        full_request = json.dumps({'requests': sum_list})
        response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key='+api_key, 
                                 data=full_request, 
                                 headers={'Content-Type': 'application/json'})

        with open('output.json', 'w', encoding='utf-8') as output_file:
            json.dump(response.text, output_file, ensure_ascii=True)

        json_response = response.json()

        if json_response['responses']==[{}]:
            with open("", "w") as f:
                f.write("오류로인한 사인입니다.")
        else:
            words = json_response['responses'][0]['textAnnotations'][0]['description']
            print("인식한 결과 :",words)

            if words!='(인)\n':
                #해당 프로세스는 (인) 만들어오는것이 아닌 다른것도 같이 들어온다.
                with open("", "w") as f:
                    f.write("인이 아니므로 사인입니다.")

            else:
                input_data=''.join(input_data)
                google_ocr.detect_labels(input_data)
   

        
        
if __name__ == "__main__":
    mooongs=google_ocr
    f = open("", 'r')
    line = f.readline()
    mooongs.image_crop(line)
    mooongs.google_OCR('')