# SignDection-by-googleOCR

## Introduction 

계약서 및 다양한 Signature의 유무를 판단합니다<br>
_Determine whether the contract and various documents have and do not have a Signature._
<br><br>
OCR 엔진은 구글엔진을 사용합니다. Text-detection 과 Labeling 의 OCR 결과들을 활용하였습니다.<br>
_The OCR engine uses a Google engine. We used OCR results of Text-detection and Labeling.
<br><br>
사인의 판단유무를 체크하기 위해 PIL Package를 활용하여 해당 부분을 Crop하였습니다.<br>
_To check the cause of death, we used PIL Package to crop the part.
<br><br>
현재, Crop부분은 자동으로 사인부분을 인지하지 못하여 직접 개발자가 해당 문서에 맞는 사인 부분의 좌표값을 설정해야합니다.<br>
_Currently, the Crop part does not automatically recognize the sine part, so the developer has to set the coordinates for the sine part that matches the document.
  
  
  <br><br><br><br>
  
  
## How to Use

먼저 Google API 키를 할당 받으셔아합니다.<br>
그후, API 사용법은 Google Vision에 자세히 나와있으니 Vision을 참고하시면 됩니다.<br>

API 키 부분이 본인의 API키를 넣어줍니다.<br>
PATH부분에 본인이 확인하고자하는 문서를 넣어줍니다.<br>


<br><br><br><br>


## 간략한 OCR 과정
<img width="621" alt="주석 2020-08-27 115747" src="https://user-images.githubusercontent.com/41941627/91379188-0adbc900-e85d-11ea-85d1-83f8b721794d.png">



