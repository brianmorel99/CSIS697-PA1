import xml.etree.ElementTree as ET


class Response:
    def __init__(self):
        self.stored = False
        self.note = ''
        
    def __str__(self):
        return f"Stored: {self.stored}, Note: {self.note}"

    def parse_XML_response(self, xml_string):

        root = ET.fromstring(xml_string)

        for res in root.iter("response"):
            self.stored = res.find("stored").text
            self.note = res.find("note").text
            
    def export_XML_response(self):
        response_xml = ET.Element('response')
        ET.SubElement(response_xml, "stored").text = self.stored
        ET.SubElement(response_xml, "note").text = self.note
        tree = ET.tostring(response_xml, xml_declaration=True)
        return tree
