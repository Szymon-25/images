import cairosvg
import os

# The base template for your SVG. The SCORE and REMAINDER will be replaced.
SVG_TEMPLATE = """
<svg width="120" height="120" viewBox="0 0 42 42" xmlns="http://www.w3.org/2000/svg">
  <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#E6E6FA" stroke-width="4"></circle>
  <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#6A5ACD" stroke-width="4" stroke-dasharray="{SCORE} {REMAINDER}" stroke-dashoffset="25" stroke-linecap="round"></circle>
</svg>
"""

# Create a directory to save the images
output_dir = "score_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Generating 101 score images...")

# Loop from 0 to 100
for score in range(101):
    remainder = 100 - score
    
    # Fill in the SVG template with the current score
    svg_code = SVG_TEMPLATE.format(SCORE=score, REMAINDER=remainder)
    
    # Define the output filename
    output_filename = os.path.join(output_dir, f"score-{score}.png")
    
    # Convert the SVG string to a PNG file
    cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=output_filename)

print(f"Success! All images saved in the '{output_dir}' folder.")
