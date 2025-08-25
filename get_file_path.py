# import json
# import sys

# if len(sys.argv) < 2:
#     print(json.dumps({"error": "No file path provided"}))
#     sys.exit(1)

# file_path = sys.argv[1]
# print(json.dumps({"file_path": file_path}))

# import os
# import json
# import sys

# # First argument from n8n
# file_path = sys.argv[1]  # e.g. C:/Users/Uday/Documents/files/2206.13491v1.docx

# # Get directory and filename
# directory = os.path.dirname(file_path)
# filename = os.path.basename(file_path)

# # Make absolute path
# absolute_path = os.path.abspath(file_path)

# # Output JSON so n8n can pass it to the next node
# output = {
#     "file_path": absolute_path,
#     "directory": directory,
#     "filename": filename
# }

# print(json.dumps(output))

# import os
# import sys
# import json

# # Get the full path from n8n argument
# full_path = sys.argv[1]
# print(f"Received file path: {full_path}")
# # Normalize for OS
# full_path = os.path.normpath(full_path)

# output = {
#     "file_path": full_path,
#     "directory": os.path.dirname(full_path),
#     "filename": os.path.basename(full_path)
# }

# print(json.dumps(output))


# import os
# import sys
# import json

# # Get the file path from argument
# full_path = sys.argv[1]

# # Normalize for Windows paths
# full_path = os.path.normpath(full_path)

# # Output only the absolute path as JSON
# print(json.dumps({"file_path": full_path}))

import os
import sys

# Get the file path from argument
full_path = sys.argv[1]

# Normalize for Windows paths
full_path = os.path.normpath(full_path)

# Print only the value (no JSON, no key)
print(full_path)






