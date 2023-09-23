#!/usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import boto3

translate = boto3.client('translate', aws_access_key_id="AKIAZMFRY4**********", aws_secret_access_key="PF8mVLJ7H871SHIBRwbsjr*************", region_name="ap-south-1")
print(translate)

form = cgi.FieldStorage()
source_lang = form.getvalue('source_lang', 'en')
target_lang = form.getvalue('target_lang', 'hi')

text_to_translate = form.getvalue('text_to_translate', '')

if text_to_translate:
    response = translate.translate_text(
        Text=text_to_translate,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    translated_text = response['TranslatedText']
else:
    translated_text = "No text to translate."

print("<html>")
print("<head><title>Translation Result</title></head>")
print("<body>")
print("<h1>Translation Result</h1>")
print("<p><strong>Source Language:</strong> {}</p>".format(source_lang))
                                                                         
print("<p><strong>Target Language:</strong> {}</p>".format(target_lang))
print("<p><strong>Original Text:</strong> {}</p>".format(text_to_translate))
print("<p><strong>Translated Text:</strong> {}</p>".format(translated_text))
print("</body>")
print("</html>")
