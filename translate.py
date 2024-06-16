from googletrans import Translator, LANGUAGES
import re

# Function to translate text to English, handling mixed languages
def translate_mixed_languages_to_english(text):
    translator = Translator()

    # Split the text into segments based on language
    segments = re.split(r'(?<=\.)\s+', text)  # Split by sentences (assuming sentences end with periods)

    translated_text = []

    for segment in segments:
        if not segment.strip():
            continue
        try:
            detected_lang = translator.detect(segment)
            if detected_lang.lang != 'en':  # Only translate non-English segments
                translated_segment = translator.translate(segment, src=detected_lang.lang, dest='en').text
                translated_text.append(translated_segment)
            else:
                translated_text.append(segment)  # Append as-is if already in English
        except:
            continue

    return ' '.join(translated_text)

# Example usage
if __name__ == '__main__':
    text_to_translate = """
    Apple Inc. est une entreprise américaine multinationale spécialisée dans la technologie et l'informatique. 
    Das Unternehmen wurde 1976 von Steve Jobs, Steve Wozniak und Ronald Wayne gegründet. 
    It is known for its flagship products such as the iPhone, iPad, and MacBook Pro. 
    L'action d'Apple a récemment atteint un nouveau sommet historique à la bourse de New York. 
    Die Aktienkurse haben sich seit dem letzten Quartal verdoppelt, was zu einem Anstieg der Marktkapitalisierung geführt hat. 
    Le prix de l'action a également attiré l'attention des investisseurs internationaux.
    """
    
    translated_text = translate_mixed_languages_to_english(text_to_translate)
    print("Translated Text:")
    print(translated_text)
