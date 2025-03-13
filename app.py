from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    team = os.getenv('TEAM', 'Unknown')
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Team Display</title>
    </head>
    <body>
        <h1>Welcome to the Team Page</h1>
        <p>Team: {{ team }}</p>
    </body>
    </html>
    """
    return render_template_string(html, team=team)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)