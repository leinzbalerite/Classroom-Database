import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_read_query
from sql import execute_query
import creds

# setting up the name of the application
app = flask.Flask(__name__) # sets up the application
app.config["DEBUG"] = True # allow errors to be shown in browser

myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

# Add a facility
@app.route('/api/facility', methods=['POST'])
def add_facility():
    name = request.json['name']
    query = f"INSERT INTO facility (name) VALUES ('{name}');"
    execute_read_query(conn, query)
    return jsonify({'message': 'Facility added successfully', 'name' : name})

# get all facilities
@app.route('/api/facility', methods=['GET'])
def get_facilities():
    query = "SELECT * FROM facility;"
    facilities = execute_read_query(conn, query)
    return jsonify(facilities)

# Get single facility
@app.route('/api/facility/<int:id>', methods=['GET'])
def get_facility(id):
    query = f"SELECT * FROM facility WHERE id = {id};"
    facility = execute_read_query(conn, query)
    return jsonify(facility)

#update a Facility
@app.route('/api/facility/<int:id>', methods=['PUT'])
def update_facility(id):
    data = request.get_json()
    name = data['name']
    query = f"UPDATE facility SET name = '{name}' WHERE id = {id};"
    execute_read_query(conn, query)
    return jsonify({'message': 'Facility updated successfully', 'id': id, 'name': name})

#Delete Facility
@app.route('/api/facility/<int:id>', methods=['DELETE'])
def delete_facility(id):
    query = f"DELETE FROM facility WHERE id = {id};"
    execute_read_query(conn, query)
    return jsonify({'message': 'Facility deleted successfully', 'id': id})

# Add a Classroom
@app.route('/api/classroom', methods=['POST'])
def add_classroom():
    data = request.get_json()
    name = data['name']
    capacity = data['capacity']
    facility_id = data['facility']
    query = """
    INSERT INTO classroom (name, capacity, facility_id) 
    VALUES (%s, %s, %s);
    """
    execute_query(conn, query, (name, capacity, facility_id))
    return jsonify({'message': 'Classroom added successfully', 'name': name, 'capacity': capacity, 'facility': facility_id})

# Get All Classrooms
@app.route('/api/classroom', methods=['GET'])
def get_classrooms():
    query = "SELECT * FROM classroom;"
    classrooms = execute_read_query(conn, query)
    return jsonify(classrooms)

# Get Single Classroom
@app.route('/api/classroom/<int:id>', methods=['GET'])
def get_classroom(id):
    query = f"SELECT * FROM classroom WHERE id = {id};"
    classroom = execute_read_query(conn, query)
    return jsonify(classroom)

# Update a Classroom
@app.route('/api/classroom/<int:id>', methods=['PUT'])
def update_classroom(id):
    data = request.get_json()
    name = data['name']
    capacity = data['capacity']
    facility_id = data['facility']
    query = """
    UPDATE classroom 
    SET name = %s, capacity = %s, facility_id = %s 
    WHERE id = %s;
    """
    execute_query(conn, query, (name, capacity, facility_id, id))
    return jsonify({'message': 'Classroom updated successfully', 'id': id, 'name': name, 'capacity': capacity, 'facility': facility_id})

# Delete a Classroom
@app.route('/api/classroom/<int:id>', methods=['DELETE'])
def delete_classroom(id):
    query = f"DELETE FROM classroom WHERE id = {id};"
    execute_read_query(conn, query)
    return jsonify({'message': 'Classroom deleted successfully', 'id': id})


# Create a new teacher
@app.route('/api/teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    room_id = data['room_id']
    query = """
    INSERT INTO teacher (firstname, lastname, room_id) 
    VALUES (%s, %s, %s);
    """
    execute_query(conn, query, (firstname, lastname, room_id))
    return jsonify({'message': 'Teacher added successfully'})

# Get all teachers
@app.route('/api/teacher', methods=['GET'])
def get_teachers():
    query = "SELECT * FROM teacher;"
    teachers = execute_read_query(conn, query)
    return jsonify(teachers)

# Get a single teacher by id
@app.route('/api/teacher/<int:id>', methods=['GET'])
def get_teacher(id):
    query = f"SELECT * FROM teacher WHERE id = {id};"
    teacher = execute_read_query(conn, query)
    return jsonify(teacher)

# Update a teacher
@app.route('/api/teacher/<int:id>', methods=['PUT'])
def update_teacher(id):
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    room_id = data.get('room_id')
    query = """
    UPDATE teacher
    SET firstname = %s, lastname = %s, room_id = %s
    WHERE id = %s;
    """
    execute_query(conn, query, (firstname, lastname, room_id, id))
    return jsonify({'message': 'Teacher updated successfully'})

# Delete a teacher
@app.route('/api/teacher/<int:id>', methods=['DELETE'])
def delete_teacher(id):
    query = "DELETE FROM teacher WHERE id = %s;"
    execute_query(conn, query, (id,))
    return jsonify({'message': 'Teacher deleted successfully'})


# Create a new child
@app.route('/api/child', methods=['POST'])
def add_child():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    age = data['age']
    room_id = data['room_id']
    query = """
    INSERT INTO child (firstname, lastname, age, room_id) 
    VALUES (%s, %s, %s, %s);
    """
    execute_query(conn, query, (firstname, lastname, age, room_id))
    return jsonify({'message': 'Child added successfully'})

# Get all children
@app.route('/api/child', methods=['GET'])
def get_children():
    query = "SELECT * FROM child;"
    children = execute_read_query(conn, query)
    return jsonify(children)

# Get a single child by id
@app.route('/api/child/<int:id>', methods=['GET'])
def get_child(id):
    query = f"SELECT * FROM child WHERE id = {id};"
    child = execute_read_query(conn, query)
    return jsonify(child)


# Update a child
@app.route('/api/child/<int:id>', methods=['PUT'])
def update_child(id):
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    age = data.get('age')
    room_id = data.get('room_id')
    query = """
    UPDATE child
    SET firstname = %s, lastname = %s, age = %s, room_id = %s
    WHERE id = %s;
    """
    execute_query(conn, query, (firstname, lastname, age, room_id, id))
    return jsonify({'message': 'Child updated successfully'})

# Delete a child
@app.route('/api/child/<int:id>', methods=['DELETE'])
def delete_child(id):
    query = "DELETE FROM child WHERE id = %s;"
    execute_query(conn, query, (id,))
    return jsonify({'message': 'Child deleted successfully'})

@app.route('/api/login', methods=['POST'])
def login():
    # username and password required to login
    USERNAME = 'admin'
    PASSWORD = 'leilawashere'

    # Get username and password from the user
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')

    # Check if the provided credentials match the configured username and password
    if username == USERNAME and password == PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True)



app.run() 