from abc import ABC, abstractmethod


class BaseRuntime(ABC):
    """
    Local inference runtime abstract interface.

    All local model runtimes should inherit from this class.
    """

    @abstractmethod
    def load(self):
        """
        Load model resources.
        """
        pass

    @abstractmethod
    def generate(self, prompt: str, **kwargs):
        """
        Generate response from model.

        Args:
            prompt: Input text.
            **kwargs: Additional generation parameters.

        Returns:
            Generated text response.
        """
        pass

    @abstractmethod
    def unload(self):
        """
        Release model resources.
        """
        pass
