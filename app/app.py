from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Arjun", "department": "DevOps"},
    {"id": 2, "name": "Rahul", "department": "Cloud"}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Employee Management API",
        "status": "Running from GitHub Actions"
    })

@app.route("/health")
def health():
    return jsonify({"status": "Healthy"})

@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    for emp in employees:
        if emp["id"] == id:
            return jsonify(emp)
    return jsonify({"message": "Employee not found"}), 404

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.json

    employee = {
        "id": len(employees)+1,
        "name": data["name"],
        "department": data["department"]
    }

    employees.append(employee)

    return jsonify(employee),201

@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    global employees

    employees = [emp for emp in employees if emp["id"] != id]

    return jsonify({"message":"Employee deleted"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)