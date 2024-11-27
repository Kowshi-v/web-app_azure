from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template with Embedded CSS and JS
@app.route('/')
def index():
    html_code = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To Do Tracker</title>

        <link rel="stylesheet" href="data:text/css;base64,{{ css_data }}">
    </head>
    <body>
        <div class="app">
            <div class="container">
                <div id="wrapper">
                    <input type="text" placeholder="What's there in your mind ?..." />
                    <button id="add-button">Add Task</button>
                </div>
                <div id="tasks">
                    <p id="pending tasks">
                        You have <span class="count-value">0</span> task(s) to complete
                    </p>
                </div>
            </div>
            <p id="error">Input cannot be empty !!</p>
        </div>

        <script>
        {{ js_data }}
        </script>
    </body>
    </html>
    '''

    # Read the CSS and JS as raw data
    with open('style.css', 'r') as css_file:
        css_data = css_file.read()

    with open('main.js', 'r') as js_file:
        js_data = js_file.read()

    return render_template_string(html_code, css_data=css_data, js_data=js_data)

if __name__ == '__main__':
    app.run(debug=True)
