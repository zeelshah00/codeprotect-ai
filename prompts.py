from openai import OpenAI
import re
client = OpenAI()


def ai_suggestions(code, findings, language):

    prompt = f"""
        You are a secure coding assistant.

        Language: {language}

        Code: {code}

        Security findings: {findings}

    Provide a safer solution with minimal changes and nothing else.
    """
    try:
        suggestion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )
    except:
        suggestion = "AI explanation unavailable."


    return suggestion.choices[0].message.content