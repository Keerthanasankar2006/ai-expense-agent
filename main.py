import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from tools import calculate_total, add_expense


load_dotenv()


client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


tools = [

    {
        "type": "function",
        "function": {
            "name": "calculate_total",
            "description": "Calculate the total of multiple expenses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amounts": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": "List of expense amounts"
                    }
                },
                "required": ["amounts"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "add_expense",
            "description": "Save an expense into the expense database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "Expense amount"
                    },
                    "category": {
                        "type": "string",
                        "description": "Expense category such as food, travel or shopping"
                    },
                    "description": {
                        "type": "string",
                        "description": "Short description of the expense"
                    }
                },
                "required": [
                    "amount",
                    "category",
                    "description"
                ]
            }
        }
    }

]


system_prompt = """
You are an AI Expense Assistant.

You can help the user manage expenses.

Available tools:

1. calculate_total
   Use this when the user asks to calculate
   the total of multiple amounts.

2. add_expense
   Use this when the user wants to save an expense.

Answer in simple English.
"""


user_message = input("You: ")


messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_message
    }
]


# AGENT LOOP

while True:

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )


    assistant_message = response.choices[0].message


    # No tool required

    if not assistant_message.tool_calls:

        print("\nFinal Answer:")
        print(assistant_message.content)

        break


    # Save assistant tool request

    messages.append(assistant_message)


    # Execute every requested tool

    for tool_call in assistant_message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )


        print("\nAgent selected tool:", tool_name)

        print("Arguments:", arguments)


        # calculate_total

        if tool_name == "calculate_total":

            result = calculate_total(
                arguments["amounts"]
            )


        # add_expense

        elif tool_name == "add_expense":

            result = add_expense(
                arguments["amount"],
                arguments["category"],
                arguments["description"]
            )


        else:

            result = "Unknown tool"


        print("Tool result:", result)


        # Send result back to LLM

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )