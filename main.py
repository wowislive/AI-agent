import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

from config import SYSTEM_PROMPT

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    user_prompt = sys.argv[1]
    is_verbose = (len(sys.argv) >= 3 and sys.argv[2] == "--verbose")
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_write_file,
            schema_get_file_content,
            schema_run_python_file,
        ]
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ))
    
    if response.function_calls:
        for function_call_part in response.function_calls:
            result_of_call = call_function(function_call_part, is_verbose)
            res = result_of_call.parts[0].function_response.response
            if not res:
                raise Exception("Missing function response")
            
            print(f"-> {res['result']}")

    else:
        print(response.text)


if __name__ == "__main__":
    main()
