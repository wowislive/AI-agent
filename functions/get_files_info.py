import os
from google.genai import types


def get_files_info(working_directory, directory="."):
  try:
    
    root_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, directory))
    
    if not (target_abs == root_abs or target_abs.startswith(root_abs + os.sep)):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_abs):
      return f'Error: "{directory}" is not a directory'
    
    
    content = os.listdir(target_abs)
    
    result = ""
    
    for c in content:
      p = os.path.join(target_abs, c)
      size = os.path.getsize(p)
      is_file = os.path.isfile(p)
      result += f"- {c}: file_size={size} bytes, is_dir={is_file}" + "\n"
    
    return result
  
  except Exception as e:
    return f"Error: {e}"
  
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory relative to the working directory. Optional; defaults to '.'.",
            ),
        },
        required=[],
    ),
)
