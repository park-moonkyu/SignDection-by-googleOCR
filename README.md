# SignDection-by-googleOCR

## Introduction 

계약서 및 다양한 Signature의 유무를 판단합니다
_Determine whether the contract and various documents have and do not have a Signature._

OCR 엔진은 구글엔진을 사용합니다. Text-detection 과 Labeling 의 OCR 결과들을 활용하였습니다.
_The OCR engine uses a Google engine. We used OCR results of Text-detection and Labeling.

사인의 판단유무를 체크하기 위해 PIL Package를 활용하여 해당 부분을 Crop하였습니다.
_To check the cause of death, we used PIL Package to crop the part.

현재, Crop부분은 자동으로 사인부분을 인지하지 못하여 직접 개발자가 해당 문서에 맞는 사인 부분의 좌표값을 설정해야합니다.
_Currently, the Crop part does not automatically recognize the sine part, so the developer has to set the coordinates for the sine part that matches the document.

## How to Use

먼저 Google API 키를 할당 받으셔아합니다.
그후, API 사용법은 Google Vision에 자세히 나와있으니 Vision을 참고하시면 됩니다.

**API 키 부분이 본인의 API키를 넣어줍니다.
**PATH부분에 본인이 확인하고자하는 문서를 넣어줍니다.

## 간략한 OCR 과정



