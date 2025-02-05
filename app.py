from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

# Generic GET function for any entity
def get_entity(entity):
    return jsonify(data[entity])

# Generic GET by ID function for any entity
def get_entity_by_id(entity, id):
    item = next((item for item in data[entity] if item["id"] == id), None)
    return jsonify(item) if item else (jsonify({"error": "Not found"}), 404)

# Generic POST function for any entity
def add_entity(entity):
    new_item = request.json
    data[entity].append(new_item)
    save_data(data)
    return jsonify(new_item), 201

# Generic PUT function for any entity
def update_entity(entity, id):
    for item in data[entity]:
        if item["id"] == id:
            item.update(request.json)
            save_data(data)
            return jsonify(item)
    return jsonify({"error": "Not found"}), 404

# Generic DELETE function for any entity
def delete_entity(entity, id):
    data[entity] = [item for item in data[entity] if item["id"] != id]
    save_data(data)
    return jsonify({"message": "Deleted"})

# Patients Routes
@app.route("/patients", methods=["GET"])
def get_patients():
    return get_entity("patients")

@app.route("/patients/<int:id>", methods=["GET"])
def get_patient(id):
    return get_entity_by_id("patients", id)

@app.route("/patients", methods=["POST"])
def add_patient():
    return add_entity("patients")

@app.route("/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    return update_entity("patients", id)

@app.route("/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    return delete_entity("patients", id)

# Doctors Routes
@app.route("/doctors", methods=["GET"])
def get_doctors():
    return get_entity("doctors")

@app.route("/doctors/<int:id>", methods=["GET"])
def get_doctor(id):
    return get_entity_by_id("doctors", id)

@app.route("/doctors", methods=["POST"])
def add_doctor():
    return add_entity("doctors")

@app.route("/doctors/<int:id>", methods=["PUT"])
def update_doctor(id):
    return update_entity("doctors", id)

@app.route("/doctors/<int:id>", methods=["DELETE"])
def delete_doctor(id):
    return delete_entity("doctors", id)

# Appointments Routes
@app.route("/appointments", methods=["GET"])
def get_appointments():
    return get_entity("appointments")

@app.route("/appointments/<int:id>", methods=["GET"])
def get_appointment(id):
    return get_entity_by_id("appointments", id)

@app.route("/appointments", methods=["POST"])
def add_appointment():
    return add_entity("appointments")

@app.route("/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):
    return update_entity("appointments", id)

@app.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):
    return delete_entity("appointments", id)

# Prescriptions Routes
@app.route("/prescriptions", methods=["GET"])
def get_prescriptions():
    return get_entity("prescriptions")

@app.route("/prescriptions/<int:id>", methods=["GET"])
def get_prescription(id):
    return get_entity_by_id("prescriptions", id)

@app.route("/prescriptions", methods=["POST"])
def add_prescription():
    return add_entity("prescriptions")

@app.route("/prescriptions/<int:id>", methods=["PUT"])
def update_prescription(id):
    return update_entity("prescriptions", id)

@app.route("/prescriptions/<int:id>", methods=["DELETE"])
def delete_prescription(id):
    return delete_entity("prescriptions", id)

# Billing Routes
@app.route("/billing", methods=["GET"])
def get_billing():
    return get_entity("billing")

@app.route("/billing/<int:id>", methods=["GET"])
def get_bill(id):
    return get_entity_by_id("billing", id)

@app.route("/billing", methods=["POST"])
def add_bill():
    return add_entity("billing")

@app.route("/billing/<int:id>", methods=["PUT"])
def update_bill(id):
    return update_entity("billing", id)

@app.route("/billing/<int:id>", methods=["DELETE"])
def delete_bill(id):
    return delete_entity("billing", id)

if __name__ == "__main__":
    app.run(debug=True)
