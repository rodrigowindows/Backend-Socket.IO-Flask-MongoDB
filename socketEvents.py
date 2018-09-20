
from flask_socketio import SocketIO, join_room, leave_room, emit, disconnect
import json

def init(socketio):
    @socketio.on('connect')
    def connectIO():
        print("a user connected")

    @socketio.on('disconnect')
    def disconnectIO():
        print('a client disconnected')

    @socketio.on('join')# format: {"username":"Rodrigo","room":"providers"}
    def on_join(data):
        dataJson = json.loads(data)
        username = dataJson['username']
        room = dataJson['room']
        join_room(room)
        print(username + ' has entered the room: ' + room)

    @socketio.on('new') # format: {"username":"Rodrigo","room":"providers","message":"Hello everyone!"}
    def on_send(data):
        dataJson = json.loads(data)
        username = dataJson['username']
        message = dataJson['message']
        room = dataJson['room']
        emit(room, message)
        print(username + ' has sent message: '+ message + ' to the room: ' + room)

    @socketio.on('leave')
    def on_leave(data):
        dataJson = json.loads(data)
        username = dataJson['username']
        room = dataJson['room']
        leave_room(room)
        print(username + ' has left the room: ' + room)
        disconnect()