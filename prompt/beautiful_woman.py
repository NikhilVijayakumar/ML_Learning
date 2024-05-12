import random

def generate_beautiful_woman_prompt(ethnicity="European"):
    # Define lists of possible values for each attribute
    face_shapes = ["round", "oval", "square", "heart", "diamond"]
    eye_colors = ["green", "blue", "brown", "hazel"]
    lip_shapes = ["full", "plump", "thin", "heart-shaped", "round"]
    nose_shapes = ["small", "pointy", "button", "straight", "upturned"]
    makeup_styles = ["HD makeup", "Natural makeup", "Airbrush makeup", "Evening makeup",
                     "Matte makeup", "Bridal makeup", "Smokey makeup", "Dewy makeup", "Editorial makeup"]
    lighting_conditions = ["natural lighting", "studio lighting", "cinematic lighting"]

    # Define ethnicity-specific features
    ethnicity_features = {
        "Latina": {
            "makeup": random.choice(makeup_styles),
            "eye_color": random.choice(["brown", "hazel"]),
            "lip_shape": random.choice(["full", "plump", "heart-shaped"]),
            "nose_shape": random.choice(["small", "pointy", "upturned"]),
            "cheekbone": "high",
            "jawline": "slender",
            "skin_tone": random.choice(["ivory", "pale", "porcelain", "beige"]),
            "face_shape": random.choice(face_shapes),
            "lighting": random.choice(lighting_conditions)
        },
        "Korean": {
            "makeup": random.choice(makeup_styles),
            "eye_color": "brown",
            "lip_shape": "full",
            "nose_shape": "small",
            "cheekbone": "prominent",
            "jawline": "slender",
            "skin_tone": "porcelain",
            "face_shape": random.choice(face_shapes),
            "lighting": random.choice(lighting_conditions)
        },
        "European": {
            "makeup": random.choice(makeup_styles),
            "eye_color": random.choice(["blue", "green"]),
            "lip_shape": random.choice(["full", "thin", "heart-shaped"]),
            "nose_shape": random.choice(["small", "straight", "upturned"]),
            "cheekbone": random.choice(["high", "prominent"]),
            "jawline": random.choice(["angular", "chiseled"]),
            "skin_tone": random.choice(["ivory", "pale", "porcelain", "golden", "almond"]),
            "face_shape": random.choice(face_shapes),
            "lighting": random.choice(lighting_conditions)
        },
        # Add more ethnicities and their associated features as needed
    }

    # Get ethnicity-specific features
    ethnicity_data = ethnicity_features.get(ethnicity)

    # Construct the prompt string
    prompt = (f"Beautiful {ethnicity} woman with a {ethnicity_data['face_shape']} face, "
              f"{ethnicity_data['eye_color']} eyes, {ethnicity_data['skin_tone']} skin, "
              f"{ethnicity_data['lip_shape']} lips, {ethnicity_data['nose_shape']} nose, "
              f"{ethnicity_data['cheekbone']} cheekbones, {ethnicity_data['jawline']} jawline, "
              f"and {ethnicity_data['makeup']} makeup, under {ethnicity_data['lighting']}.")

    return prompt

# Example usage
prompt = generate_beautiful_woman_prompt()
print(prompt)
