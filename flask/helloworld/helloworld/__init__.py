from flask import Flask

app = Flask(__name__)
### Flask constructor attributes
### 1. static_url_path : define static_directory location from web. default location is ./static
### 2. static_folder : define static_folder location in filesystem. default location is ./static
### 3. template_folder : define template_folder locaion in filesystem. default location is ./templates

# @app.route("/")
# def helloworld():
#     return "Hello World"

from flask import g
import sqlite3
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request_db_ready():
    g.db = connect_db()

@app.teardown_request
def teardown_request_db_close(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

from flask import Response, make_response
@app.route("/")
def response_test():
    # custom_response = Response("Custom Response", 200, {"Program" : "Flask Web Application"})
    custom_response = ('Tuple Custom Response', 'OK', {'response_method' : "Tuple Response"})

    return make_response(custom_response)

@app.before_first_request
def before_first_request():
    print("앱이 기동되고 나서 첫 번째 HTTP 요청에만 응답합니다.")

@app.before_request
def before_request():
    print("매 HTTP 요청이 처리되고 나서 실행됩니다.")

## before_first_request와 before_request decorator를 사용한 함수들은 flask instance 내의 before_first_request_funcs, before_request_func list에 append됨.

@app.after_request
def after_request(response):
    print("매 HTTP 요청이 처리되고 나서 실행됩니다.")
    return response

@app.teardown_request
def teardown_request(exception):
    print("매 HTTP 요청의 결과가 브라우저에 응답하고 나서 호출됩니다.")

@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행됩니다.")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
