from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
  functions_dict = {"get_files_info": get_files_info, "get_file_content": get_file_content,
                    "run_python_file": run_python_file, "write_file": write_file}
  
  all_args = dict(function_call_part.args or {})
  all_args["working_directory"] = "./calculator"
  if function_call_part.name == "run_python_file":
    all_args["args"] = all_args.get("args") or []
  
  
  if verbose:
    print(f"Calling function: {function_call_part.name}({all_args})")
  else:
    print(f" - Calling function: {function_call_part.name}")
    
  fn = functions_dict.get(function_call_part.name)
  
  if fn:
    function_result = fn(**all_args)
  else:
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Unknown function: {function_call_part.name}"},
            )
        ],
    )

  return types.Content(
      role="tool",
      parts=[
          types.Part.from_function_response(
              name=function_call_part.name,
              response={"result": function_result},
          )
      ],
  )
  