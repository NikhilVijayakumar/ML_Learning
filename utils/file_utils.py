import os
import shutil

def rename_files(folder_path, base_name):
    # Hardcoded supported extensions
    supported_extensions = {'.png', '.jpg', '.jpeg', '.webp'}

    # Check if the folder path exists
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path")
        return

    # Initialize index
    index = 1

    # Iterate over files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(file_name)

        # Check if the extension is supported
        if extension.lower() in supported_extensions:
            # Generate new file name
            new_file_name = f"{base_name}_{index}{extension.lower()}"
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)

            # Increment index
            index += 1

    print(f"Files renamed successfully from '{base_name}_1' to '{base_name}_{index - 1}'")





def organize_files(target_folder, base_name, no_face_detected_images, non_matching_images, matching_images):
    # Define directories
    matching_dir = os.path.join(target_folder, "matching")
    non_matching_dir = os.path.join(target_folder, "not_matching")
    non_face_detected_dir = os.path.join(target_folder, "no_face_detected")

    # Create directories if they don't exist
    for directory in [matching_dir, non_matching_dir, non_face_detected_dir]:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)

    # Sort matching images by similarity percentage in descending order
    sorted_matching_images = sorted(matching_images, key=lambda x: x['similarity_percentage'], reverse=True)

    # Copy files to corresponding directories
    for index, matching_image in enumerate(sorted_matching_images, start=1):
        similarity_percentage = str(matching_image['similarity_percentage']).replace('.', '_')  # Replace decimal point
        filename = matching_image['filename']
        _, extension = os.path.splitext(filename)
        # Generate new file name
        #new_filename = f"{index}_{base_name}_{similarity_percentage}{extension}"

        # Copy file to matching directory with new name
        shutil.copy2(os.path.join(target_folder, filename), os.path.join(matching_dir, filename))

    # Copy non-matching images to corresponding directory
    for non_matching_image in non_matching_images:
        shutil.copy2(os.path.join(target_folder, non_matching_image), non_matching_dir)

    # Copy non-face-detected images to corresponding directory
    for non_face_detected_image in no_face_detected_images:
        shutil.copy2(os.path.join(target_folder, non_face_detected_image), non_face_detected_dir)

    print("Files organized successfully.")

