import argparse
import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DEFAULT_OUTPUT = BASE_DIR / "assets" / "rag_large_dataset"


TOPICS = [
    "GrayProject Architecture",
    "RAG Pipeline Design",
    "Embedding System",
    "Knowledge Base Management",
    "Vector Database",
    "LLM Runtime",
    "Agent System",
]


def generate_markdown(path: Path, index: int):
    content = f"""
# {random.choice(TOPICS)}

Document ID: {index}

GrayProject is an AI management system.

This document describes RAG architecture,
knowledge retrieval,
embedding pipeline,
and vector database design.

## Components

- Loader
- Chunker
- Embedding
- Retriever
- Reranker

The system supports incremental indexing
and multiple knowledge bases.
"""

    path.write_text(
        content,
        encoding="utf-8",
    )


def generate_text(path: Path, index: int):
    content = f"""
GrayProject Text Document {index}

This is a large scale RAG testing document.

The knowledge base contains documents,
chunks,
embeddings,
and retrieval information.
"""

    path.write_text(
        content,
        encoding="utf-8",
    )


def generate_python(path: Path, index: int):
    content = f'''
class DocumentProcessor{index}:

    def process(self, document):
        """
        Process document in RAG pipeline.
        """
        return document


def build_embedding(index):
    return {{
        "id": index,
        "status": "created"
    }}
'''

    path.write_text(
        content,
        encoding="utf-8",
    )


def generate_json(path: Path, index: int):
    data = {
        "id": index,
        "project": "GrayProject",
        "type": "knowledge",
        "features": [
            "rag",
            "embedding",
            "retrieval",
        ],
    }

    path.write_text(
        json.dumps(
            data,
            indent=2,
        ),
        encoding="utf-8",
    )


def generate_html(path: Path, index: int):
    content = f"""
<html>
<body>

<h1>GrayProject Document {index}</h1>

<p>
RAG system performance testing.
</p>

</body>
</html>
"""

    path.write_text(
        content,
        encoding="utf-8",
    )


def create_dataset(
    output: Path,
    count: int,
):
    folders = {
        "markdown": output / "markdown",
        "text": output / "text",
        "python": output / "python",
        "json": output / "json",
        "html": output / "html",
    }

    for folder in folders.values():
        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

    for index in range(count):
        selector = index % 10

        if selector < 4:
            generate_markdown(
                folders["markdown"] / f"doc_{index}.md",
                index,
            )

        elif selector < 6:
            generate_text(
                folders["text"] / f"doc_{index}.txt",
                index,
            )

        elif selector < 8:
            generate_python(
                folders["python"] / f"doc_{index}.py",
                index,
            )

        elif selector == 8:
            generate_json(
                folders["json"] / f"doc_{index}.json",
                index,
            )

        else:
            generate_html(
                folders["html"] / f"doc_{index}.html",
                index,
            )

    return output


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--count",
        type=int,
        default=1000,
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
    )

    args = parser.parse_args()

    result = create_dataset(
        args.output,
        args.count,
    )

    print(f"Dataset generated: {result}")

    print(f"Documents: {args.count}")


if __name__ == "__main__":
    main()
