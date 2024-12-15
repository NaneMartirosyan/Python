from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'cars.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def get_next_id():
    data = load_data()
    if data:
        return max(car['id'] for car in data) + 1
    return 1

@app.route('/cars', methods=['GET'])
def get_cars():
    data = load_data()
    return jsonify(data)

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    data = load_data()
    car = next((car for car in data if car['id'] == car_id), None)
    if car is None:
        return jsonify({'message': 'Car not found'}), 404
    return jsonify(car)

@app.route('/cars', methods=['POST'])
def create_car():
    data = load_data()
    new_car = request.json
    new_car['id'] = get_next_id()
    data.append(new_car)
    save_data(data)
    return jsonify(new_car), 201

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = load_data()
    car = next((car for car in data if car['id'] == car_id), None)
    if car is None:
        return jsonify({'message': 'Car not found'}), 404
    car.update(request.json)
    save_data(data)
    return jsonify(car)

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    data = load_data()
    car = next((car for car in data if car['id'] == car_id), None)
    if car is None:
        return jsonify({'message': 'Car not found'}), 404
    data.remove(car)
    save_data(data)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
