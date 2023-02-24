from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst', 
    'location': 'Bangkok, Thailand',
    'salary': 'Bht. 25,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist', 
    'location': 'Phuket, Thailand',
    'salary': 'Bht. 25,000'
  },
{
    'id': 3,
    'title': 'Engineer', 
    'location': 'Remote',
    'salary': 'Bht. 35,000'
  },
{
    'id': 4,
    'title': 'Tour Guide', 
    'location': 'Koh samui, Thailand',
    'salary': 'Bht. 25,000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

  @app.route("/api/jobs")
  def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
