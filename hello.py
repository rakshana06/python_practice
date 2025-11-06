app = Flask(_name_)

@app.route('/')
def greet():
    """Return a custom friendly HTTP greeting."""
    return "Hi Everyone ! I am running through cloud shell from rakshana log in"

if _name_ == "_main_":
    app_host = "http://127.0.0.1:8080"
    print(f"App host link: {app_host}")
    app.run(host="127.0.0.1", port=8080, debug=True)
