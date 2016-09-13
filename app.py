import os
import sys
from bottle import route, run, template, request
from summpy.lexrank import summarize

@route('/')
def index():
    frm = """
        <h1>Paste Review!</h1>
        <form action="/sum" method="post">
            <p><textarea name="review" rows="25", cols="80"></textarea></p>
            <p><input type="submit" value="   summarize   " /></p>
        </form>
    """
    return template(frm)

@route('/sum', method="POST")
def sum():
    review = unicode(request.forms.get("review"), 'utf-8')
    try:
   	    sentences, debug_info = summarize(review, sent_limit=3, continuous=True, debug=True)
    except:
        print sys.exc_info()[0]
        raise

    sumres = ""
    for sent in sentences:
        sumres = sumres + sent

    out = """
        <h1>Summarize Result.</h1>
        <p>[REVIEW]</p>
        <p><textarea name="review" rows="25", cols="80">{{review}}</textarea></p>
        <p></p>
        <p>[RESULT]</p>
        <p><textarea name="sumres" rows="15", cols="80">{{sumres}}</textarea></p>
    """
    return template(out, review=review, sumres=sumres)

run(host='0.0.0.0', port=int(os.environ.get("PORT", 5364)))

