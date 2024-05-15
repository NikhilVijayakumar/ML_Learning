import os
from deepface import DeepFace

def verify_face(source_path, target_path):
    try:
        result = DeepFace.verify(img1_path=source_path, img2_path=target_path)
        if result is None:
            print("Unable to detect face")
            return None
        max_distance = 1.0  # Maximum possible distance, assuming distances are normalized
        similarity_percentage = round(max(0, (max_distance - result["distance"]) / max_distance) * 100,2)
        result["similarity_percentage"] = similarity_percentage
        return result
    except Exception as e:
        print(f"Exception: {e}")
        return None

def process_images(source_image, target_folder):
    non_face_detected_images = []
    non_matching_images = []
    matching_images = []

    print(f"Image processing started on folder {target_folder}: ")
    for target_file in os.listdir(target_folder):
        target_image = os.path.join(target_folder, target_file)
        if os.path.isfile(target_image):
            result = verify_face(source_image, target_image)
            if result is not None:
                if result["verified"]:
                    matching_images.append({"filename": target_file, "similarity_percentage": result["similarity_percentage"]})
                else:
                    non_matching_images.append(target_file)
            else:
                non_face_detected_images.append(target_file)
        print(f"Processing completed {target_file}")

    return non_face_detected_images, non_matching_images, matching_images



def process_images_similarity(source_image, target_folder,similarity_percentage):
    non_face_detected_images = []
    non_matching_images = []
    matching_images = []

    print(f"Image processing started on folder {target_folder}: ")
    for target_file in os.listdir(target_folder):
        target_image = os.path.join(target_folder, target_file)
        if os.path.isfile(target_image):
            result = verify_face(source_image, target_image)
            if result is not None:
                if result["verified"] and result["similarity_percentage"] >= similarity_percentage:
                    matching_images.append({"filename": target_file, "similarity_percentage": result["similarity_percentage"]})
                else:
                    non_matching_images.append(target_file)
            else:
                non_face_detected_images.append(target_file)
        print(f"Processing completed {target_file}")

    return non_face_detected_images, non_matching_images, matching_images
