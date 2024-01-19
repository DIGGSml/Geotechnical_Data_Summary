from lxml import etree
import xmlschema
import os

# Load the XML file
file_path = '/content/600304_20180702.xml'

# Parse the XML file
tree = etree.parse(file_path)
root = tree.getroot()

namespaces = {'diggs_geo': 'http://diggsml.org/schemas/2.5.a'}  # Replace with the actual URI


# Function to get all unique diggs_geo types
def get_unique_diggs_geo_types(root, namespaces):
    unique_types = set()
    for element in root.iter():
        # Ensure element.tag is a string before using startswith
        if isinstance(element.tag, str) and element.tag.startswith('{'+namespaces['diggs_geo']):
            unique_types.add(etree.QName(element).localname)
    return unique_types


# Extract and print unique diggs_geo types
unique_diggs_geo_types = get_unique_diggs_geo_types(root, namespaces)

# Initialize an empty list
diggs_geo_type_list = []

# Add each unique type to the list
for dtype in unique_diggs_geo_types:
    diggs_geo_type_list.append(dtype)

# Now, diggs_geo_type_list contains all unique diggs_geo types
print(diggs_geo_type_list)

# Convert both lists to sets
set_complex_type_names = set(complex_type_names)
set_diggs_geo_type_list = set(diggs_geo_type_list)

# Find common elements
common_values = set_complex_type_names.intersection(set_diggs_geo_type_list)

# Convert the result back to a list (optional)
common_values_list = list(common_values)

# Print common elements
print("Common elements between complex_type_names and diggs_geo_type_list:")
for val in common_values_list:
    print(val)


