from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "San Francisco, CA",
        "salary": "$120,000 per year"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "New York, NY",
        "salary": "$130,000 per year"
    },
    {
        "id": 3,
        "title": "Marketing Manager",
        "location": "Los Angeles, CA",
        "salary": "$100,000 per year"
    },
    {
        "id": 4,
        "title": "Graphic Designer",
        "location": "Chicago, IL",
        "salary": "$90,000 per year"
    },
    {
        "id": 5,
        "title": "Financial Analyst",
        "location": "Houston, TX",
        "salary": "$110,000 per year"
    }
]




@app.route('/')
def hello_world():
    # return "Hello, World!"
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    # serve(app, host="0.0.0.0", port=8000)
