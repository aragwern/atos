from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('data.txt', mode='a') as txt_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = txt_file.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open('data.csv', mode='a', newline='') as csv_file:
        fieldnames = ["email","subject","message"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'form error'
