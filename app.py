from ultralytics import YOLO
import gradio as gr

# Load the model
model = YOLO("model_weights.pt")

# Define the function to call for each frame
def inference(frame, confidence, overlap):
    results = model.predict(
        source=frame,
        device="cuda:0",
        imgsz=(960, 1707),
        conf=confidence,
        iou=overlap,
    )
    output = results[0].plot(
        line_width=3,
        labels=False,
        conf=False,
    )
    return output

# Define the GUI
with gr.Blocks(fill_height=True) as demo:
    gr.Markdown(
        """
        # Mini Project 2: Object Detection
        Long-distance Pedestrian Detection w/ YOLO11s.
        """
    )
    with gr.Row():
        frame = gr.Image(
            label="Camera",
            type="numpy", sources="webcam", streaming=True,
        )
    with gr.Row():
        confidence = gr.Slider(
            label="Confidence Threshold",
            minimum=0.0, maximum=1.0, step=0.05,
            value=0.10,
        )
        overlap = gr.Slider(
            label="Overlap Threshold",
            minimum=0.0, maximum=1.0, step=0.05,
            value=0.20,
        )
    frame.stream(
        inference,
        inputs=[frame, confidence, overlap],
        outputs=frame,
        stream_every=0.1, # FPS here (seconds per frame)
    )

# Launch the GUI
demo.launch()