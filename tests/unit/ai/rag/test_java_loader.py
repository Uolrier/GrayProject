from pathlib import Path

from backend.app.ai.rag.ingestion.loaders.java import JavaLoader


def test_java_loader(tmp_path: Path):
    java_file = tmp_path / "Hello.java"

    java_file.write_text(
        """
        public class Hello {
            public static void main(String[] args) {
                System.out.println("Hello");
            }
        }
        """,
        encoding="utf-8",
    )

    loader = JavaLoader()

    doc = loader.load(str(java_file))

    assert "public class Hello" in doc.page_content

    assert doc.metadata["type"] == "java"

    assert doc.metadata["language"] == "java"
