import os
import subprocess
import sys
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
  try:
    
    root_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (target_abs == root_abs or target_abs.startswith(root_abs + os.sep)):
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_abs):
      return f'Error: File "{file_path}" not found.'
    
    if not target_abs.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file.'
    
    completed_process = subprocess.run([sys.executable, target_abs, *args], timeout=30, capture_output=True, cwd=working_directory, text=True)
    
    if not completed_process.stdout and not completed_process.stderr:
      return "No output produced."
    
    result_lines = [f"STDOUT: {completed_process.stdout}",
                    f"STDERR: {completed_process.stderr}"]
    
    if not completed_process.returncode == 0:
      result_lines.append(f"Process exited with code {completed_process.returncode}")
    
    return "\n".join(result_lines)
    
  except Exception as e:
    return f"Error: executing Python file: {e}"
  
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a Python script inside the permitted working directory and returns its "
        "STDOUT, STDERR, and exit code information."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "Path to the Python (.py) file, relative to the working directory. "
                    "Must be located inside the permitted working directory."
                ),
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description=(
                    "Optional list of command-line arguments to pass to the script. "
                    "Defaults to an empty list."
                ),
            ),
        },
        required=["file_path"],
    ),
)
