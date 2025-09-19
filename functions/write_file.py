import os
from google.genai import types

def write_file(working_directory, file_path, content):
  try:
    
    root_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (target_abs == root_abs or target_abs.startswith(root_abs + os.sep)):
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    with open(target_abs, "w") as f:
      file_content_string = f.write(content)
      
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
  except Exception as e:
    return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=(
        "Writes the given text content to a file inside the permitted working directory. "
        "If the file does not exist, it is created; existing content is overwritten."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "Path to the file relative to the working directory. "
                    "Must resolve inside the permitted working directory."
                ),
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write into the file. Existing data will be replaced.",
            ),
        },
        required=["file_path", "content"],
    ),
)
