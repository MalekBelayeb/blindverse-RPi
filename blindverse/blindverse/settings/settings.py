import json

def get_settings():
    a_file = open("/home/pi/Desktop/blindverse-RPi/blindverse/blindverse/settings/settings.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    return json_object

def update_lang(lang):
    json_object = get_settings()
    json_object["default_lang"] = lang
    a_file = open("/home/pi/Desktop/blindverse-RPi/blindverse/blindverse/settings/settings.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def get_lang():
    try:
        settings = get_settings()
        return settings["default_lang"]
    except: 
        return "en"




