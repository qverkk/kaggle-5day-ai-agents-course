from google.adk.runners import InMemoryRunner
import asyncio
from agent import image_agent
from dotenv import load_dotenv
from IPython.display import display, Image as IPImage
import base64

load_dotenv()

async def main():
    runner = InMemoryRunner(agent=image_agent)
    response = await runner.run_debug("Provide a sample tiny image", verbose=True)
    for event in response:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, "function_response") and part.function_response:
                    for item in part.function_response.response.get("content", []):
                        if item.get("type") == "image":
                            display(IPImage(data=base64.b64decode(item["data"])))

if __name__=="__main__":
    asyncio.run(main())

