from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
cats_images = [
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr01/15/9/anigif_enhanced-buzz-31540-1381844535-8.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr02/15/9/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-18774-1381844645-6.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-25158-1381844793-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/10/anigif_enhanced-buzz-11980-1381846269-1.gif"
]

# list of dog images
dogs_images = [
    "http://www.doggifpage.com/gifs/150.gif",
    "http://www.doggifpage.com/gifs/105.gif",
    "http://www.doggifpage.com/gifs/148.gif",
    "http://www.doggifpage.com/gifs/146.gif",
    "http://www.doggifpage.com/gifs/144.gif",
    "http://www.doggifpage.com/gifs/143.gif",
    "http://www.doggifpage.com/gifs/139.gif",
    "http://www.doggifpage.com/gifs/137.gif",
    "http://www.doggifpage.com/gifs/136.gif",
    "http://www.doggifpage.com/gifs/135.gif",
    "http://www.doggifpage.com/gifs/128.gif",
    "http://www.doggifpage.com/gifs/120.gif"
]

@app.route('/')
def index():
    combined_list = cats_images + dogs_images
    url = random.choice(combined_list)
    return render_template('index.html', url=url)

@app.route('/cats')
def cats_index():
    url = random.choice(cats_images)
    return render_template('index.html', url=url)

@app.route('/dogs')
def dogs_index():
    url = random.choice(dogs_images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")