def print_analysis_report(no_face_detected_images, non_matching_images, matching_images):
    total = len(no_face_detected_images) + len(non_matching_images) + len(matching_images)
    print("\nAnalysis report")
    print(f"Total images: {total}")

    # Print non face detected images
    no_face_detected_count = len(no_face_detected_images)
    print(f"{no_face_detected_count} images where face cannot be detected: {no_face_detected_count * 100 / total:.2f}%")
    for image_name in no_face_detected_images:
        print(f"Unable to detect face on target image {image_name}")

    # Print non matching images
    non_matching_count = len(non_matching_images)
    print(f"{non_matching_count} non-matching images: {non_matching_count * 100 / total:.2f}%")
    for image_name in non_matching_images:
        print(f"Non-matching target image {image_name}")

    # Sort matching images based on similarity score
    sorted_matching_images = sorted(matching_images, key=lambda x: x['similarity_percentage'], reverse=True)

    # Print matching images sorted by similarity score
    matching_count = len(matching_images)
    print(f"{matching_count} matching images: {matching_count * 100 / total:.2f}%")
    for matching_image in sorted_matching_images:
        print(f"Matching target image {matching_image['filename']} with similarity percentage: {matching_image['similarity_percentage']}%")
