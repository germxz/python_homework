import traceback

try:
    first_prompt = True

    with open("diary.txt", "a") as file:
        while True:
            if first_prompt:
                entry = input("What happened today? ")
                first_prompt = False
            else:
                entry = input("What else? ")

            file.write(entry + "\n")

            if entry == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
import traceback

try:
    with open("diary.txt", "a") as file:
        first = True

        while True:
            if first:
                line = input("What happened today? ")
                first = False
            else:
                line = input("What else? ")

            file.write(line + "\n")

            if line == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []

    for trace in trace_back:
        stack_trace.append(
            f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Msg: {trace[3]}'
        )

    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {str(e)}")
    print(f"Stack trace: {stack_trace}")