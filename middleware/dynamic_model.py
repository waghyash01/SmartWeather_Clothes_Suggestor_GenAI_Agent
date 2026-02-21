from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from models import basic_model, advanced_model

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    message_count = len(request.state["messages"])

    if message_count > 5:
        request.model = advanced_model
    else:
        request.model = basic_model

    return handler(request)