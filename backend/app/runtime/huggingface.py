from transformers import AutoModelForCausalLM, AutoTokenizer

from backend.app.runtime.base import BaseRuntime
from backend.app.runtime.registry import RuntimeRegistry


class HuggingFaceRuntime(BaseRuntime):
    """
    HuggingFace Transformers based local model runtime.
    """

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B-Instruct",
        device: str = "auto",
    ):
        self.model_name = model_name
        self.device = device

        self.tokenizer = None
        self.model = None

    def load(self):
        """
        Load tokenizer and model.
        """

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map=self.device,
        )

    def generate(self, prompt: str, **kwargs):
        """
        Generate text from local model.
        """

        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model is not loaded. Call load() first.")

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
        )

        outputs = self.model.generate(
            **inputs,
            **kwargs,
        )

        result = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True,
        )

        return result

    def unload(self):
        """
        Release model resources.
        """

        self.model = None
        self.tokenizer = None


RuntimeRegistry.register(
    "qwen_local",
    HuggingFaceRuntime,
)
