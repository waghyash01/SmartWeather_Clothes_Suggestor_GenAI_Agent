from agent import agent
from schema import UserContext
import base64

config = {"configurable": {"thread_id": 1}}

context = UserContext(
    user_id="USER001",
    user_role="expert"
)

import base64

def load_image_base64(image_path: str):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
    
#wrapper function to agent.invoke (here we do streaming)
def chat_stream(message: str, config, context,image_path: str = None):

    content = [{"type": "text", "text": message}]

    # 🔥 Add image if provided
    if image_path:
        image_base64 = load_image_base64(image_path)
        content.append({
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{image_base64}"
        })

    stream = agent.stream(
        {"messages": [{"role": "user", "content": content}]},
        config=config,
        context=context,
        stream_mode="values"   # Important
    )

    final_response = None

    for chunk in stream:
        if "structured_response" in chunk:
            final_response = chunk["structured_response"]
            print(final_response.summary, end="", flush=True)

    print("\n")
    return final_response



response1 = chat_stream(
    "Is this outfit good for today?",
    config,
    context,
    image_path="images/sweater.jpg"
)

response2 = chat_stream(
    "How is the weather today and any tips for me?",
    config,
    context
)

response3 = chat_stream(
    "whats the most impostant tip u gave me above and how its going to reply u gave on my outfit above",
    config,
    context
)
