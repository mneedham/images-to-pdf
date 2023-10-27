from pdfme import build_pdf, PDFDocument
import glob
from PIL import Image

document = {"style": {
    'rotate_page': True,
      'margin_bottom': 15,
    'text_align': 'c','bg': 'red'
}}

# document['per_page'] = [
#     {'pages': '1:1000:2', 'style': {'margin': [60, 100, 60, 60]}},
#     {'pages': '0:1000:2', 'style': {'margin': [0,0,0,0]}}
# ]

per_page = []
document['per_page'] = per_page


# page_width =  3840
# page_height = 2160

page_width = 842
page_height = 595

document['sections'] = []

# files = [
#     '2023-10-26_11-06-22.png', 
#     '2023-10-26_11-06-32.png'
# ]

base = "../../../20231027-MaterializedView"
print(f"{base}slides/*.png")

files = sorted([file for file in glob.glob(f"{base}/slides/*.png")])

print (files)

for index, image_path in enumerate(files):
    image = Image.open(image_path)
    image_width, image_height = image.size 
    print(image.size)

    scale_factor = min(page_width / image_width, page_height / image_height)
    scaled_width = image_width * scale_factor
    scaled_height = image_height * scale_factor

    vertical = (page_height - scaled_height) / 2
    horizontal = (page_width - scaled_width) / 2
    horizontal = 50

    # vertical = (page_height - image_height) / 4
    # vertical = 200
    # horizontal = (page_width - image_width) / 2
    # horizontal = 100

    print(vertical, horizontal)

    per_page.append({'pages': f"{index}", 'style': {'margin': [vertical,horizontal,vertical,horizontal]}})

    section1 = {}
    section1['content'] = content1 = []
    content1.append({
        'image': image_path,
        'style': {
            'min_height': 200
        #     'x': x_position,
        # 'y': y_position,
        # 'width': scaled_width,
        # 'height': scaled_height,
        # 'margin': [0,100,100,100]
        }
    })

    document['sections'].append(section1)

with open(f"{base}/slides/document.pdf", 'wb') as f:
    # build_pdf(document, f, {"rotate_page": True})
    doc = PDFDocument(document)
    doc.run()
    doc.output(f)

