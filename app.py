from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    # Define features and descriptions here
    features = [
        {'title': 'Comprehensive Dashboard', 'description': 'See trends and insights unfold as your data updates.'},
        {'title': 'Ease of Use', 'description': 'The SaaS web platform allows businesses to simply upload their files for automated analysis, with all data securely stored in the cloud. We get insights just by uploading file in format of your choice. It can read a dataset in various formats such as xlsx, csv, jpg, png, pdf and etc.'},
        {'title': 'Mobile compatibility', 'description': 'Users can capture physical invoices with their mobile camera and upload them to get insights in a click.'},
        {'title': 'Handy AI assistant', 'description': 'We can chat with the AI assistant in our natural language and in our desired language, whether it be Hindi, Telugu, Tamil, Bengali, etc.'},
        {'title': 'Precise Demand Predictions', 'description': 'Utilizes advanced algorithms for accurate forecasts.'},
        {'title': 'Real-Time Insights', 'description': 'Provides immediate, actionable data for decision-makers.'},
        {'title': 'User-Friendly Interface', 'description': 'Easy to navigate, no prior experience required.'},
        {'title': 'Accurate Forecasting', 'description': 'With precise demand predictions, they optimized their stock levels.'},
    ]
    return render_template('features.html', features=features)

@app.route('/pricing')
def pricing():
  return render_template('pricing.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/team')
def team():
  return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)
