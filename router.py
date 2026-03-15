from prompts import PROMPTS

def route_and_respond(message, intent_data):

    intent = intent_data["intent"]

    if intent == "unclear":
        return "I'm not sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"

    if intent == "code":
        return "You can sort a list in Python using the built-in sorted() function or the list.sort() method."

    elif intent == "data":
        numbers = [12, 45, 23, 67]
        avg = sum(numbers) / len(numbers)
        return f"The average of the numbers is {avg}."

    elif intent == "writing":
        return "Try simplifying your sentence and removing unnecessary words to make it clearer and more professional."

    elif intent == "career":
        return "Could you tell me more about the role you are preparing for and your experience level?"

    else:
        return "I'm not sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"