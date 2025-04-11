from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Addis Ababa, Ethiopia',
        'salary' : '10,000 ETB'
    },
    {
        'id' : 2,
        'title' : 'Software Eng',
        'location' : 'Hawassa, Ethiopia',
        'salary' : '20,000 ETB'
    },
    {
        'id' : 3,
        'title' : 'Data Eng',
        'location' : 'Adama, Ethiopia',
        'salary' : '30,000 ETB'
    },
    {
        'id' : 4,
        'title' : 'Cyber Analyst',
        'location' : 'Addis Ababa, Ethiopia',
        'salary' : '50,000 ETB'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)