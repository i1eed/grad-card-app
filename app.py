# Import necessary libraries
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration - Set paths for template and font
TEMPLATE_PATH = "static/card_template.png"  # Background card image
FONT_PATH = "static/arial.ttf"  # Font file
FONT_SIZE = 80  # Size of text
TEXT_COLOR = (255, 255, 255)  # White text color
TEXT_POSITION = (400, 500)  # Adjust based on your design
OUTPUT_FOLDER = "static/cards/"  # Folder for generated cards

# Ensure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].strip()  # Get the name from the form
        
        if name:
            # Load the card template
            img = Image.open(TEMPLATE_PATH)
            draw = ImageDraw.Draw(img)

            # Load font
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

            # Add text to the image
            draw.text(TEXT_POSITION, name, fill=TEXT_COLOR, font=font)

            # Save the personalized card
            output_path = os.path.join(OUTPUT_FOLDER, f"{name.replace(' ', '_')}.png")
            img.save(output_path)

            return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
