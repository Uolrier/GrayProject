from .base import BaseRuntime
from .registry import RUNTIME_REGISTRY


class DummyRuntime(BaseRuntime):
    """
    Dummy runtime for testing runtime architecture.
    """

    def load(self):
        print("Dummy runtime loaded")

    def generate(self, prompt: str, **kwargs):
        return f"Dummy response: {prompt}"

    def unload(self):
        print("Dummy runtime unloaded")


RUNTIME_REGISTRY.register("dummy", DummyRuntime)
