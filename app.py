import os
from bottle import route, run, template, request

@route('/')
def index():
    frm = """
        <h1>Hello</h1>
        <form action="/sum" method="post">
            <input type="text" name="review" />
            <input type="submit" name="sb" value="DO" />
        </form>
    """
    return template(frm)

@route('/sum', method="POST")
def sum():
    review = request.forms.get("review")
    return template('<b>{{review}}</b>', review=review)

run(host='0.0.0.0', port=int(os.environ.get("PORT", 5364)))

