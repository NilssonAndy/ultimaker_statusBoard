#!/usr/bin/env python
from threading import Lock
from flask import Flask, json, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import requests
from time import time, sleep

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.


async_mode = None



app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode=async_mode)

thread = None

thread_lock = Lock()




def background_thread():
    while True:
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        socketio.sleep(3)
        r = requests.get("http://192.168.50.203/api/v1/print_job/name")
        if r.status_code == 404:
            s3name = "No print running"
            #print(s3name)
            socketio.emit('my_response',
              {'data': 'data', 's3name': s3name})

        if r.status_code == 200:
            s3name = r.text
            s3name = s3name.strip('"')
            #print(s3name)
            socketio.emit('my_response',
              {'data': 'data', 's3name': s3name})

            socketio.sleep(3)
        r1 = requests.get("http://192.168.50.203/api/v1/print_job/time_elapsed")
        s3time_elapsed = r1.text
        #print(s3time_elapsed)

        r2 = requests.get("http://192.168.50.203/api/v1/print_job/time_total")
        s3time_total = r2.text
        #print(s3time_total)
        if r1.status_code and r2.status_code == 404:
            s3time_left = 0
            #print(s3time_left)
        if r1.status_code and r2.status_code == 200:
            
            s3time_left = int(s3time_total) - int(s3time_elapsed)
            #print(s3time_left)
            #print(r1.status_code, r2.status_code)

            time = float(s3time_left)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            #print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
            
            time_left_now = ("%d:%d:%d:%d" % (day, hour, minutes, seconds) )
            #print(time_left_now)

            socketio.emit('my_response1',
                {'data': 'data', 'time_left_now': time_left_now})
        
            socketio.sleep(3)
        r3 = requests.get("http://192.168.50.203/api/v1/print_job/time_elapsed")
        s3state1 = r1.text
        if r3.status_code == 404:
            s3state1 = "Ready"
            print(s3state1)

        if r3.status_code == 200:
            s3state1 = "Printer Is Running"
            print(s3state1)
        socketio.emit('my_response2',
            {'data': 'data', 's3state1': s3state1})


        
        socketio.sleep(3)
        r = requests.get("http://192.168.50.203/api/v1/print_job/name")
        if r.status_code == 404:
            s3name = "No print running"
            #print(s3name)
            socketio.emit('my_response',
              {'data': 'data', 's3name': s3name})

        if r.status_code == 200:
            s3name = r.text
            s3name = s3name.strip('"')
            #print(s3name)
            socketio.emit('my_response',
              {'data': 'data', 's3name': s3name})

            socketio.sleep(3)
        r1 = requests.get("http://192.168.50.203/api/v1/print_job/time_elapsed")
        s3time_elapsed = r1.text
        #print(s3time_elapsed)

        r2 = requests.get("http://192.168.50.203/api/v1/print_job/time_total")
        s3time_total = r2.text
        #print(s3time_total)
        if r1.status_code and r2.status_code == 404:
            s3time_left = 0
            #print(s3time_left)
        if r1.status_code and r2.status_code == 200:
            
            s3time_left = int(s3time_total) - int(s3time_elapsed)
            #print(s3time_left)
            #print(r1.status_code, r2.status_code)

            time = float(s3time_left)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            #print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
            
            time_left_now = ("%d:%d:%d:%d" % (day, hour, minutes, seconds) )
            #print(time_left_now)

            socketio.emit('my_response1',
                {'data': 'data', 'time_left_now': time_left_now})
        
            socketio.sleep(3)
        r3 = requests.get("http://192.168.50.203/api/v1/print_job/time_elapsed")
        s3state1 = r1.text
        if r3.status_code == 404:
            s3state1 = "Ready"
            print(s3state1)

        if r3.status_code == 200:
            s3state1 = "Printer Is Running"
            print(s3state1)
        socketio.emit('my_response2',
            {'data': 'data', 's3state1': s3state1})
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1


        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2

        socketio.sleep(3)
        r4 = requests.get("http://192.168.50.204/api/v1/print_job/name")
        if r4.status_code == 404:
            s3name2 = "No print running"
            #print(s3name2)
            socketio.emit('my_response3',
              {'data': 'data', 's3name2': s3name2})

        if r4.status_code == 200:
            s3name2 = r4.text
            s3name2 = s3name2.strip('"')
            #print(s3name2)
            socketio.emit('my_response3',
              {'data': 'data', 's3name2': s3name2})

            socketio.sleep(3)
        r5 = requests.get("http://192.168.50.204/api/v1/print_job/time_elapsed")
        s3time2_elapsed = r5.text
        #print(s3time2_elapsed)

        r6 = requests.get("http://192.168.50.204/api/v1/print_job/time_total")
        s3time2_total = r6.text
        #print(s3time2_total)
        if r5.status_code and r6.status_code == 404:
            s3time2_left = 0
            #print(s3time2_left)
        if r5.status_code and r6.status_code == 200:
            
            s3time2_left = int(s3time2_total) - int(s3time2_elapsed)
            #print(s3time2_left)
            #print(r5.status_code, r6.status_code)

            time2 = float(s3time2_left)
            day2 = time2 // (24 * 3600)
            time2 = time2 % (24 * 3600)
            hour2 = time2 // 3600
            time2 %= 3600
            minutes2 = time2 // 60
            time2 %= 60
            seconds2 = time2
            #print("d:h:m:s-> %d:%d:%d:%d" % (day2, hour2, minutes2, seconds2))
            
            time_left_now2 = ("%d:%d:%d:%d" % (day2, hour2, minutes2, seconds2) )
            #print(time_left_now2)

            socketio.emit('my_response4',
                {'data': 'data', 'time_left_now2': time_left_now2})
        
            socketio.sleep(3)
        r7 = requests.get("http://192.168.50.204/api/v1/print_job/time_elapsed")
        s3state2 = r5.text
        if r7.status_code == 404:
            s3state2 = "Ready"
            print(s3state2)

        if r7.status_code == 200:
            s3state2 = "Printer Is Running"
            print(s3state2)
        socketio.emit('my_response5',
            {'data': 'data', 's3state2': s3state2})


        
        socketio.sleep(3)
        r8 = requests.get("http://192.168.50.204/api/v1/print_job/name")
        if r8.status_code == 404:
            s3name2 = "No print running"
            #print(s3name)
            socketio.emit('my_response3',
              {'data': 'data', 's3name2': s3name2})

        if r8.status_code == 200:
            s3name2 = r8.text
            s3name2 = s3name2.strip('"')
            #print(s3name2)
            socketio.emit('my_response3',
              {'data': 'data', 's3name2': s3name2})

            socketio.sleep(3)
        r9 = requests.get("http://192.168.50.204/api/v1/print_job/time_elapsed")
        s3time2_elapsed = r9.text
        #print(s3time2_elapsed)

        r10 = requests.get("http://192.168.50.204/api/v1/print_job/time_total")
        s3time_total = r2.text
        #print(s3time2_total)
        if r10.status_code and r9.status_code == 404:
            s3time2_left = 0
            #print(s3time2_left)
        if r10.status_code and r9.status_code == 200:
            
            s3time2_left = int(s3time2_total) - int(s3time2_elapsed)
            #print(s3time2_left)
            #print(r10.status_code, r9.status_code)

            time3 = float(s3time2_left)
            day3 = time3 // (24 * 3600)
            time3 = time3 % (24 * 3600)
            hour3 = time3 // 3600
            time3 %= 3600
            minutes3 = time3 // 60
            time3 %= 60
            seconds3 = time3
            #print("d:h:m:s-> %d:%d:%d:%d" % (day3, hour3, minutes3, seconds3))
            
            time_left_now3 = ("%d:%d:%d:%d" % (day3, hour3, minutes3, seconds3) )
            #print(time3_left_now)

            socketio.emit('my_response6',
                {'data': 'data', 'time_left_now3': time_left_now3})
        
            socketio.sleep(3)
        r7 = requests.get("http://192.168.50.204/api/v1/print_job/time_elapsed")
        s3state2 = r7.text
        if r7.status_code == 404:
            s3state2 = "Ready"
            print(s3state2)

        if r7.status_code == 200:
            s3state2 = "Printer Is Running"
            print(s3state2)
        socketio.emit('my_response7',
            {'data': 'data', 's3state2': s3state2})

        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)




@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})



if __name__ == '__main__':
    socketio.run(app, debug=True)
