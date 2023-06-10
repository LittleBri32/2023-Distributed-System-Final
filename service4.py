from flask import Flask
from flask import request, render_template, redirect
import os
import requests
import socket
import sys
import mysql.connector
import time

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

class ticketRecord:
    def __init__(self, phone_num, show_name, ticket_num, ticket_price, total_price, order_date):
        self.phone_num = phone_num
        self.show_name = show_name
        self.ticket_num = ticket_num
        self.ticket_price = ticket_price
        self.total_price = total_price
        self.order_date = order_date

ticketRecordArray = []

@app.route('/service/<service_number>', methods=['POST','GET'])
def place(service_number):
    if request.method =='POST':
        if request.values['book']=='More':
            return render_template('index4.html', 
                                   ticketPrice=request.values['ticketPrice'], 
                                   ticketName=request.values['ticketName'], 
                                   ticketDate=request.values['ticketDate'])

        elif request.values['book']=='BUY':
            '''
            CREATE TABLE ticket_order(
                ticket_id INT PRIMARY KEY AUTO_INCREMENT,
                phone_num INT NOT NULL,
                show_name VARCHAR(64) NOT NULL,
                ticket_num INT NOT NULL,
                ticket_price INT NOT NULL,
                total_price INT NOT NULL,
                order_date DATE NOT NULL
            );
            '''
            record = ticketRecord(request.values['phoneNum'], 
                                  request.values['ticketName'], 
                                  request.values['ticketNum'],
                                  request.values['ticketPrice'],
                                  request.values['totalPrice'],
                                  time.strftime('%Y-%m-%d %H:%M:%S')
                                )
            app.logger.info('Date Time: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
            ##########db test##########

            config = {
                'user': 'root',
                'password': 'secret',
                'host': 'mysql-server',
                'database': 'ds_prj'
            }
            
            # build connection to mysql
            db = mysql.connector.connect( **config )
            
            cursor = db.cursor()
            
            # insert query
            """ insert_query = ("INSERT INTO ds_prj.ticket_order "
                            "(Name, phoneNum, order_date) "
                            "VALUES (%s, %s, %s)") """
            
            insert_query = ("INSERT INTO ds_prj.ticket_order"
                            "(phone_num, show_name, ticket_num, ticket_price, total_price, order_date)"
                            "VALUES (%s, %s, %s, %s, %s, %s)")
            
            # test data
            data = (record.phone_num, record.show_name, record.ticket_num, record.ticket_price, record.total_price, record.order_date)
            
            cursor.execute(insert_query, data)
            
            db.commit()
            
            cursor.close()
            db.close()

            ##########db test##########
            return redirect('http://localhost:8080/service/3', code = "302")
    return render_template('index4.html',status="")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
