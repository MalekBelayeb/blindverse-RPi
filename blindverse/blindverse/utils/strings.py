import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')

from blindverse.settings.settings import get_lang

welcome_text_en = "Welcome to blindverse, please wait while data is loading"
welcome_text_fr = "Bienvenue dans blindverse, veuillez patienter pendant le chargement des données"

data_loaded_en = "Data loaded successfully, Please select your mode:"
data_loaded_fr = "Données chargées avec succès, veuillez sélectionner votre mode:"

selected_mode_money_en = "Mode money detection is selected"
selected_mode_money_fr = "Mode détection d'argent est sélectionné"

selected_mode_product_en = "Mode product detection is selected"
selected_mode_product_fr = "Mode détection de produit est sélectionné"

selected_mode_scene_en = "Mode scene description is selected"
selected_mode_scene_fr = "Mode description de scene est sélectionnée"

selected_mode_question_en = "Mode visual question answering is selected"
selected_mode_question_fr = "Mode question et réponse visuelle est sélectionné"


confirmed_mode_money_en = "Confirmed mode money detection"
confirmed_mode_money_fr = "Mode détection d'argent est confirmé"

confirmed_mode_product_en = "Confirmed mode product detection"
confirmed_mode_product_fr = "Mode détection de produit est confirmé"

confirmed_mode_scene_en = "confirmed mode scene description"
confirmed_mode_scene_fr = "Mode description de scene est confirmé"

confirmed_mode_question_en = "confirmed mode visual question answering "
confirmed_mode_question_fr = "Mode question et réponse visuelle est confirmé"

start_recording_msg_en = "You have 6 seconds to record"
start_recording_msg_fr = "Vous avez 6 secondes pour enregistrer"


your_question_en = "Your question"
your_question_fr = "Votre question"


#======================================================#

welcome_text = welcome_text_fr if get_lang() == 'fr' else welcome_text_en 

data_loaded = data_loaded_fr if get_lang() == "fr" else data_loaded_en

selected_mode_money = selected_mode_money_fr if get_lang() == "fr" else selected_mode_money_en
selected_mode_product = selected_mode_product_fr if get_lang() == "fr" else selected_mode_product_en
selected_mode_scene = selected_mode_scene_fr if get_lang() == "fr" else selected_mode_scene_en
selected_mode_question = selected_mode_question_fr if get_lang() == "fr" else selected_mode_question_en

confirmed_mode_money = confirmed_mode_money_fr if get_lang() == "fr" else confirmed_mode_money_en
confirmed_mode_product = confirmed_mode_product_fr if get_lang() == "fr" else confirmed_mode_product_en
confirmed_mode_scene = confirmed_mode_scene_fr if get_lang() == "fr" else confirmed_mode_scene_en
confirmed_mode_question = confirmed_mode_question_fr if get_lang() == "fr" else confirmed_mode_question_en

your_question = your_question_fr if get_lang() == "fr" else your_question_en

start_recording = start_recording_msg_fr if get_lang() == "fr" else start_recording_msg_en
