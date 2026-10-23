from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Jennifer Vo! I am adding my first code change'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

#favorite course and returns the subjct and course number
@app.route('/favorite-course')
def favoritecourse():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')

    print('Subject entered: ' + subject)
    print('Course number entered: ' + course_number)

    return render_template('favorite-course.html', subject=subject, course_number=course_number)

#contact with jinja template, returns form response if filled out, and if not then its false
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        contact_method = request.form.get('contact_method')

        print('First name entered: ' + first_name)
        print('Last name entered: ' + last_name)
        print('Email entered: ' + email)
        print('Contact method entered: ' + contact_method)

        if first_name and last_name and email and contact_method != 'Choose...':
            return render_template('contact.html', submitted=True, first_name=first_name,
                               last_name=last_name, email=email, contact_method=contact_method)

    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run()
