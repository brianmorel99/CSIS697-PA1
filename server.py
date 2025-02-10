import socket			 
import sqlite3
from patient import Patient
from response import Response

HOST = "127.0.0.1"
PORT = 10022

def main():
    dbconn = sqlite3.connect("diagnosis.db")
    cursor = dbconn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS diagnosis
                (patient_id INTEGER, patient_name TEXT, patient_age TEXT, patient_diagnosis TEXT)''')


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Listening on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            msg = conn.recv(1500)
            patient: Patient = Patient()
            patient.parse_XML_patient(msg.decode())
            print(f"Received record: {patient}")
            cursor.execute(f"INSERT INTO diagnosis VALUES ('{int(patient.patient_id)}','{patient.patient_name}','{patient.patient_age}','{patient.patient_diagnosis}')")
            response: Response = Response()
            response.stored = "True"
            response.note = "Made it trough"
            conn.send(response.export_XML_response()[:1500])
            conn.close()
    except KeyboardInterrupt:
        server.close()
        print("Closing Server Application")
        print("Final State of Database")
        for row in cursor.execute("SELECT * FROM diagnosis"):
            print(row)
        dbconn.close()

if __name__ == "__main__":
    main()
