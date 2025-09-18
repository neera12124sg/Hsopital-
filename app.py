from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage (replace with database in production)
patients = []  # List of dicts: {'name': 'John Doe', 'age': 30, 'condition': 'Flu'}
doctors = []   # List of dicts: {'name': 'Dr. Smith', 'specialty': 'Cardiology'}
appointments = []  # List of dicts: {'patient': 'John Doe', 'doctor': 'Dr. Smith', 'date': '2025-09-20'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients', methods=['GET', 'POST'])
def patients_page():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        patients.append({'name': name, 'age': age, 'condition': condition})
        return redirect(url_for('patients_page'))
    return render_template('patients.html', patients=patients)

@app.route('/doctors', methods=['GET', 'POST'])
def doctors_page():
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        doctors.append({'name': name, 'specialty': specialty})
        return redirect(url_for('doctors_page'))
    return render_template('doctors.html', doctors=doctors)

@app.route('/appointments', methods=['GET', 'POST'])
def appointments_page():
    if request.method == 'POST':
        patient = request.form['patient']
        doctor = request.form['doctor']
        date = request.form['date']
        appointments.append({'patient': patient, 'doctor': doctor, 'date': date})
        return redirect(url_for('appointments_page'))
    return render_template('appointments.html', appointments=appointments, patients=patients, doctors=doctors)

if __name__ == '__main__':
    app.run(debug=True)
