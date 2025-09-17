import os

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
