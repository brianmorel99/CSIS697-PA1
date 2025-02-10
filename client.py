import socket
from patient import Patient
from response import Response

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 10022  # The port used by the server      

def main():
    print("Welcome Patient Diagnosis Entry")
    patient: Patient = Patient()
    patient.patient_id = input("Please Enter Patient ID: ")
    patient.patient_name = input("Please Enter Patient Name: ")
    patient.patient_age = input("Please Enter Patient Age: ")
    patient.patient_diagnosis = input("Please Enter Patient Diagnosis: ")

    choice = input("Send the data to the server? (Y/n)")
    if choice.lower() == 'y':
        patient_xml = patient.export_XML_patient()
        print(f"Sending Patient Data as XML: {patient_xml.decode()}")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        client.send(patient_xml[:1500])
        message = client.recv(1500)
        response = Response()
        response.parse_XML_response(message.decode())
        print(f"The response from the server: Stored: {response.stored} , Note: {response.note}")
    else:
        print(f"Discarding Record: {patient} , GoodBye")


if __name__ == "__main__":
    main()
