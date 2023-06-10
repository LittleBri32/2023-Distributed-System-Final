from flask import Flask
from flask import request, render_template
import os
import requests
import socket
import sys
import mysql.connector

app = Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id",

    # SkyWalking headers.
    "sw8"
]
class Reservation:
    def __init__(self, cel):
        self.cel = cel

reservationArray = []

@app.route('/service/<service_number>', methods=['POST','GET'])
def hello(service_number):
    
    if request.method =='POST':
            app.logger.info(request.values['phone-number'])
            reservation = Reservation(request.values['phone-number'])
            # build connection to mysql
            db = mysql.connector.connect(host="mysql-server", user="root", password="secret", database="ds_prj")
            
            cursor = db.cursor()

            query = "SELECT * FROM ticket_order WHERE phone_num = %s"
            
            data = reservation.cel

            cursor.execute(query, (data,))
            ticket_info = cursor.fetchall()
            db.commit()
            app.logger.info(ticket_info)
            cursor.close()
            db.close()
            if ticket_info:
                return render_template('index2.html', result = ticket_info)
            else:
                return render_template('index2.html', result = None)
    
    return render_template('index2.html', result = "")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)