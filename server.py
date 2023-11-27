from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:subpath>')
def html_page(subpath):
    return render_template(subpath)

#Write the user data to text file
def write_to_file(data):
    with open('.venv/db_file.txt',mode='a') as database:
        email=data["email"]        
        subject=data['subject']
        message= data['message']
        file = database.write(f'\n{email} , {subject} , {message}')      

#Write the user data to csv file
def write_to_csv(data):
    with open('.venv/db_file.csv',mode='a', newline='') as csvfile:
        email=data["email"]        
        subject=data['subject']
        message= data['message']
        writer = csv.writer(csvfile)
        writer.writerow([email, subject, message])

#On click of send button on contact form page
@app.route('/submit_form', methods=['POST', 'GET']) #GET means the browser wants us to set information and use it in the url and POST means that the browser wants us to save information.
def submit_form():
    if request.method == 'POST':
        # subject = request.form['subject']
        # email = request.form['email']
        # message = request.form['message']
        # To fetch data in the form of dictionary
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'    
    else:
        return 'something went wrong. Try again'     
