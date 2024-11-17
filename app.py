from flask import Flask, render_template, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initializing the Flask applicatino
app = Flask(__name__)

# All admin routing
@app.route('/admin/dashboard', methods=['GET'])
def adminDash():
    return 'Index Page'

@app.route('/admin/search', methods=['GET'])
def adminSearch():
    searchBY = request.args.get('searchBY')
    searchText = request.args.get('searchText')

    results = []
    if searchBY == 'services':
        results = []
    elif searchBY == 'customers':
        results = []
    elif searchBY == 'professionals':
        results = []
    
    return render_template('admin/search.html')

@app.route('/admin/summary', methods=['GET', 'POST'])
def adminSummary():
    return 'Hello, World'

@app.route('/admin/create_Service', methods=['GET', 'POST'])
def adminServiceCreate():
    return 'Hello, World'


# Authorization routing
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    return 'Hello, World'

@app.route('/auth/customer_signup', methods=['GET', 'POST'])
def customerSignUp():
    return 'Hello, World'

@app.route('/auth/professional_signup', methods=['GET', 'POST'])
def professionalSignUp():
    return 'Hello, World'


# Customer routing
@app.route('/customer/dashboard', methods=['GET', 'POST'])
def customerDashboard():
    return 'Hello, World'

@app.route('/customer/search', methods=['GET'])
def customerSearch():
    return 'Hello, World'

@app.route('/customer/service_remarks', methods=['GET'])
def serviceRemarks():
    return 'Hello, World'

@app.route('/customer/services', methods=['GET', 'POST'])
def services():
    return 'Hello, World'

@app.route('/customer/summary', methods=['GET', 'POST'])
def customerSummary():
    return 'Hello, World'


# Service Professional routing
@app.route('/professional/dashboard', methods=['GET', 'POST'])
def professionalDashboard():
    return 'Hello, World'

@app.route('/professional/search', methods=['GET', 'POST'])
def professionalSearch():
    return 'Hello, World'

@app.route('/professional/summary', methods=['GET', 'POST'])
def professionalSummary():
    return 'Hello, World'