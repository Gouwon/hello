```
django-admin startproject django_pjt
```
  명령어 실행 이후, 상위 디렉토리의 이름을 django_pjt -> django_book1으로 변경함.
  
  nginx server conf 파일은 /usr/local/etc/nginx/servers에서 include됨.
  따라서 nginx.conf를 따로 만들어서 이 디렉터리에 추가해줘야 함.
  ```
  ln -s ~/workspace/hello/django/django_book1/nginx/django_pjt_nginx.conf ./servers/django_pjt_nginx
  ```
  명령어로 심볼릭 링크를 만듦. 


  uwsgi를 이용하기 위해서 /etc/uwsgi/vassals 만듦.
  그리고 심볼릭 링크로 uwsgi.ini 추가.

  rest_framework 작업...