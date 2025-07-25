import gradio as gr

# Function that returns the square
def square_number(n):
    return n ** 2

# Create Gradio interface
app = gr.Interface(
    fn=square_number,
    inputs=gr.Number(label="Enter a number"),
    outputs=gr.Number(label="Square")
)

# Launch app
app.launch()
