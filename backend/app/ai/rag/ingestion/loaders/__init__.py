from .html import HTMLLoader
from .markdown import MarkdownLoader
from .pdf import PDFLoader
from .text import TextLoader
from .word import WordLoader

__all__ = [
    "TextLoader",
    "MarkdownLoader",
    "PDFLoader",
    "HTMLLoader",
    "WordLoader",
]
