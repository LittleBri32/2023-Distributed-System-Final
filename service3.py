from flask import Flask
from flask import request, render_template, redirect
import os
import requests
import socket
import sys

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
    def __init__(self, ticketName, ticketPrice, ticketDate):
        self.ticketName = ticketName
        self.ticketPrice = ticketPrice
        self.ticketDate = ticketDate

reservationArray = []

@app.route('/service/<service_number>', methods=['POST','GET'])
def hello(service_number):
    app.logger.info('method: {}'.format(request.method))
    if request.method =='POST':
        if request.values['book']=='More':
            app.logger.info('ticketName: {}'.format(request.values['ticketName']))
            app.logger.info('ticketPrice: {}'.format(request.values['ticketPrice']))
            app.logger.info('ticketDate: {}'.format(request.values['ticketDate']))
            reservation = Reservation(request.values['ticketName'], request.values['ticketPrice'], request.values['ticketDate'])
           
            reservationArray.append(reservation)
            
            return redirect('http://localhost:8080/service/4', code = "307")
    return render_template('index3.html',service=os.environ['SERVICE_NAME'],hostnameOne=socket.gethostname(),hostnameTwo=socket.gethostbyname(socket.gethostname()))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
