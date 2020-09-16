# -*- coding: utf-8 -*-
class google_ocr:
    root_path = 'C:\\Users\\user\\Desktop\\SignDection-by-googleOCR-master\\'
    #root_path = '/var/local/webapps/ocr-portal/py/'
    
    def image_crop(path):
        from PIL import Image
        im = Image.open(path[0])
        (img_width, img_height) = im.size
        print(img_width)
        print(img_height)
        pos_x = img_width / 2;
        pos_y = img_height / 6;
        crop_rectangle1 = (0, pos_y*4, pos_x, pos_y*5)
        crop_rectangle2 = (0, pos_y*5, pos_x, pos_y*6)
        cropped_im = im.crop(crop_rectangle1)
        cropped_im.save(google_ocr.root_path + 'crop1.png')
        cropped_im2 = im.crop(crop_rectangle2)
        cropped_im2.save(google_ocr.root_path + 'crop2.png')
    
            
    #구글 라벨링 OCR 메서드입니다.
    def detect_labels(path, idx):
        """Detects labels in the file."""
        import os
        from google.cloud import vision
        import io

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= google_ocr.root_path + "test-ocr-dex-0e318a36ae9b.json"
        client = vision.ImageAnnotatorClient()

        if idx == 1:
            path_data = open(path).read().splitlines()
            
            with io.open(path_data[0], 'rb') as image_file:
                content = image_file.read()
        else:
            with io.open(path, 'rb') as image_file:
                content = image_file.read() 

       
    
        image = vision.types.Image(content=content)
        

        response = client.label_detection(image=image)
        labels = response.label_annotations
        result=[]
        logo_score=100
        for label in labels:
            result.append(label.description)
            if label.description=="Logo":
                logo_score=label.score*100
                print(logo_score)

        
        check = False

        print(result)    
        if "Calligraphy" in result:
            with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("캘리그래피 있어서 사인입니다.")
                check = True
        elif "Handwriting" in result:
            with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("Handwriting 있어서 사인입니다.")
            check = True
        elif "White" in result and "Black" in result:
             with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("화이트 블랙으로 사인이아닙니다.(1)")
                

        elif "Black-and-white" in result:
             with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("화이트 블랙으로 사인이아닙니다.(2)")

        elif logo_score < 70:
             with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("로고 정확도가 낮아서 사인입니다.")
        elif result==[]:
             with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("라벨링이 아무것도 없으면 사인입니다.")
        else:
             with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("로고 정확도가 높아서 사인이 아닙니다.")

       

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

    def test_crop(path, pos, i, name):
        from PIL import Image
        im = Image.open(path)
        (img_width, img_height) = im.size
        print('img_width : {}'.format(img_width))
        print('img_height : {}'.format(img_height))
        print(pos[i][0]['x'])
        print(pos[i][0]['y'])
        print(pos[i][1]['x'])
        print(pos[i][1]['y'])
        crop_rectangle = (pos[i][0]['x']-50, pos[i][0]['y']-50, pos[i][1]['x']+50, pos[i][1]['y']+50)
        cropped_im = im.crop(crop_rectangle)
        cropped_im.save(google_ocr.root_path + name)

    def test_crop2(path):
        from PIL import Image
        im = Image.open(path)
        (img_width, img_height) = im.size
        print(img_width)
        print(img_height)
        pos_x = img_width / 2;
        crop_rectangle1 = (0, 0, pos_x, img_height)
        crop_rectangle2 = (pos_x, 0, img_width, img_height)
        cropped_im = im.crop(crop_rectangle1)
        cropped_im.save(google_ocr.root_path + 'crop1.png')
        cropped_im2 = im.crop(crop_rectangle2)
        cropped_im2.save(google_ocr.root_path + 'crop2.png')

    
      #구글  OCR 메서드입니다. 위에 구글 라벨링 OCR은 해당 메서드에서 호출됩니다.
    def google_OCR(input_file):
        import requests
        #import win32api
        import base64
        import json
        import sys
        import config as cfg
        from PIL import Image
       
        api_key = 'AIzaSyCvOsFqq4L5qlF3BgMe2iFKp13UsixO5qM'

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

        

        json_response = response.json()

        
        make = json_response['responses'][0]['textAnnotations']
        pre = make[0]['boundingPoly']['vertices'][0]['y']
        pre_co = make[0]['boundingPoly']['vertices'][0]['y']
        for item in make:
            if item['boundingPoly']['vertices'][0]['y'] - pre_co < 10 and item['boundingPoly']['vertices'][0]['y'] - pre_co > -10:
                pre_co = item['boundingPoly']['vertices'][0]['y']
                item['boundingPoly']['vertices'][0]['y'] = pre
            else:
                pre = item['boundingPoly']['vertices'][0]['y']
                pre_co = item['boundingPoly']['vertices'][0]['y']
        make = sorted(json_response['responses'][0]['textAnnotations'], key=lambda vertice: (vertice['boundingPoly']['vertices'][0]['y'], vertice['boundingPoly']['vertices'][0]['x']))
        with open(google_ocr.root_path + 'make.json', 'w', encoding='utf-8') as output_file:
            json.dump(make, output_file, ensure_ascii=True)

        
        field = json_response['responses'][0]['textAnnotations']
        pos = {}
        max_x = 0
        max_y = 0
        temp_x = 0
        temp_y = 0
        st_x = 0
        st_y = 0
        idx = 0
        for i in range(len(field)-1):
            if i > 0:
                
                if st_x == 0 and st_y == 0:
                    print(field[i]['description'])
                    st_x = field[i]['boundingPoly']['vertices'][0]['x']
                    st_y = field[i]['boundingPoly']['vertices'][0]['y']
                if field[i+1]['boundingPoly']['vertices'][0]['x'] - field[i]['boundingPoly']['vertices'][1]['x'] < 100 and field[i+1]['boundingPoly']['vertices'][0]['x'] - field[i]['boundingPoly']['vertices'][1]['x'] > 0:
                    temp_x = field[i+1]['boundingPoly']['vertices'][1]['x']
                    #print('temp_x : ')
                    #print(temp_x)
                elif field[i+1]['boundingPoly']['vertices'][0]['x'] - field[i]['boundingPoly']['vertices'][1]['x'] < 0 or field[i+1]['boundingPoly']['vertices'][0]['x'] - field[i]['boundingPoly']['vertices'][1]['x'] > 100:
                    if max_x < temp_x:
                        max_x = temp_x
                        temp_x = 0
                        #print('max_x : ')
                        #print(max_x)
                    if field[i+1]['boundingPoly']['vertices'][0]['y'] - field[i]['boundingPoly']['vertices'][2]['y'] < 100:
                        #print('==============')
                        #print(field[i+1]['boundingPoly']['vertices'][0]['y'])
                        #print(field[i]['boundingPoly']['vertices'][2]['y'])
                        max_y = field[i+1]['boundingPoly']['vertices'][2]['y']
                        #print('max_y : ')
                        #print(max_y)
                    else :
                        if max_y == 0:
                            max_y = field[i]['boundingPoly']['vertices'][2]['y']
                        print('========문단 획득========')
                        print(field[i]['description'])
                        pos[idx] = [{"x": st_x, "y": st_y},{"x":max_x, "y":max_y}]
                        max_x = 0
                        max_y = 0
                        st_x = 0
                        st_y = 0
                        idx = idx+1
                
                    
                    

        with open(google_ocr.root_path + 'pos.json', 'w', encoding='utf-8') as output_file:
            json.dump(pos, output_file, ensure_ascii=True)
            
        with open(google_ocr.root_path + 'sign_output.json', 'w', encoding='utf-8') as output_file:
            json.dump(field, output_file, ensure_ascii=True)

        if json_response['responses']==[{}]:
            with open(google_ocr.root_path + "sign_result.txt", "w") as f:
                f.write("오류로인한 사인입니다.")
        #else:
