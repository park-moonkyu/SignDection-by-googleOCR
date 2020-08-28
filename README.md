# SignDection-OCR(서명 유/무 판단 OCR)
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
  
  <br><br>
  
## How to Use

먼저 Google API 키를 할당 받으셔아합니다.<br>
API를 사용하기 앞서 윈도우/맥 환경에 맞춰서  os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="YOUR File.json" 과정도 필요합니다.<br>
자세한 OCR 사용법은  길게 설명하지 않겠습니다. Google Vision에 자세히 나와있으니 해당 홈페이지를 참고하시면 됩니다.<br><br>

API 키 부분이 본인의 API키를 넣어줍니다.<br>
PATH부분에 본인이 확인하고자하는 문서를 넣어줍니다.<br>


<br><br>

## 추후 개선 사항 
(1)현재 사인이 있는 부분을 Google Text OCR, Google Label OCR에서 사인이 없다고 판단하는 문서들이 2~3개 발생합니다.<br>
(2)또한 OCR결과가 사인이 있는 부분과 없는 부분이 일치하여 Labeling한 결과 Label값(Text, Line 만 존재)도 일치하는 문서들도 발생합니다.<br>
(3) 현재 Crop부분은 수동으로 진행됩니다. <br>
따라서 해당 문서 및 다양한 데이터들을 활용하여 위와 같은 오류를 수정해 나갈 계획입니다. (2020.08.28 부)
<br>
(진행방향) <br>
(1)사인이 존재함에도 없다고 판단하는 문서들의 라벨값을 사인이 있는것들과 대조하여 라벨 및 라벨의 정확도를 Fine tuning할 예정입니다.<br>
(2)라벨값들이 아닌 해당 라벨값들의 결과 정확도를 세밀하게 조정 예정입니다.<br>
(3) Crop 부분의 자동화를 위해 다양한 기술들을 적용 및 테스트합니다.
<br>
<br>
<br>
## 간략한 OCR 과정
<img width="621" alt="주석 2020-08-27 115747" src="https://user-images.githubusercontent.com/41941627/91379188-0adbc900-e85d-11ea-85d1-83f8b721794d.png">

<br><br>
==================================================
##2020.08.27 추가 작업 내용입니다.
<br><br>
<img width="606" alt="zzzz" src="https://user-images.githubusercontent.com/41941627/91419764-c36e3080-e88e-11ea-9828-1622956b46f6.png">
