from langchain.agents.middleware import dynamic_prompt
from schema import UserContext

@dynamic_prompt
def role_based_prompt(request):
    role = request.runtime.context.user_role

    base = "You are an intelligent AI assistant."

    if role == "expert":
        return base + " Provide detailed technical explanations."
    elif role == "beginner":
        return base + " Provide simple easy explanations."
    else:
        return base