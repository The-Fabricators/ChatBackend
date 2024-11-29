import openai
import os

def gptChat(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt}"}],
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"There's a error: {e}")
        
