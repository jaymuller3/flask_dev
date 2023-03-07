# Image from Unsplash.com
# Random text generated from LoremIpsum.io
from flask import Flask, render_template, url_for

app = Flask(__name__)

jobs = [
    {'id': 1,
     'title': 'Data Scientist',
     'location': 'San Francisco',
     'salary': '$100,000'    
    },
    {'id': 2,
     'title': 'Frontend Engineer',
     'location': 'Remote',
     'salary': '$120,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)