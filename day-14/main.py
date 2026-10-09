
import os
import socket
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

# Temporary IPv4-only test
original_getaddrinfo = socket.getaddrinfo

def ipv4_only(host, port, family=0, type=0, proto=0, flags=0):
    return original_getaddrinfo(
        host, port, socket.AF_INET, type, proto, flags
    )

socket.getaddrinfo = ipv4_only


# Load environment variables from the project root .env file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

API_URL = (
    "https://generativelanguage.googleapis.com/"
    f"v1beta/models/{MODEL}:generateContent"
)

OUTPUT_FILE = Path(__file__).resolve().parent / "generated_content.txt"

CONTENT_TYPES = {
    "1": "a professional customer email reply",
    "2": "an engaging LinkedIn post",
    "3": "a polite business lead follow-up email",
}


def generate_content(content_type, user_details):
    """Generate business content using the Gemini API."""

    if not API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Add your API key to the root .env file."
        )

    prompt = f"""
You are a professional business writing assistant.

Task:
Generate {content_type} based on the user's details.

Requirements:
- Use clear, natural English.
- Keep the content relevant to the user's request.
- Do not invent facts, prices, promises, or customer information.
- Return only the generated content.

User details:
{user_details}
"""

    headers = {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
        },
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60,
    )

    # Raise an exception for unsuccessful HTTP responses
    response.raise_for_status()

    data = response.json()
    candidates = data.get("candidates", [])

    if not candidates:
        feedback = data.get("promptFeedback", {})
        block_reason = feedback.get("blockReason", "Unknown")
        raise ValueError(
            f"No content generated. Reason: {block_reason}"
        )

    candidate = candidates[0]
    parts = candidate.get("content", {}).get("parts", [])

    generated_text = "\n".join(
        part["text"]
        for part in parts
        if isinstance(part.get("text"), str)
    ).strip()

    if not generated_text:
        finish_reason = candidate.get(
            "finishReason", "Unknown"
        )
        raise ValueError(
            f"Gemini returned empty content. "
            f"Finish reason: {finish_reason}"
        )

    return generated_text


def save_content(content_type, generated_text):
    """Append generated content to a local text file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(f"Created: {timestamp}\n")
        file.write(f"Type: {content_type}\n")
        file.write("=" * 60 + "\n\n")
        file.write(generated_text + "\n")

    print(f"\nContent saved to: {OUTPUT_FILE}")


def main():
    """Run the AI Business Content Generator."""

    print("\n=== AI Business Content Generator ===")
    print("Powered by Google Gemini API\n")

    for key, value in CONTENT_TYPES.items():
        print(f"{key}. {value.title()}")

    choice = input("\nChoose an option (1-3): ").strip()

    if choice not in CONTENT_TYPES:
        print("Invalid option. Please choose 1, 2, or 3.")
        return

    user_details = input(
        "\nDescribe what you want the AI to write: "
    ).strip()

    if not user_details:
        print("Input cannot be empty.")
        return

    content_type = CONTENT_TYPES[choice]

    try:
        print("\nGenerating content with Gemini API...\n")

        generated_text = generate_content(
            content_type,
            user_details,
        )

        print("-" * 60)
        print(generated_text)
        print("-" * 60)

        save_content(content_type, generated_text)

    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code

        print(f"Gemini API returned HTTP error: {status_code}")

        try:
            details = error.response.json()
            message = details.get("error", {}).get("message")

            if message:
                print(f"Details: {message}")

        except ValueError:
            print("Could not read the API error details.")

        if status_code == 429:
            print(
                "Check your free-tier quota, rate limits, "
                "and API usage."
            )
        elif status_code in (401, 403):
            print("Check your API key and model access.")
        elif status_code in (400, 404):
            print("Check your request and model name.")

    except requests.exceptions.Timeout:
        print("The API request timed out. Please try again.")

    except requests.exceptions.RequestException as error:
        print(f"Network or API request failed: {error}")

    except ValueError as error:
        print(f"Generation failed: {error}")


if __name__ == "__main__":
    main()