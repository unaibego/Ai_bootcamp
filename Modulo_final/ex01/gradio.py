import gradio as gr
import numpy as np
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

# def image_predictor(image):
#     # url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
#     # image = Image.open(requests.get(url, stream=True).raw)

#     processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
#     model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

#     inputs = processor(images=image, return_tensors="pt")
#     outputs = model(**inputs)
#     logits = outputs.logits
#     # model predicts one of the 1000 ImageNet classes
#     predicted_class_idx = logits.argmax(-1).item()
#     return (model.config.id2label[predicted_class_idx])

# demo = gr.Interface(image_predictor, gr.Image(shape=(200, 200)), "label")
# demo.launch()

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

# demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
# demo.launch()

input_interface = gr.inputs.Image(shape=(200, 200))
output_interface = gr.outputs.Image()
io_interfaces = gr.Interface(sepia, input_interface, output_interface)

io_interfaces.launch()