import random


def generate_beautiful_woman_face_prompt(ethnicity="European"):
    # Define lists of possible values for each attribute

    # Define ethnicity-specific features
    ethnicity_features = {
        "Latina": {
            "FaceShape": ["Diamond"],
            "SkinTone": ["Golden", "Olive", "Caramel"],
            "Eyes": {
                "Shape": ["Big"],
                "Colors": ["Brown", "Hazel", "Green", "Amber"],
                "Eyelashes": {
                    "Length": ["Long"],
                    "Thickness": ["Full"]
                }
            },
            "Eyebrows": {
                "Shape": ["Straight,  Arched"],
                "Thickness": ["Thin", "Medium", "Thick"],
            },
            "Cheekbones": {
                "Prominence": ["High"],
                "Contouring": ["Natural", "Defined"]
            },
            "Lips": {
                "Size": ["Full"],
                "Shape": ["Plump", "Heart-shaped"],
                "ColorOptions": ["Natural", "Bold", "Glossy"]
            },
            "Chin": {
                "Type": ["Shorter", "Defined"],
                "Length": ["Short", "Medium"]
            },
            "Jawline": {
                "Type": ["Smooth", "Defined"],
                "Contouring": ["Natural", "Defined"]
            },
            "MakeupStyle": ["Airbrush makeup", "Natural look", "Glamorous"],
            "NoseShape": ["Mesorrhine", "Straight","Broad", "Aquiline"],
            "BrowProminence": ["Medium", "Low","High"],
            "Freckles": [True, False],
        },
        "Korean": {
            "FaceShape": ["V-shaped"],
            "SkinTone": ["Pale", "Porcelain", "Light Beige"],
            "Eyes": {
                "Shape": ["Small and rounded"],
                "Colors": ["Black", "Dark Brown", "Hazel"],
                "Eyelashes": {
                    "Length": ["Long"],
                    "Thickness": ["Full"]
                },
                "DoubleEyelids": 'True'
            },
            "Eyebrows": {
                "Shape": ["Straight or Slightly Arched"],
                "Thickness": ["Thin", "Medium"],
                "Defined": 'True'
            },
            "Cheekbones": {
                "Prominence": ["High"],
                "Contouring": ["Natural", "Defined"]
            },
            "Lips": {
                "Size": ["Thin", "Medium"],
                "Shape": ["Straight", "Slightly Full"],
                "ColorOptions": ["Natural", "Bold", "Glossy"]
            },
            "Chin": {
                "Type": ["Sharp", "Defined"],
                "Length": ["Short", "Medium"]
            },
            "Jawline": {
                "Type": ["Smooth", "Defined"],
                "Contouring": ["Natural", "Defined"]
            },
            "MakeupStyle": ["Natural look", "Dewy finish", "Glamorous"],
            "NoseShape": ["Narrow", "Pointy", "Broad", "Straight"],
            "BrowProminence": ["Medium", "Low"],
            "Freckles": [True, False],
        },
        "European": {
            "FaceShape": ["Oval", "Round"],
            "SkinTone": ["Ivory", "Pale", "Porcelain"],
            "Eyes": {
                "Shape": ["Deep-set almond-shaped"],
                "Colors": ["Blue", "Green", "Gray", "Hazel", "Brown"],
                "Eyelashes": {
                    "Length": ["Long"],
                    "Thickness": ["Full"]
                }
            },
            "Eyebrows": {
                "Shape": ["Well-shaped"],
                "Thickness": ["Thin", "Medium", "Thick"],
                "Arched": 'True'
            },
            "Cheekbones": {
                "Prominence": ["High"],
                "Contouring": ["Natural", "Defined"]
            },
            "Lips": {
                "Size": ["Big"],
                "Shape": ["Full", "Heart-shaped"],
                "ColorOptions": ["Natural", "Bold", "Glossy"]
            },
            "Chin": {
                "Type": ["Strong", "Defined", "Soft"],
                "Length": ["Short", "Medium", "Long"]
            },
            "Jawline": {
                "Type": ["Good", "Soft", "Angular"],
                "Contouring": ["Natural", "Defined"]
            },
            "MakeupStyle": ["HD makeup", "Natural look", "Glamorous"],
            "NoseShape": ["Straight", "Narrow", "Aquiline", "Broad"],
            "BrowProminence": ["High", "Medium", "Low"],
            "Freckles": [True, False],
        }
    }

    ethnicity_data = ethnicity_features.get(ethnicity)

    prompt = (f"Beautiful {ethnicity} woman with a {random.choice(ethnicity_data['FaceShape'])} face,"
              f"{random.choice(ethnicity_data['Eyes']['Shape'])} {random.choice(ethnicity_data['Eyes']['Colors'])} eyes ,"
              f"{random.choice(ethnicity_data['SkinTone'])} skin,"
              f"{random.choice(ethnicity_data['Lips']['Shape'])} {random.choice(ethnicity_data['Lips']['Size'])} lips ,"
              f"{random.choice(ethnicity_data['Chin']['Type'])} chin {random.choice(ethnicity_data['Chin']['Length'])},"
              f"{random.choice(ethnicity_data['Jawline']['Type'])} jawline with {random.choice(ethnicity_data['Jawline']['Contouring'])} contouring,"
              f"{random.choice(ethnicity_data['Cheekbones']['Prominence'])} cheekbones with {random.choice(ethnicity_data['Cheekbones']['Contouring'])} contouring,"
              f"{random.choice(ethnicity_data['Eyebrows']['Shape'])} eyebrows {random.choice(ethnicity_data['Eyebrows']['Thickness'])},"
              f"{random.choice(ethnicity_data['Eyes']['Eyelashes']['Length'])} eyelashes that are {random.choice(ethnicity_data['Eyes']['Eyelashes']['Thickness'])},"
              f"{random.choice(ethnicity_data['NoseShape'])} nose,"
              f" {random.choice(ethnicity_data['BrowProminence'])} Brow prominence,"
              f"{random.choice(ethnicity_data['MakeupStyle'])} makeup.")

    return prompt



print(generate_beautiful_woman_face_prompt("European"))
#print(generate_beautiful_woman_face_prompt("Latina"))
#print(generate_beautiful_woman_face_prompt("Korean"))
