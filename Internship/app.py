from flask import Flask, render_template, jsonify, send_file
import model  # Import the model file

app = Flask(__name__)

# Route for main dashboard (practice1.html)
@app.route('/')
def home():
    return render_template('practice1.html')

# Route for monthly trends page (practice2.html)
@app.route('/monthly-trends')
def monthly_trends():
    return render_template('practice2.html')

# API endpoint for revenue data
@app.route('/data/revenue')
def revenue_data():
    data = model.get_revenue_data()
    return jsonify(data)

# API endpoint for booking trends data
@app.route('/data/booking')
def booking_data():
    data = model.get_booking_data()
    return jsonify(data)

# API endpoint to get revenue graph
@app.route('/graph/revenue')
def revenue_graph():
    model.generate_revenue_graph()
    return send_file('static/revenue_graph.png', mimetype='image/png')

# API endpoint to get booking trend graph
@app.route('/graph/booking')
def booking_graph():
    model.generate_booking_trend()
    return send_file('static/booking_trend.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
