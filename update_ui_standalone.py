import json
import base64

# Load allocations from allocation_results.json
with open('allocation_results.json', encoding='utf-8') as f:
    allocations = json.load(f)

# Encode allocations as base64 JSON string
encoded = base64.b64encode(json.dumps(allocations, ensure_ascii=False).encode('utf-8')).decode('ascii')

# Read ui_standalone.html
with open('ui_standalone.html', encoding='utf-8') as f:
    html = f.read()

# Replace the encodedAllocations assignment in the HTML
import re
html_new = re.sub(
    r'(const encodedAllocations = ")([^"]*)(";)',
    f'\\1{encoded}\\3',
    html
)

# Write back to ui_standalone.html
with open('ui_standalone.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

print('Allocations updated in ui_standalone.html')
