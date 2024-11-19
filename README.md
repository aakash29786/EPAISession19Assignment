# EPAISession19Assignment

In this assignment we created a class called SmartDevice with the following;

Attributes:
SmartDevice should have the following attributes:
device_name: The name of the device
model_number: The model number of the device
is_online: A boolean indicating if the device is currently online
status: A dictionary that stores the current status of various device features (e.g., battery level, temperature)

Methods:
update_status(attribute, value): Adds or updates a status attribute in the status dictionary
get_status(attribute): Returns the value of a specific status attribute. If the attribute does not exist, it should return 'Attribute not found'. 
toggle_online(): Changes the device's online status (is_online) to its opposite value
reset():L Resets all status attributes to their default values (i.e. clears the status dictionary)
Callable Class:
Make the SmartDevice class callable, such that calling an instance returns its device_name and model_number in a formatting string
Function Attributes:
Add a callable function attribute to the class named device_info which returns the current state of the device as a dictionary