#            words = json_response['responses'][0]['textAnnotations'][0]['description']
#            print("인식한 결과 :",words)

#            if words!='(인)\n':
                #해당 프로세스는 (인) 만들어오는것이 아닌 다른것도 같이 들어온다.
#                with open(google_ocr.root_path + "sign_result.txt", "w") as f:
#                    f.write("인이 아니므로 사인입니다.")

        else:
        #input_data=''.join(input_data)
            #google_ocr.image_crop(input_data)
            im = Image.open(google_ocr.root_path + 'image\\for\\0001.jpg')
            (im_width, im_height) = im.size
            for i in range(len(pos)):
                print(i)
                google_ocr.test_crop(google_ocr.root_path + 'image\\for\\0001.jpg', pos, i, 'crop{}.jpg'.format(i))
                im2 = Image.open(google_ocr.root_path + 'crop{}.jpg'.format(i))
                (img_width, img_height) = im2.size
                if img_width > im_width / 2:
                    google_ocr.test_crop2(google_ocr.root_path + 'crop{}.jpg'.format(i))
                    google_ocr.detect_labels(google_ocr.root_path + 'crop1.png'.format(i), 2)
                    google_ocr.detect_labels(google_ocr.root_path + 'crop2.png'.format(i), 2)

                else:
                    with open(google_ocr.root_path + "path.txt", "w") as f:
                        f.write(google_ocr.root_path + 'crop{}.jpg'.format(i))
                    google_ocr.detect_labels(google_ocr.root_path + 'path.txt', 1)
       

        
        
if __name__ == "__main__":
    mooongs=google_ocr
#    f = open(mooongs.root_path + "sign_input.txt", 'r')
#    line = f.readline()
#    print(line)
    mooongs.google_OCR(mooongs.root_path + "sign_input.txt")
