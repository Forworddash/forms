from flask import Flask, render_template, request

# create an instance of the Flask class
app = Flask(__name__)

# define routes and views
@app.route('/')
def home():
    return render_template('canvas.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # process sign-in form data
        username = request.form['username']
        password = request.form['password']
        # validate credentials and handle sign-ins
        return 'Sign-in successful!'
    #if the request method is GET, return the sign-in form
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)