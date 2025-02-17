from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Process form data here
        date = request.form['date']
        category = request.form['category']
        merchant = request.form['merchant']
        amount = request.form['amount']
        payment_method = request.form['payment_method']
        notes = request.form['notes']
        
        # Save data to spread sheet

        return "Expense recorded successfully!", 200

    return render_template('index.html')

if __name__ == '__main__':
    app.run()