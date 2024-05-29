import tweepy
import json
from googletrans import Translator
from flask import Flask, request, render_template

app = Flask(__name__)

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    config = load_config()
    if request.method == 'POST':
        config['CONSUMER_KEY'] = request.form['consumer_key']
        config['CONSUMER_SECRET'] = request.form['consumer_secret']
        config['ACCESS_TOKEN'] = request.form['access_token']
        config['ACCESS_TOKEN_SECRET'] = request.form['access_token_secret']
        config['TARGET_ACCOUNT'] = request.form['target_account']
        config['CRON_SCHEDULE'] = request.form['cron_schedule']
        save_config(config)
    return render_template('index.html', config=config)

def get_latest_tweet(account):
    tweets = api.user_timeline(screen_name=account, count=1, tweet_mode="extended")
    return tweets[0] if tweets else None

def translate_tweet(tweet_text):
    translator = Translator()
    translated = translator.translate(tweet_text, src='en', dest='zh-cn')
    return translated.text

def post_tweet(text):
    api.update_status(status=text)

@app.route('/run', methods=['GET'])
def run():
    config = load_config()
    auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
    auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    tweet = get_latest_tweet(config['TARGET_ACCOUNT'])
    if tweet:
        translated_text = translate_tweet(tweet.full_text)
        post_tweet(translated_text)
    return 'Success'

if __name__ == "__main__":
    app.run(debug=True)