# Django

## 0. setting

- `.gitignore`
- 가상환경 설정/실행
    - `python -m venv venv`
    - `source venv/Script/activate`
- `README.md`

## 1. Django 프로젝트

1. django 설치
```shell
pip install django
```

2. 프로젝트 생성
```shell
django-admin startproject <pjt_name> <path>
```

3. 서버실행(종료 : `ctrl + c`)
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app_name>
```

5. 앱 등록(`settings.py`)
```python
INSTALLED_APPS = [
    <APP NAMES>,
]
```
# settings.py의 installed_apps에 app name을 직접 기록해서 등록
