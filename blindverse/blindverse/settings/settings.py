

import json

def get_lang():
    a_file = open("settings.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    return json_object

def update_lang(lang):
    json_object = get_lang()
    json_object["default_lang"] = lang
    a_file = open("settings.json", "w")
    json.dump(json_object, a_file)
    a_file.close()



update_lang("en")
