from utils.face_utils import process_images,process_images_similarity
from utils.report_utils import print_analysis_report
from utils.file_utils import organize_files

def process_and_report(source_image, target_folder, base_filename):
    no_face_detected_images, no_matching_images, matching_images = process_images(source_image, target_folder)
    print_analysis_report(no_face_detected_images, no_matching_images, matching_images)
    organize_files(target_folder, base_filename, no_face_detected_images, no_matching_images, matching_images)



def process_and_similarity(source_image, target_folder,similarity_percentage):
    no_face_detected_images, no_matching_images, matching_images = process_images_similarity(source_image, target_folder,similarity_percentage)
    print_analysis_report(no_face_detected_images, no_matching_images, matching_images)
    organize_files(target_folder, no_face_detected_images, no_matching_images, matching_images)
