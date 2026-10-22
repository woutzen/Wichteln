import base64

# Read the image and encode as data URI
with open('image.JPG', 'rb') as img_file:
    img_bytes = img_file.read()
    img_b64 = base64.b64encode(img_bytes).decode('ascii')
    data_uri = f'data:image/jpeg;base64,{img_b64}'

# Read the HTML file
with open('ui_standalone.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the image after the header
import re
html_new = re.sub(
    r'(<h1[^>]*>.*?</h1>)',
    r'\1\n    <img src="' + data_uri + '" alt="Bild" style="max-width:90vw; max-height:40vh; display:block; margin:2vw auto 4vw auto; border-radius:1vw; box-shadow:0 0 2vw #888;" />',
    html,
    count=1,
    flags=re.DOTALL
)

with open('ui_standalone.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

print('Image added as Data URI to ui_standalone.html')
