import random


def generate_body_prompt(ethnicity="European"):
    # Define dictionaries for ethnicity-specific body features
    ethnicity_body_features = {
        "Latina": {
            "BodyShape": ["Hourglass", "Pear", "Apple"],
            "Height": {
                "Categories": ["Short", "Average", "Tall"]
            },
            "Weight": {
                "Categories": ["Slim", "Fit", "Curvy"]
            },
            "BustSize": {
                "Options": ["Medium", "Large"]
            },
            "WaistSize": {
                "Options": ["Narrow", "Average"]
            },
            "HipSize": {
                "Options": ["Average", "Full"]
            },
            "HairOptions": {
                "Types": ["Straight", "Wavy", "Curly"],
                "Colors": ["Brunette", "Black", "Chestnut"],
                "LengthOptions": ["Short", "Medium", "Long"],
                "Styles": ["Loose waves", "Braided crown", "Messy bun",
                           "Straight with bangs", "Curly updo"]
            }
        },
        "Korean": {
            "BodyShape": ["Slim", "Athletic"],
            "Height": {
                "Categories": ["Short", "Average"]
            },
            "Weight": {
                "Categories": ["Slim", "Fit"]
            },
            "BustSize": {
                "Options": ["Medium", "Large"]
            },
            "WaistSize": {
                "Options": ["Narrow", "Average"]
            },
            "HipSize": {
                "Options": ["Narrow", "Average"]
            },
            "HairOptions": {
                "Types": ["Straight"],
                "Colors": ["Black", "Dark Brown"],
                "LengthOptions": ["Short", "Medium", "Long"],
                "Styles": ["Straight and sleek",
                           "Soft waves with layers",
                           "High ponytail",
                           "Braided pigtails"]
            }
        },
        # European features
        "European": {
            # Similar structure as above for European features
            # Include hair styles for European models
            "BodyShape": ["Slim", "Athletic", "Curvy"],
            "Height": {
                "Categories": ["Short", "Average", "Tall"]
            },
            "Weight": {
                "Categories": ["Slim", "Fit", "Average", "Curvy"]
            },
            "BustSize": {
                "Options": ["Medium", "Large"]
            },
            "WaistSize": {
                "Options": ["Narrow", "Average"]
            },
            "HipSize": {
                "Options": ["Average", "Full"]
            },
            "HairOptions": {
                "Types": ["Straight", "Wavy", "Curly"],
                "Colors": ["Blonde", "Brunette", "Redhead", "Black"],
                "LengthOptions": ["Short", "Medium", "Long"],
                "Styles": ["Long layers",
                           "Sleek bob",
                           "Curls with volume",
                           "Messy bun",
                           "Ponytail with waves"]
            }

        }
    }

    # Get ethnicity-specific body features
    body_data = ethnicity_body_features.get(ethnicity)

    # Constructing the prompt
    prompt = f"Character Body Features:\n"

    # Randomly select values for fields with multiple options
    body_shape = random.choice(body_data['BodyShape'])
    height = random.choice(body_data['Height']['Categories'])
    weight = random.choice(body_data['Weight']['Categories'])
    bust_size = random.choice(body_data['BustSize']['Options'])
    waist_size = random.choice(body_data['WaistSize']['Options'])
    hip_size = random.choice(body_data['HipSize']['Options'])

    # Hair options
    hair_options = body_data['HairOptions']
    hair_type = random.choice(hair_options['Types'])
    hair_color = random.choice(hair_options['Colors'])
    hair_length = random.choice(hair_options['LengthOptions'])
    hair_style = random.choice(hair_options['Styles'])

    # Constructing the prompt
    prompt = (f"Professional Full body photoshoot Beautiful {ethnicity} {body_shape} shape "
              f"{weight} body type "
              f"Curvy, Busty, Voluptuous {bust_size} breast "
              f"{waist_size} Waist "
              f"Voluptuous Curvy {hip_size} Hip "
              f"{hair_color} {hair_type} {hair_length} {hair_style} Hair ")

    return prompt


# Example usage
if __name__ == "__main__":
    print(generate_body_prompt("European"))
    #print(generate_body_prompt("Latina"))
    #print(generate_body_prompt("Korean"))
