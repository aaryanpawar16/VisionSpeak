import cv2
import torch
from paddleocr import PaddleOCR
from transformers import BlipProcessor, BlipForConditionalGeneration
from gtts import gTTS
import os

# --- Configuration ---
# specialized prompt for the user interface
print("⏳ Loading AI Models... (This usually takes 30-60 seconds)")

# Initialize PaddleOCR (English, disabled angle classifier for speed/compatibility)
paddle_ocr = PaddleOCR(use_angle_cls=False, lang='en', show_log=False)

# Initialize BLIP (Image Captioning)
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

print("✅ Models Loaded!")

def capture_image_webcam(filename='input.jpg'):
    """Captures an image using the standard local webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return None
    
    print("📷 Press 's' to save the photo, or 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break
            
        cv2.imshow('Camera - Press "s" to Save', frame)
        
        key = cv2.waitKey(1)
        if key == ord('s'):  # Save
            cv2.imwrite(filename, frame)
            print(f"📸 Image saved to {filename}")
            cap.release()
            cv2.destroyAllWindows()
            return filename
        elif key == ord('q'): # Quit
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return None

def extract_text(image_path):
    """Extracts text using PaddleOCR."""
    try:
        result = paddle_ocr.ocr(image_path, cls=False)
        extracted_text = ""
        if result:
            for line in result:
                if line:
                    # Handle different version output formats
                    if isinstance(line, list):
                        for word_info in line:
                            extracted_text += word_info[1][0] + " "
                    else:
                        extracted_text += line[1][0] + " "
        return extracted_text.strip()
    except Exception as e:
        print(f"⚠️ OCR Error: {e}")
        return ""

def generate_description(image_path):
    """Generates a caption if no text is found."""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    inputs = blip_processor(image, return_tensors="pt")
    out = blip_model.generate(**inputs)
    description = blip_processor.decode(out[0], skip_special_tokens=True)
    return description

def text_to_speech(text, output_path="output.mp3"):
    """Converts text to audio."""
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)
    print(f"🔊 Audio saved to {output_path}")
    
    # Play audio (Works on Windows/Mac/Linux)
    if os.name == 'nt':  # Windows
        os.system(f'start {output_path}')
    else:  # Mac/Linux
        os.system(f'afplay {output_path}' if os.sys.platform == 'darwin' else f'xdg-open {output_path}')

# --- Main Execution ---
if __name__ == "__main__":
    choice = input("Choose input method:\n1. Webcam\n2. Image Path\n> ")
    
    img_path = None
    if choice == '1':
        img_path = capture_image_webcam()
    else:
        img_path = input("Enter image filename: ").strip('"')
        
    if img_path and os.path.exists(img_path):
        print("🔍 Analyzing image...")
        
        # Try OCR
        detected_text = extract_text(img_path)
        
        final_message = ""
        if detected_text:
            print(f"✅ Text Found: {detected_text}")
            final_message = detected_text
        else:
            print("⚠️ No text found. Generating description...")
            description = generate_description(img_path)
            print(f"🖼️ Description: {description}")
            final_message = description
            
        # Speak
        text_to_speech(final_message)
