from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('buatkopi2.html')

if __name__ == '__main__':
    app.run(debug=True)
# This code sets up a simple Flask web application that renders a template
# called 'buatkopi2.html' when the root URL is accessed. The application runs