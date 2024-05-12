import random

def generate_female_dress_prompt(style="casual", ethnicity="European"):
    # Define lists of possible values for each attribute
    dress_styles = {
        "medieval": ["gown", "corset", "cloak", "robe"],
        "modern": ["dress", "skirt", "blouse", "pantsuit"],
        "casual": ["t-shirt", "jeans", "sneakers", "hoodie"],
        "formal": ["gown", "evening dress", "suit", "heels"],
        "sports": ["athletic top", "leggings", "sneakers", "sports bra"],
        "yoga": ["yoga pants", "tank top", "yoga mat", "sweatband"]
    }

    # Define ethnicity-specific dress elements
    ethnicity_dress_elements = {
        "Korean": {
            "casual": ["hanbok-inspired dress", "flats", "handbag", "headband"],
            "formal": ["hanbok", "heels", "clutch", "hairpin"]
        },
        "Indian": {
            "casual": ["sari", "sandals", "bindi", "bangles"],
            "formal": ["sari", "heels", "clutch", "necklace"]
        },
        "Latina": {
            "casual": ["ruffled blouse", "denim skirt", "espadrilles", "tote bag"],
            "formal": ["flamenco dress", "high heels", "clutch", "statement earrings"]
        },
        "European": {
            "casual": ["midi dress", "flats", "tote bag", "sunglasses"],
            "formal": ["ballgown", "stilettos", "clutch", "pearl necklace"]
        }
        # Add more ethnicities and their dress elements as needed
    }

    # Get dress elements based on style and ethnicity
    dress_elements = ethnicity_dress_elements.get(ethnicity, {}).get(style, [])

    if not dress_elements:
        return "Invalid style or ethnicity."

    # Construct the prompt string
    prompt = f"Female {style} dress for {ethnicity}: "
    prompt += ", ".join(dress_elements) + "."

    return prompt

# Example usage
prompt = generate_female_dress_prompt("casual", "European")
print(prompt)
