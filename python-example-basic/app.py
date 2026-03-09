from shiny import Inputs, Outputs, Session, ui, render, App

app = ui.page_fluid(
  ui.panel_title("My First Shiny App"),
  ui.input_text("name", label="Enter your name:"),
  ui.output_text("greeting"),
)

def server(inputs: Inputs, outputs: Outputs, session: Session):
  @render.text
  def greeting():
    return f"Hello, {inputs.name()}!"

app = App(app, server)

# From: https://www.appsilon.com/guides/shiny-python-guide#6-getting-started-with-shiny-for-python 
