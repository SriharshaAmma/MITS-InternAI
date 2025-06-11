from flask import Flask, render_template, request, flash
import predictor

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = {
            'cgpa': float(request.form['cgpa']),
            'projects': int(request.form['projects']),
            'internships': int(request.form['internships']),
            'participation': float(request.form['participation'])
        }
    except ValueError:
        flash("Please enter valid numeric values for all fields.")
        return render_template('index.html', prediction=None)

    result = predictor.predict_success(features)
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    from dash_dashboard import init_dashboard
    init_dashboard(app)
    app.run(debug=True, port=5001)
