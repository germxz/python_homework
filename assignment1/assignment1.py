# Write your code here.
def hello():
    return "Hello!"  

def greet(name):
    return f"Hello, {name}!"

def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                return "You can't divide by 0!"
            return a // b
        elif operation == "subtract":
            return a - b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            if b == 0:
                return "You can't divide by 0!"
            else:
                return a / b
        elif operation == "power":
            return a ** b
    except TypeError:
        return "You can't multiply those values!"
    
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    
def grade(*args):
    try:
        if len(args) == 0: return "Invalid data was provided."
        
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    except Exception:
        return "Invalid data was provided."
    
def repeat(string, times):
    result = ""
    for i in range(times):
        result += string
    return result

def student_scores(operation, **kwargs):
    if len(kwargs) == 0: return "Invalid data was provided."
    
    if operation == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif operation == "best":
        return max(kwargs, key=kwargs.get)
    else:
        return "Invalid data was provided."




def titleize(string):
    
    words = string.split()
    little_words = ["a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "by"]
    result = [] 
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)

        else:
            result.append(word.capitalize())
            
    return " ".join(result)





def hangman(word, guessed):
    result = ""
    for letter in word:
        if letter in guessed:
            result += letter
        else:
            result += "_"
    return result


def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []
    vowels = ["a","e","i","o","u"]
    
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        else:
            i = 0
            
            # move through consonants
            while i < len(word) and word[i] not in vowels:
                # special case for "qu"
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
            
            pig_latin_words.append(word[i:] + word[:i] + "ay")
    
    return " ".join(pig_latin_words)