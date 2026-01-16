import json
import os
from typing import Any, Dict
from litellm import completion

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"

#api_key = 


def get_itinerary(destination: str) -> Dict[str, Any]:
    """
    Returns a JSON-like dict with keys:
      - destination
      - price_range
      - ideal_visit_times
      - top_attractions
    """
    # implement litellm call here to generate a structured travel itinerary for the given destination

    # See https://docs.litellm.ai/docs/ for reference.

    response = completion(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Return ONLY valid JSON. No extra text."
            },
            {
                "role": "user",
                "content": f"""
              Generate a travel itinerary for {destination}.
              Return a JSON object with exactly these fields:
              - destination (string)
              - price_range (string)
              - ideal_visit_times (array of strings)
              - top_attractions (array of strings)
              """
            }
        ],
    )
    print(response["choices"][0]["message"]["content"])

    content = response["choices"][0]["message"]["content"]
    content = content[content.find("{") : content.rfind("}") + 1]
    data = json.loads(content)


    for key in ["destination", "price_range", "ideal_visit_times", "top_attractions"]:
        if key not in data:
            raise ValueError("Invalid response schema")
    

    return data
