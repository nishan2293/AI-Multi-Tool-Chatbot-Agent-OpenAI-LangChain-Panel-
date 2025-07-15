import panel as pn
from utils.agent_initializer import get_agent

pn.extension()
agent = get_agent()

input_box = pn.widgets.TextInput(placeholder="Ask me anything...")
output_area = pn.pane.Markdown("")

def on_submit(event):
    query = input_box.value
    if query:
        response = agent.run(query)
        output_area.object += f"\n**You:** {query}\n\n**Bot:** {response}\n"
        input_box.value = ""

input_box.param.watch(on_submit, "value")

dashboard = pn.Column(
    "# 🧠 AI Multi-Tool Chatbot",
    input_box,
    output_area
)

dashboard.servable()