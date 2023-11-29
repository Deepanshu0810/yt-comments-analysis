from flask import render_template, Blueprint,request
from .youtube import get_video_comments
from .predict import predict_sentiments

views = Blueprint('views', __name__)

def get_video_data(video_id):
    if video_id == '':
        return {'comments': [], 'sentiments': []}
    
    comments = get_video_comments(video_id)
    prediction = predict_sentiments(comments)

    pos_count = prediction.count('Positive')
    neg_count = prediction.count('Negative')

    summary = {
        'pos_count': pos_count,
        'neg_count': neg_count,
        'total': pos_count + neg_count,
        'pos_percent': round(pos_count / (pos_count + neg_count) * 100, 2),
        'neg_percent': round(neg_count / (pos_count + neg_count) * 100, 2)
    }

    return {'comments': comments, 'sentiments': prediction, 'summary': summary}

@views.route('/', methods=['GET', 'POST'])
def home():
    summary = None
    comments = []
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if video_url == '':
            return render_template("index.html",summary=summary,comments=comments)
        video_id = video_url.split("=")[1]
        print(video_id)
        data = get_video_data(video_id)
        comments = list(zip(data['comments'], data['sentiments']))
        summary = data['summary']
        print(summary)
    return render_template("index.html",summary=summary,comments=comments)