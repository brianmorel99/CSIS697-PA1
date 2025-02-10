import xml.etree.ElementTree as ET


class Patient:
    def __init__(self):
        self.patient_id = 0
        self.patient_name = ''
        self.patient_age = 0
        self.patient_diagnosis = ''

    def __str__(self):
        return f"Paitent ID: {self.patient_id}, Patient Name: {self.patient_name}, Patient Age: {self.patient_age}, Patient Diagnosis: {self.patient_diagnosis}"

    def parse_XML_patient(self, xml_string):

        root = ET.fromstring(xml_string)

        for patient in root.iter("patient"):
            self.patient_id = patient.find("patient_id").text
            self.patient_name = patient.find("name").text
            self.patient_age = patient.find("age").text
            self.patient_diagnosis = patient.find("diagnosis").text

    def export_XML_patient(self):
        patient_xml = ET.Element('patient')
        ET.SubElement(patient_xml, "patient_id").text = self.patient_id
        ET.SubElement(patient_xml, "name").text = self.patient_name
        ET.SubElement(patient_xml, "age").text = self.patient_age
        ET.SubElement(patient_xml, "diagnosis").text = self.patient_diagnosis
        tree = ET.tostring(patient_xml, xml_declaration=True)
        return tree
