from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, world!</h1>' \
           '<p> Just a cat website for now.</p>' \
           '<img src="https://media2.giphy.com/media/5i7umUqAOYYEw/giphy.webp?cid=ecf05e47rhxxwlpcmabknvylh2gjs8m22ojvkfmkj9q71n8l&rid=giphy.webp&ct=g" width:200px>'

# Different routes using the app.route decorator
@app.route('/bye')
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}! I know that you're {number} year old."


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
