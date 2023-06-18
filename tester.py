import openai
import os
import subprocess

# Please replace `your-openai-api-key` with your own OpenAI API key
openai.api_key = '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'
engine = "gpt-4"
max_token = 500
def generate_code_from_prompt(prompt, human:str=""):
    
    response = openai.ChatCompletion.create(
      model=engine,
      messages=[{"role":"user","content":f"Only return python code to this problem with proper indentation and do not include any test suite in the output if given: {prompt}\nPython script:"}],
      temperature=0.5,
      max_tokens=max_token
    )
    return response["choices"][0]["message"]["content"].replace(" ```python","")

def generate_test_cases_from_prompt(prompt, human:str=""):
    
    response = openai.ChatCompletion.create(
      model=engine,
      messages=[{"role":"user","content":f"{prompt}\nOnly write the Python test case code that will validate if the function works and write a main function that will run the test suite when run as the file:"}],
      temperature=0.5,
      max_tokens=max_token
    )
    return response["choices"][0]["message"]["content"].replace(" ```python","")

def lmm_engine(prompt, human:str=""):
    response = openai.ChatCompletion.create(
      model=engine,
      messages=[{"role":"user","content":prompt}],
      temperature=0.5,
      max_tokens=max_token
    )


    return response["choices"][0]["message"]["content"].replace(" ```python","")

def write_code_to_file(code, filename):
    with open(filename, 'w') as f:
        f.write(code)

def run_code(filename):
    process = subprocess.Popen(['python', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the subprocess to finish and get the output
    stdout, stderr = process.communicate()

    # Print the output
    # print("Standard Output:")
    # print(stdout.decode())

    # print("Standard Error:")
    # print(stderr.decode())

    return stderr.decode()
def code_loop(new_prompt:str = "", og_prompt:str="", error: str = "", loop:int = 0, title:str="", feedback:str=""):
    loop += 1
    print(f"loop: {loop}")
    if new_prompt and not error:
        print("The code and test cases ran successfully!")
        print(new_prompt)
        print("--------------------")
        inp = input("Does this code work? (y/n): ")
        if inp == "y":
            print("Great! Your code is ready to submit!")
            return
        elif inp == "n":
            print("Please enter the feedback you would like to give to the AI")
            feedback = input("Feedback: ")
            code_loop(new_prompt, og_prompt, error, loop, title, feedback)
    elif new_prompt == "":
        # og_prompt = input("Enter a task: ")  # User input for the task
        og_prompt = "reverse a linked list"
        prompt = og_prompt
        title = lmm_engine(f"Create a short python file name with the file extension for this task: {og_prompt}")
        code = generate_code_from_prompt(prompt)
        print("Generated code:\n", code)
        test_prompt = f"The prompt: {prompt} \n The code: {code}"
        test_cases = generate_test_cases_from_prompt(test_prompt)
        print("Generated test cases:\n", test_cases)

        # Write both the code and test cases to the same file
        write_code_to_file(code, f'{title}')
        write_code_to_file(test_cases, 'test.py')
        test_str = f"{code} \n{test_cases}"
        write_code_to_file(test_str, 'checker.py')
        print("Running the code and test cases...")
        error = run_code("checker.py")
        code_loop(test_str, og_prompt, error, loop, title)
    else:
        prompt = f"previous code with the test suite: {new_prompt} \n error output: {error}"
        code_prompt = f"{prompt} \nWrite new code to fix the error"
        code = generate_code_from_prompt(code_prompt)
        test_prompt = f"The prompt: {og_prompt} \n The code: {code}"
        test_cases = generate_test_cases_from_prompt(test_prompt)
        write_code_to_file(code, f'{title}')
        write_code_to_file(test_cases, 'test.py')
        test_str = f"{code} \n{test_cases}"
        write_code_to_file(test_str, 'checker.py')
        error = run_code("checker.py")

        print("---start---")
        print(code_prompt)
        print("-----")
        print(code)
        print("-----")
        print(test_cases)
        print("-----")
        print(test_str)
        print("-----")
        print(error)
        print("======")
        code_loop(test_str, og_prompt, error, loop, title)




if __name__ == "__main__":
    code_loop("")
    # process = subprocess.Popen(['python', '-c', 'print(5)'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()

    # print("Standard Output:")
    # print(stdout.decode())

    # print("Standard Error:")
    # print(repr(stderr.decode()))