from livekit.agents import ToolContext
class AssistantFnc(ToolContext) :
    def __init__ (self) : 
        super().__init__(tools=[])