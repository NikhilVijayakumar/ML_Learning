import random


def generate_dress_prompt(ethnicity="European"):
    # Define dictionaries for ethnicity-specific dress styles with categories
    dress_styles = {
        "Latina": {
            "casual": {
                "tops": ["flowy blouse", "crop top"],
                "bottoms": ["jeans", "shorts"],
                "footwear": ["sandals", "sneakers"]
            },
            "summer": {
                "full_outfit": ["sundress"],
                "footwear": ["flip-flops", "espadrilles"]
            },
            "sports": {
                "tops": ["athletic tank top"],
                "bottoms": ["leggings"],
                "footwear": ["running shoes"]
            },
            "formal": {
                "full_outfit": ["elegant gown", "cocktail dress"],
                "footwear": ["heels"]
            },
            "dress": {
                "full_outfit": ["colorful embroidered dress"],
                "footwear": ["flats"]
            }
        },
        "Korean": {
            "casual": {
                "tops": ["oversized sweater", "blouse"],
                "bottoms": ["skinny jeans", "culottes"],
                "footwear": ["sneakers", "loafers"]
            },
            "summer": {
                "full_outfit": ["lightweight dress"],
                "footwear": ["sandals"]
            },
            "sports": {
                "tops": ["athletic t-shirt"],
                "bottoms": ["shorts"],
                "footwear": ["running shoes"]
            },
            "formal": {
                "full_outfit": ["hanbok", "elegant dress"],
                "footwear": ["heels"]
            },
            "dress": {
                "full_outfit": ["korean traditional dress"],
                "footwear": ["flats"]
            }
        },
        "European": {
            "casual": {
                "tops": ["t-shirt", "blouse"],
                "bottoms": ["jeans", "capris"],
                "footwear": ["flats", "sneakers"]
            },
            "summer": {
                "full_outfit": ["summer dress"],
                "footwear": ["sandals"]
            },
            "sports": {
                "tops": ["sports tank top"],
                "bottoms": ["track pants"],
                "footwear": ["athletic shoes"]
            },
            "formal": {
                "full_outfit": ["evening gown", "tailored suit"],
                "footwear": ["heels"]
            },
            "dress": {
                "full_outfit": ["elegant cocktail dress"],
                "footwear": ["pumps"]
            }
        }
    }

    # Get ethnicity-specific dress styles
    style_data = dress_styles.get(ethnicity)

    # Randomly select a category to wear
    category = random.choice(list(style_data.keys()))

    # Constructing the outfit based on the selected category
    if 'full_outfit' in style_data[category]:
        outfit = random.choice(style_data[category]['full_outfit'])
        footwear = random.choice(style_data[category]['footwear'])
        prompt = f"This {ethnicity} woman is wearing a {outfit} paired with {footwear}."
    else:
        tops = random.choice(style_data[category]['tops'])
        bottoms = random.choice(style_data[category]['bottoms'])
        footwear = random.choice(style_data[category]['footwear'])
        prompt = (f"This {ethnicity} woman is wearing a {tops} and {bottoms} paired with {footwear}.")

    return prompt


# Example usage
if __name__ == "__main__":
    print(generate_dress_prompt("European"))
    print(generate_dress_prompt("Latina"))
    print(generate_dress_prompt("Korean"))