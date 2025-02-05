# healthcare_management
# Healthcare API

This Flask-based API manages **patients, doctors, appointments, prescriptions, and billing** with full CRUD functionality.

## Features
- Manage **Patients**, **Doctors**, **Appointments**, **Prescriptions**, and **Billing**.
- Generic functions for streamlined CRUD operations.
- Data stored in `data.json`.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/healthcare-api.git
   cd healthcare-api
   ```
2. Install dependencies:
   ```sh
   pip install flask
   ```
3. Run the API:
   ```sh
   python app.py
   ```

## API Endpoints
### Patients
- `GET /patients` - Get all patients.
- `GET /patients/<id>` - Get a patient by ID.
- `POST /patients` - Add a new patient.
- `PUT /patients/<id>` - Update a patient.
- `DELETE /patients/<id>` - Delete a patient.

### Doctors
- `GET /doctors` - Get all doctors.
- `GET /doctors/<id>` - Get a doctor by ID.
- `POST /doctors` - Add a new doctor.
- `PUT /doctors/<id>` - Update a doctor.
- `DELETE /doctors/<id>` - Delete a doctor.

### Appointments
- `GET /appointments` - Get all appointments.
- `GET /appointments/<id>` - Get an appointment by ID.
- `POST /appointments` - Add a new appointment.
- `PUT /appointments/<id>` - Update an appointment.
- `DELETE /appointments/<id>` - Delete an appointment.

### Prescriptions
- `GET /prescriptions` - Get all prescriptions.
- `GET /prescriptions/<id>` - Get a prescription by ID.
- `POST /prescriptions` - Add a new prescription.
- `PUT /prescriptions/<id>` - Update a prescription.
- `DELETE /prescriptions/<id>` - Delete a prescription.

### Billing
- `GET /billing` - Get all billing records.
- `GET /billing/<id>` - Get a billing record by ID.
- `POST /billing` - Add a new billing record.
- `PUT /billing/<id>` - Update a billing record.
- `DELETE /billing/<id>` - Delete a billing record.

## Data Structure
Data is stored in `data.json` and follows this structure:
```json
{
    "patients": [...],
    "doctors": [...],
    "appointments": [...],
    "prescriptions": [...],
    "billing": [...]
}
```


