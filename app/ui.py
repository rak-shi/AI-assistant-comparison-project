import gradio as gr

from oss_assistant import generate_response as oss_chat
from frontier_assistant import generate_response as api_chat

def chat(model_type, message):

    if model_type == "OSS":
        return oss_chat(message)

    return api_chat(message)

demo = gr.Interface(
    fn=chat,
    inputs=[
        gr.Dropdown(
            ["OSS", "Frontier"],
            label="Assistant"
        ),
        gr.Textbox(label="Message")
    ],
    outputs="text"
)

demo.launch(share=True)