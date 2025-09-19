import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
  try:
    
    root_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (target_abs == root_abs or target_abs.startswith(root_abs + os.sep)):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_abs):
      return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    with open(target_abs, "r") as f:
      file_content_string = f.read(MAX_CHARS+1)
      
      if len(file_content_string) > MAX_CHARS:
        file_content_string = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
      
      return file_content_string
    
  except Exception as e:
    return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=(
        "Reads and returns the text content of a file located within the permitted working "
        "directory. The content is truncated to MAX_CHARS characters if longer."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "Path to the file relative to the working directory. "
                    "Must resolve to a regular file inside the permitted working directory."
                ),
            ),
        },
        required=["file_path"],
    ),
)
