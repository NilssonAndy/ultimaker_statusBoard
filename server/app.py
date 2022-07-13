#!/usr/bin/env python
from this import s
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


        #S3 NR 1 NAME
        socketio.sleep(3)
        nameRequestS3_1 = requests.get("http://192.168.../api/v1/print_job/name")
        if nameRequestS3_1.status_code == 404:
            s3name1 = " "
            #print(s3name)
            

        if nameRequestS3_1.status_code == 200:
            s3name1 = nameRequestS3_1.text
            s3name1 = s3name1.strip('"')
            #print(s3name1)
        socketio.emit('my_response1',
          {'data': 'data', 's3name1': s3name1})
        #S3 NR 1 NAME
        socketio.sleep(3)
        #S3 NR 1 STATE

        stateRequestS3_1 = requests.get("http://192.168.../api/v1/print_job/state")
        
        if stateRequestS3_1.status_code == 404:
            s3StateC1 = "Ready"
            
            

        if stateRequestS3_1.status_code == 200:
            s3State1 = stateRequestS3_1.text          
            s3State1 = s3State1.strip('"')
            s3State_1 = s3State1.replace("_"," ")
            
            
            
            

        
            s3StateC1 = ' '.join(elem.capitalize() for elem in s3State_1.split())
        socketio.emit('my_response2',
            {'data': 'data', 's3StateC1': s3StateC1})

        #S3 NR 1 STATE

        #S3 NR 1 TIME
        r_timeElapseS3_1 = requests.get("http://192.168.../api/v1/print_job/time_elapsed")
        s3time_elapsed_1 = r_timeElapseS3_1.text
        #print(s3time_elapsed)
        r_timeTotS3_1 = requests.get("http://192.168.../api/v1/print_job/time_total")
        s3time_total_1 = r_timeTotS3_1.text
        
        
       

        if r_timeElapseS3_1.status_code == 200:
            
            s3time_left_1 = int(s3time_total_1) - int(s3time_elapsed_1)
            

            time = float(s3time_left_1)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            
            #print("d:h:m-> %d:%d:%d:%d" % (day, hour, minutes))
            
            time_left_now1 = ("%d:%d:%d" % (day, hour, minutes) )

            
            
            if 'wait_cleanup' in stateRequestS3_1.text:
                time_left_now1 = " "

            if 'pre_print' in stateRequestS3_1.text:
                time_left_now1 = " "

            if 'none' in stateRequestS3_1.text:
                time_left_now1 = " "

            if 'wait_user_action' in stateRequestS3_1.text:
                time_left_now1 = " "
            
            if 'post_print' in stateRequestS3_1.text:
                time_left_now1 = " "

            socketio.emit('my_response3',
                {'data': 'data', 'time_left_now1': time_left_now1})

        #S3 NR 1 TIME


        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1
        #ULTIMAKER S3 NR1



        #################################

        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2


        #S3 NR 2 NAME
        socketio.sleep(3)
        nameRequestS3_2 = requests.get("http://192.168.../api/v1/print_job/name")
        if nameRequestS3_2.status_code == 404:
            s3name2 = " "
            #print(s3name)
            

        if nameRequestS3_2.status_code == 200:
            s3name2 = nameRequestS3_2.text
            s3name2 = s3name2.strip('"')
            #print(s3name1)
        socketio.emit('my_response4',
          {'data': 'data', 's3name2': s3name2})
        #S3 NR 2 NAME
        socketio.sleep(3)
        #S3 NR 2 STATE

        stateRequestS3_2 = requests.get("http://192.168.../api/v1/print_job/state")
        
        if stateRequestS3_2.status_code == 404:
            s3StateC2 = "Ready"
            
            

        if stateRequestS3_2.status_code == 200:
            s3State2 = stateRequestS3_2.text          
            s3State2 = s3State2.strip('"')
            s3State_2 = s3State2.replace("_"," ")
            
            
        
            s3StateC2 = ' '.join(elem.capitalize() for elem in s3State_2.split())
        socketio.emit('my_response5',
            {'data': 'data', 's3StateC2': s3StateC2})

        #S3 NR 2 STATE

        #S3 NR 2 TIME
        r_timeElapseS3_2 = requests.get("http://192.168.../api/v1/print_job/time_elapsed")
        s3time_elapsed_2 = r_timeElapseS3_2.text
        #print(s3time_elapsed)
        r_timeTotS3_2 = requests.get("http://192.168.../api/v1/print_job/time_total")
        s3time_total_2 = r_timeTotS3_2.text
        
        
       

        if r_timeElapseS3_2.status_code == 200:
            
            s3time_left_2 = int(s3time_total_2) - int(s3time_elapsed_2)
            
            time = float(s3time_left_2)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            
            #print("d:h:m-> %d:%d:%d:%d" % (day, hour, minutes))
            
            time_left_now2 = ("%d:%d:%d" % (day, hour, minutes) )

            
            
            if 'wait_cleanup' in stateRequestS3_2.text:
                time_left_now2 = " "

            if 'pre_print' in stateRequestS3_2.text:
                time_left_now2 = " "

            if 'none' in stateRequestS3_2.text:
                time_left_now2 = " "

            if 'wait_user_action' in stateRequestS3_2.text:
                time_left_now2 = " "
            
            if 'post_print' in stateRequestS3_2.text:
                time_left_now2 = " "

            socketio.emit('my_response6',
                {'data': 'data', 'time_left_now2': time_left_now2})

        #S3 NR 2 TIME


        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2
        #ULTIMAKER S3 NR2





         #################################

        #ULTIMAKER S3 NR3
        #ULTIMAKER S3 NR3
        #ULTIMAKER S3 NR3
        #ULTIMAKER S3 NR3


        #S3 NR 3 NAME
        socketio.sleep(3)
        nameRequestS3_3 = requests.get("http://192.168.../api/v1/print_job/name")
        if nameRequestS3_3.status_code == 404:
            s3name3 = " "
            
        if nameRequestS3_3.status_code == 200:
            s3name3 = nameRequestS3_3.text
            s3name3 = s3name3.strip('"')
            
        socketio.emit('my_response7',
          {'data': 'data', 's3name3': s3name3})
        #S3 NR 2 NAME
        socketio.sleep(3)
        #S3 NR 2 STATE

        stateRequestS3_3 = requests.get("http://192.168.../api/v1/print_job/state")
        
        if stateRequestS3_3.status_code == 404:
            s3StateC3 = "Ready"
            
            

        if stateRequestS3_3.status_code == 200:
            s3State3 = stateRequestS3_3.text          
            s3State3 = s3State3.strip('"')
            s3State_3 = s3State3.replace("_"," ")
            
            
        
            s3StateC3 = ' '.join(elem.capitalize() for elem in s3State_3.split())
        socketio.emit('my_response8',
            {'data': 'data', 's3StateC3': s3StateC3})

        #S3 NR 2 STATE

       
        #S3 NR 2 TIME
        r_timeElapseS3_3 = requests.get("http://192.168.../api/v1/print_job/time_elapsed")
        s3time_elapsed_3 = r_timeElapseS3_3.text
        
        r_timeTotS3_3 = requests.get("http://192.168.../api/v1/print_job/time_total")
        s3time_total_3 = r_timeTotS3_3.text
        
        
       

        if r_timeElapseS3_3.status_code == 200:
            
            s3time_left_3 = int(s3time_total_3) - int(s3time_elapsed_3)
            
            time = float(s3time_left_3)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            
            #print("d:h:m-> %d:%d:%d:%d" % (day, hour, minutes))
            
            time_left_now3 = ("%d:%d:%d" % (day, hour, minutes) )

            
            
            if 'wait_cleanup' in stateRequestS3_3.text:
                time_left_now3 = " "

            if 'pre_print' in stateRequestS3_3.text:
                time_left_now3 = " "

            if 'none' in stateRequestS3_3.text:
                time_left_now3 = " "

            if 'wait_user_action' in stateRequestS3_3.text:
                time_left_now3 = " "
            
            if 'post_print' in stateRequestS3_3.text:
                time_left_now3 = " "

            socketio.emit('my_response9',
                {'data': 'data', 'time_left_now3': time_left_now3})

        #S3 NR 3 TIME


        #ULTIMAKER S3 NR3
        #ULTIMAKER S3 NR3
        #ULTIMAKER S3 NR3
        #ULTIMAKER S3 NR3


                 #################################

        #ULTIMAKER S5 NR1
        #ULTIMAKER S5 NR1
        #ULTIMAKER S5 NR1
        #ULTIMAKER S5 NR1


        #S5 NR 1 NAME
        socketio.sleep(3)
        nameRequestS5_1 = requests.get("http://192.168.../api/v1/print_job/name")
        if nameRequestS5_1.status_code == 404:
            s5name1 = " "
            
        if nameRequestS5_1.status_code == 200:
            s5name1 = nameRequestS5_1.text
            s5name1 = s5name1.strip('"')
            
        socketio.emit('my_response10',
          {'data': 'data', 's5name1': s5name1})
        #S5 NR 1 NAME
        socketio.sleep(3)
        #S5 NR 1 STATE

        stateRequestS5_1 = requests.get("http://192.168.../api/v1/print_job/state")
        
        if stateRequestS5_1.status_code == 404:
            s5StateC1 = "Ready"
            
            

        if stateRequestS5_1.status_code == 200:
            s5State1 = stateRequestS5_1.text          
            s5State1 = s5State1.strip('"')
            s5State_1 = s5State1.replace("_"," ")
            
            
        
            s5StateC1 = ' '.join(elem.capitalize() for elem in s5State_1.split())
        socketio.emit('my_response11',
            {'data': 'data', 's5StateC1': s5StateC1})

        #S5 NR 1 STATE

        
        #S5 NR 1 TIME
        r_timeElapseS5_1 = requests.get("http://192.168.../api/v1/print_job/time_elapsed")
        s5time_elapsed_1 = r_timeElapseS5_1.text
      
        r_timeTotS5_1 = requests.get("http://192.168.../api/v1/print_job/time_total")
        s5time_total_1 = r_timeTotS5_1.text
        
        
       

        if r_timeElapseS5_1.status_code == 200:
            
            s5time_left_1 = int(s5time_total_1) - int(s5time_elapsed_1)
            
            time = float(s5time_left_1)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            
            #print("d:h:m-> %d:%d:%d:%d" % (day, hour, minutes))
            
            time_left_now4 = ("%d:%d:%d" % (day, hour, minutes) )

            
            
            if 'wait_cleanup' in stateRequestS5_1.text:
                time_left_now4 = " "

            if 'pre_print' in stateRequestS5_1.text:
                time_left_now4 = " "

            if 'none' in stateRequestS5_1.text:
                time_left_now4 = " "

            if 'wait_user_action' in stateRequestS5_1.text:
                time_left_now4 = " "
            
            if 'post_print' in stateRequestS5_1.text:
                time_left_now4 = " "

            socketio.emit('my_response12',
                {'data': 'data', 'time_left_now4': time_left_now4})

        #S5 NR 1 TIME


        #ULTIMAKER S5 NR1
        #ULTIMAKER S5 NR1
        #ULTIMAKER S5 NR1
        #ULTIMAKER S5 NR1



                 #################################

        #ULTIMAKER S5 NR2
        #ULTIMAKER S5 NR2
        #ULTIMAKER S5 NR2
        #ULTIMAKER S5 NR2


        #S5 NR 2 NAME
        socketio.sleep(3)
        nameRequestS5_2 = requests.get("http://192.168.../api/v1/print_job/name")
        if nameRequestS5_2.status_code == 404:
            s5name2 = " "
            
        if nameRequestS5_2.status_code == 200:
            s5name2 = nameRequestS5_2.text
            s5name2 = s5name2.strip('"')
            
        socketio.emit('my_response13',
          {'data': 'data', 's5name2': s5name2})
        #S5 NR 2 NAME
        socketio.sleep(3)
        #S5 NR 2 STATE

        stateRequestS5_2 = requests.get("http://192.168.../api/v1/print_job/state")
        
        if stateRequestS5_2.status_code == 404:
            s5StateC2 = "Ready"
            
            

        if stateRequestS5_2.status_code == 200:
            s5State2 = stateRequestS5_2.text          
            s5State2 = s5State2.strip('"')
            s5State_2 = s5State2.replace("_"," ")
            
            
        
            s5StateC2 = ' '.join(elem.capitalize() for elem in s5State_2.split())
        socketio.emit('my_response14',
            {'data': 'data', 's5StateC2': s5StateC2})

        #S5 NR 2 STATE

        
        #S5 NR 2 TIME
        r_timeElapseS5_2 = requests.get("http://192.168.../api/v1/print_job/time_elapsed")
        s5time_elapsed_2 = r_timeElapseS5_2.text
      
        r_timeTotS5_2 = requests.get("http://192.168.../api/v1/print_job/time_total")
        s5time_total_2 = r_timeTotS5_2.text
        
        
       

        if r_timeElapseS5_2.status_code == 200:
            
            s5time_left_2 = int(s5time_total_2) - int(s5time_elapsed_2)
            
                
            time = float(s5time_left_2)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            
            #print("d:h:m-> %d:%d:%d:%d" % (day, hour, minutes))
            
            time_left_now5 = ("%d:%d:%d" % (day, hour, minutes) )

            
            
            if 'wait_cleanup' in stateRequestS5_2.text:
                time_left_now5 = " "

            if 'pre_print' in stateRequestS5_2.text:
                time_left_now5 = " "

            if 'none' in stateRequestS5_2.text:
                time_left_now5 = " "

            if 'wait_user_action' in stateRequestS5_2.text:
                time_left_now5 = " "
            
            if 'post_print' in stateRequestS5_2.text:
                time_left_now5 = " "

            socketio.emit('my_response15',
                {'data': 'data', 'time_left_now5': time_left_now5})

        #S5 NR 2 TIME


        #ULTIMAKER S5 NR2
        #ULTIMAKER S5 NR2
        #ULTIMAKER S5 NR2
        #ULTIMAKER S5 NR2


        

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
    socketio.run(app, debug = True)
