import asyncio
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import deepgram, silero
from livekit.plugins.groq import LLM

load_dotenv()

class Assistant(Agent):
    def __init__(self):
        super().__init__(
            instructions=(
                "You are a helpful voice assistant. "
                "Keep your responses short and conversational."
            )
        )

async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(),
        llm=LLM(model="llama-3.1-8b-instant"),
        tts=deepgram.TTS(),
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(),
    )

    await session.generate_reply(
        instructions="Greet the user and ask how you can help."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))