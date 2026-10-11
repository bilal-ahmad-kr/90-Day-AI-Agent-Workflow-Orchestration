import json
from pydantic import BaseModel, Field
import ollama

# 1. Define the exact JSON Schema using Pydantic
class BusinessLead(BaseModel):
    company_name: str = Field(description="The name of the company the lead works for")
    contact_name: str = Field(description="Full name of the person")
    email: str = Field(description="Email address if available, otherwise 'N/A'")
    project_budget_usd: int = Field(description="Estimated budget mentioned in USD, or 0 if unknown")
    key_requirements: list[str] = Field(description="List of core technical or business requirements")
    urgency: str = Field(description="Urgency level: Low, Medium, or High")

def extract_lead_to_json(unstructured_text: str):
    """
    Extracts structured data from messy text using Ollama and Pydantic validation.
    """
    prompt = f"""
    Extract the business lead information from the following text according to the required schema.
    
    Input Text:
    "{unstructured_text}"
    """

    try:
        # 2. Call Ollama with the format parameter set to the Pydantic schema model
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'system', 
                    'content': 'You are a precise data extraction engine. Extract information accurately and strictly match the requested data structure.'
                },
                {
                    'role': 'user', 
                    'content': prompt
                }
            ],
            # Ollama automatically handles Pydantic classes to enforce structured JSON output!
            format=BusinessLead.model_json_schema(),
            options={'temperature': 0.1} # Low temperature for high precision
        )

        # 3. Parse the raw JSON string returned by the model
        raw_json_content = response['message']['content']
        structured_data = json.loads(raw_json_content)
        
        return structured_data

    except Exception as e:
        return {"error": str(e)}

# --- Execution Example ---
if __name__ == "__main__":
    messy_email = """
    Hi team, my name is Sarah Jenkins from NexusCorp. We are urgently looking to build 
    a full-stack web app with React and Node.js. Our timeline is tight and we need it 
    launched next month. You can reach me at sarah@nexuscorp.io. We have allocated around 
    $8,500 for this phase. Let's talk!
    """

    print("--- Unstructured Input Email ---")
    print(messy_email.strip())
    
    print("\n--- Extracted Structured JSON Output ---")
    result = extract_lead_to_json(messy_email)
    print(json.dumps(result, indent=4))