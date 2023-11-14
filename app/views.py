from flask import render_template, Blueprint,request
# from .youtube import get_video_data

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    summary = None
    comments = []
    # if request.method == 'POST':
    #     video_url = request.form.get('video_url')
    #     video_id = video_url.split("=")[1]
    #     print(video_id)
    #     data = get_video_data(video_id)
    #     summary = data['summary']
    #     comments = list(zip(data['comments'], data['sentiments']))

    return render_template("index.html",summary=summary,comments=comments)