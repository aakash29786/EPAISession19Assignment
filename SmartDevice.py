class SmartDevice:

    device_count = 0

    def __init__(self, device_name, model_number, is_online = False):
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}
        SmartDevice.device_count += 1

    
    def update_status(self, attribute, value):
        setattr(SmartDevice, attribute, value)

    def get_status(self, attribute):
        if attribute in dir(SmartDevice):
            return getattr(SmartDevice, attribute)
        else:
            return "Attribute not found"        

    def toggle_online(self):
        if self.is_online:
            self.is_online = False
            return True 
        else:
            self.is_online = True
            return False
   
    def reset(self):
        return self.status == {}
    
    def __call__(self):
        return str (self.device_name + " (" + "Model: " + self.model_number + ")")
    
    def device_info(self):
        return True
