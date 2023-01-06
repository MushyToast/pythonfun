import sys
import math
import time

def error(message):
    print(message)
    exit()
def run():
    getInput = False
    codeIndex = -1
    output = []
    stack = []
    skip = False
    while True:
        codeIndex += 1
        if codeIndex > (len(code)-1) or code[codeIndex] == "/output/":
            break
        if code[codeIndex] == "/input/":
            getInput = True
            continue
        elif code[codeIndex][0] == ".":
            command = code[codeIndex]
            readCommand = []
            readValue = []
            readingValue = False
            for char in command:
                if char == ".":
                    continue
                if char == "(":
                    readingValue = True
                    continue
                elif char == ")":
                    readingValue = False
                    continue
                elif readingValue == True:
                    readValue.append(char)
                    continue
                readCommand.append(char)
                if "".join(readCommand) == "pop":
                    stringCommand = readCommand
            command = "".join(readCommand)
            value = "".join(readValue)
            try:
                match command:
                    case "pop":
                        stack.pop(len(stack)-1)
                    case "zero":
                        stack.append(0)
                    case "increment":
                        stack[len(stack)-1] = stack[len(stack)-1]+1
                    case "decrement":
                        stack[len(stack)-1] = stack[len(stack)-1]-1
                    case "add":
                        num = stack[len(stack)-1] + stack[len(stack)-2]
                        stack.pop(len(stack)-1)
                        stack.pop(len(stack)-1)
                        stack.append(num)
                    case "debug":
                        if value == "outputBuffer":
                            print(output)
                        elif value == "currentStack":
                            print(stack)
                        else:
                            error(f"Error: \'{value}\' is not a valid value for command \'{command}\'")
                    case "multiply":
                        num = stack[len(stack)-1] * stack[len(stack)-2]
                        stack.pop(len(stack)-1)
                        stack.pop(len(stack)-1)
                        stack.append(num)
                    case "subtract":
                        num = stack[len(stack)-1] - stack[len(stack)-2]
                        stack.pop(len(stack)-1)
                        stack.pop(len(stack)-1)
                        stack.append(num)
                    case "divide":
                        num = math.floor(stack[len(stack)-1] / stack[len(stack)-2])
                        stack.pop(len(stack)-1)
                        stack.pop(len(stack)-1)
                        stack.append(num)
                    case "modulo":
                        num = math.floor(stack[len(stack)-1] % stack[len(stack)-2])
                        stack.pop(len(stack)-1)
                        stack.pop(len(stack)-1)
                        stack.append(num)
                    case "duplicate":
                        stack.append(stack[len(stack)-1])
                    case "swap":
                        value1 = stack[len(stack)-2]
                        value2 = stack[len(stack)-1]
                        stack[len(stack)-2] = value2
                        stack[len(stack)-1] = value1
                    case "over":
                        stack.append(stack[len(stack)-2])
                    case "reverse":
                        reverse = []
                        for i in range(len(stack)-1,-1,-1):
                            reverse.append(stack[i])
                        stack = reverse
                    case "length":
                        stack.append(len(stack))
                    case "print":
                        if value == "ascii":
                            output.append(chr(stack[len(stack)-1]))
                            stack.pop(len(stack)-1)
                        elif value == "number":
                            output.append(str(stack[len(stack)-1]))
                            stack.pop(len(stack)-1)
                        else:
                            error(f"Error: \'{value}\' is not a valid value for command \'{command}\'")
                    case "redirect":
                        try:
                            redirect = int(value)
                        except:
                            error(f"Error: Command \'{command}\' requires a numerical value")
                        if (codeIndex + redirect) > len(code) or (codeIndex + redirect) < 0:
                            error("Error: Redirect goes outside code length")
                        else:
                            if redirect >= 0:
                                redirect += 1
                            elif redirect < 0:
                                redirect -= 1
                            codeIndex = codeIndex + redirect
                    case "*redirect":
                        cond = stack[len(stack)-1]
                        stack.pop(len(stack)-1)
                        if cond == 1:
                            try:
                                redirect = int(value)
                            except:
                                error(f"Error: Command \'{command}\' requires a numerical value")
                            if (codeIndex + redirect) > len(code) or (codeIndex + redirect) < 0:
                                error("Error: Redirect goes outside code length")
                            else:
                                if redirect >= 0:
                                    redirect -= 1
                                elif redirect < 0:
                                    redirect += 1
                                codeIndex = codeIndex + redirect
                    case "equal":
                        value1 = stack[len(stack)-1]
                        value2 = stack[len(stack)-2]
                        stack.pop(len(stack)-1)
                        stack.pop(len(stack)-1)
                        if value1 == value2:
                            stack.append(1)
                        else:
                            stack.append(0)
                    case "not":
                        value1 = stack[len(stack)-1]
                        stack.pop(len(stack)-1)
                        if value1 == 0:
                            stack.append(1)
                        else:
                            stack.append(0)
                    case "wait":
                        try:
                            wait = int(value)
                        except:
                            error(f"Error: Command \'{command}\' requires a numerical value")
                        time.sleep(wait)
                    case default:
                        error(f"Error: Unknown command \'{command}\'")
            except IndexError:
                error(f"Error: Stack was not large enough for command \'{command}\' to function")
            continue
        elif getInput == True:
            getInput = False
            codeInput = code[codeIndex]
            codeInput = codeInput.split(" ")
            for Input in codeInput:
                try:
                    Input = int(Input)
                    stack.append(Input)
                except:
                    if Input == "args":
                        if len(sys.argv) > 2:
                            for arg in sys.argv[2:]:
                                arg = arg.strip("\n")
                                try:
                                    arg = int(arg)
                                except:
                                    error("Error: Inputs are not numbers and cannot be converted to numbers")
                                stack.append(arg)
            continue

    output = "".join(output)
    print(f"FINAL STACK: {stack}; FINAL OUTPUT: {output}")




if len(sys.argv) < 2:
    error("Use: python dotstack.py <file>")
else:
    file = open(sys.argv[1])

code = []

for line in file:
    if line.strip("\n") != "":
        line = line.split("::")
        if len(line) == 1:
            command = line[0]
            if "#" in command:
                comment = [*command]
                comment = comment[0 : command.index("#")]
                command = "".join(comment)
            if command.strip("\n").strip(" ") != "":
                code.append(command.strip("\n").strip(" "))
        else:
            if line[1].strip(" ") == "\n":
                code.append(line[0].strip("\n").strip(" "))
                error("Error: \'::\' is empty")
            for command in line:
                if "#" in command:
                    comment = [*command]
                    comment = comment[0 : command.index("#")]
                    command = "".join(comment)
                code.append(command.strip("\n").strip(" "))
if "/input/" in code:
    startIndex = code.index("/input/")
else:
    error("Error: Code does not contain \'/input/\'")
if "/output/" in code:
    endIndex = code.index("/output/")
else:
    error("Error: Code does not contain \'/output/\'")
if startIndex >= endIndex:
    error("Error: \'/input/\' must come before \'/output/\'")
code = code[startIndex : endIndex+1]
run()