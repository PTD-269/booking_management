from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from controller.BookingController import BookingController

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/bookings', methods=['GET', 'POST', 'DELETE'])
def get_bookings():
    if request.method == 'GET':
        bookings = BookingController.get_all_bookings()
        return jsonify(bookings)

    if request.method == 'POST':
        request_json = request.get_json()
        name = request_json['name']
        email = request_json['email']
        checkinDate = request_json['checkinDate']
        checkoutDate = request_json['checkoutDate']
        roomType = request_json['roomType']
        location = request_json['location']

        BookingController.create_booking(name, email, checkinDate, checkoutDate, roomType, location)
        return jsonify({'status': 'ok'})

@app.route('/bookings/<int:id>', methods=['DELETE'])
def delete_booking(id):
    BookingController.delete_booking(id)
    return jsonify({'status': 'ok'})
def run():
    app.run(debug=True, port=3667)

if __name__ == '__main__':
    run()