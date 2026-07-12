from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    return f"""
    <html>
        <head>
            <title>Rakshana's First Flask App</title>

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: white;
                    text-align: center;
                    margin-top: 80px;
                }}

                .card {{
                    background: white;
                    color: #0f172a;
                    width: 600px;
                    margin: auto;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.15);
                }}

                h1 {{
                    color: #2563eb;
                    margin-bottom: 20px;
                }}

                p {{
                    font-size: 18px;
                    line-height: 1.6;
                }}

                footer {{
                    margin-top: 25px;
                    color: #64748b;
                    font-size: 14px;
                }}
            </style>

        </head>

        <body>

            <div class="card">

                <h1>🚀 Welcome to My First Flask Web Application</h1>

                <p>
                    Hello! I'm <b>Rakshana R J</b>, a Computer Science and Business Systems (CSBS) student.
                </p>

                <p>
                    This is my first web application built using <b>Python</b> and <b>Flask</b>.
                    It marks the beginning of my web development and GitHub learning journey.
                </p>

                <p>
                    <b>Current Server Time</b><br>
                    {current_time}
                </p>

                <footer>
                    Built with ❤️ using Python & Flask by Rakshana R J
                </footer>

            </div>

        </body>
    </html>
    """

if __name__ == "__main__":
    print("Server running at http://127.0.0.1:8080")
    app.run(host="127.0.0.1", port=8080, debug=True)
