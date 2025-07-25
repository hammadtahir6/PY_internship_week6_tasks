import gradio as gr

# Function to reverse text
def reverse_text(text):
    return text[::-1]

# Create the Gradio app
app = gr.Interface(
    fn=reverse_text,
    inputs=gr.Textbox(lines=2, placeholder="Type a sentence...", label="Input Sentence"),
    outputs=gr.Textbox(label="Reversed Output")
)

# Launch the app
app.launch()
