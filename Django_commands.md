## 🤔<span style="color:red">가상환경 활성화 확인</span> 
```python
source myvenv/Scripts(mac:bin)/activate
```
```python
source myvenv/bin/activate
```

## 🤔<span style="color:red">현재 디렉토리 확인 $/~/manage.py</span>  
`ls`

 ## 앱 생성  
1. manage.py로 새로운 앱 생성
```python
 python manage.py startapp <appname>
```                                 
<br>
2. project의 settings.py에서 app등록

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  
    'appname',  #등록
]
```

# 🙀 MTV 패턴 -> developement_sequence.md

## View
- view는 지휘자, 컨트롤러
- 기능, 처리 
```python
from django.shortcuts import render

def home(request) :
    #이 자리에 모델을 다루는 코드가 들어감.
    return render(request, 'home.html')
```
###### 모델을 다루지 않으므로 바로 return

## Template

- 화면 표시
1. app 안에 직접 `templates` 디렉토리 생성
2. `templates` 안에 html 파일 생성
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>타이틀 바, 페이지 탭에 나타나는 부분</title>
</head>
<body>
    웹 페이지에 나타나는 부분
</body>
</html>
```
`! + tab키` : html 문서 기본 규격 자동 생성
## URL
- project의 urls.py
```python
from django.contrib import admin
from django.urls import path
from appname import views #view를 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
]
```
**path(`url`, `해당 view의 함수`, `urlpattern 이름`)**
