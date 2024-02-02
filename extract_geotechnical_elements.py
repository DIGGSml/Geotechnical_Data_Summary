!pip install xmlschema
from lxml import etree
import xmlschema
import os

# Load the XML file
file_path = '/content/Geosetta_29-01-2024-16-49-35_diggs.xml'
xsd_file_path= '/content/Geotechnical (1).xsd'


# Parse the XML file
tree = etree.parse(file_path)
root = tree.getroot()

namespaces = {'diggs_geo': 'http://diggsml.org/schemas/2.5.a'}  # Replace with the actual URI


# Function to get all unique diggs_geo types
def get_unique_diggs_geo_types(root, namespaces):
    unique_types = set()
    for element in root.iter():
        # Check if element.tag is a string
        if isinstance(element.tag, str) and element.tag.startswith('{'+namespaces['diggs_geo']):
            unique_types.add(etree.QName(element).localname)
    return unique_types

def extract_data_types(xsd_file_path, namespaces):
    ns = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    tree = etree.parse(xsd_file_path)
    root = tree.getroot()
    complex_types = root.findall('.//xs:complexType', namespaces=ns)
    complex_type_names = [type.get('name') for type in complex_types if type.get('name')]
    return complex_type_names

# Extract and print unique diggs_geo types
unique_diggs_geo_types = get_unique_diggs_geo_types(root, namespaces)

# Initialize an empty list
diggs_geo_type_list = []

# Add each unique type to the list
for dtype in unique_diggs_geo_types:
    diggs_geo_type_list.append(dtype)

# Now, diggs_geo_type_list contains all unique diggs_geo types



# Extract complex types from XSD
complex_type_names = extract_data_types(xsd_file_path, namespaces)



# Assuming complex_type_names is your original list
modified_complex_type_names = [name.rstrip('Type') if name.endswith('Type') else name for name in complex_type_names]

# Convert the modified list to a set
set_complex_type_names = set(modified_complex_type_names)

set_diggs_geo_type_list = set(diggs_geo_type_list)

print(set_complex_type_names)#.xsd file
print(set_diggs_geo_type_list)#.diggs file

# Find common elements
common_values = set_complex_type_names.intersection(set_diggs_geo_type_list)

# Convert the result back to a list (optional)
common_values_list = list(common_values)

# Print common elements
print("Common elements between complex_type_names and diggs_geo_type_list:")
for val in common_values_list:
    print(val)

