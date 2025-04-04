import solara
from mesa.visualization import SolaraViz, make_space_component
from money_model import MoneyModel, MoneyAgent

def agent_portrayal(agent: MoneyAgent):
    return {
        "Shape": "circle",
        "Color": "blue" if agent.wealth > 0 else "red",
        "Filled": "true",
        "r": 0.5,
        "Layer": 0,
    }

model_cls = MoneyModel
model_params = {
    "N": 100,
    "width": 10,
    "height": 10,
}

space = make_space_component(agent_portrayal)

@solara.component
def Page():
    return SolaraViz(
        model_cls=model_cls,
        model_params=model_params,
        components=[space]
    )
