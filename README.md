<div align="center">

# PLAY THAT PEN PONG

### [Play Demo!](https://youtu.be/cwx__TPskns)

</div>

#### Contents
[1. About the project](#❤-About-the-project)  
[2. Getting Started](#💛-Getting-Started-(Installation))  
[3. Main Feature](#🧡-Main-Feature)  
[4. Page](#💚-Page)  
[5. Architecture](#💙-Architecture)  
[6. Contact](#💜-contact)  

------------------------
## ❤ About the project
다이어리 및 SNS 플랫폼이 넘쳐나는 요즘, 저희의 마음에 쏙 드는 플랫폼이 없었습니다. 저희가 원하던 건 '싸이월드' 같은 Y2K 감성 다이어리 블로그였으나, 2019년에 역사 속으로 사라지고 올해 부활한다는 소식이 들렸으나 예전 같지 않다는 것을 알게 되었습니다. 그래서 MZ세대들이 좋아할 만한 블로그 사이트를 직접 만들어야겠다는 다짐으로 이 프로젝트를 시작하였습니다. 저희가 즐겨 사용하던 기능들을 한데 모은 블로그 사이트, 저희가 직접 쓰고싶게 만든 사이트라 애착이 깊습니다. 디자인도 하나하나 직접 하며 MZ세대의 감성을 저격한, 어느 블로그보다 다채로운 그런 사이트를 지금부터 소개합니다:)

## 🧡 Main Feature
- Play That Pen Pong (login_page):
  - https 서버 보유
  - Google OAuth를 통한 로그인

- Black bookmark (main):
  - 프로필 관리 및 아바타 사진
  - 오늘의 랜덤 질문
  - 포스트 보관함 캘린더

- Red bookmark (avatar):
  - 나만의 아바타 꾸미기
  - 아바타 캡처 후 프로필 등록
  - 아바타 이미지 다운로드

- Blue bookmark (gust_book):
  - 원하는 스티커에 방명록 담기
  - 방명록 스티커로 바다 꾸미기
  - 방명록 페이징

- Green bookmark (post_list):
  - 폴라로이드 형식의 포스트 리스트
  - create/edit/delete post
  - 편지지 스티커 클릭시 포스트 작성
  - 포스트에 대표 사진 한 장 설정 가능(없을시 랜덤 이미지 생성)
  - 포스트에 파일 첨부 가능

## 💛 Getting Started (Installation)
1. ```git clone```

2. 프로젝트 폴더로 들어가기

3. 가상환경을 사용하고 싶다면, ```venv\Scripts\activate.bat```

4. 
```
pip install django
pip install django-crispy-forms
pip install django-allauth
pip install django-mathfilters
pip install pillow
```

5. 로컬에서 실행하기 ```python manage.py runserver```
6. 가상환경 종료 ```deactivate```

## 💚 Page
#### Play That Pen Pong (login_page)
![image](https://user-images.githubusercontent.com/71493251/202917619-38240747-0615-4b2d-ad50-1ade80d72a85.png)

#### Black bookmark (main):
![image](https://user-images.githubusercontent.com/71493251/202917341-f9df35be-b297-4226-9006-9682e1b5fa6e.png)

#### Red bookmark (avatar):
![image](https://user-images.githubusercontent.com/71493251/202917502-655c266d-ca7d-47fc-931f-47ca2c95b273.png)

#### Blue bookmark (gust_book):
![image](https://user-images.githubusercontent.com/71493251/202917575-fae61e95-54d5-4632-82ef-0345ac0d6118.png)

#### Green bookmark (post_list):
![image](https://user-images.githubusercontent.com/71493251/202917601-120cd9a9-8110-41d2-8de9-755fa795bc37.png)

## 💙 Architecture
p114
## 💜 Contact
- 강다현 | dusdj0813@khu.ac.kr
- 김나현 | knh4769@khu.ac.kr
