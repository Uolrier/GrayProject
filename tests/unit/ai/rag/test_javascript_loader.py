from backend.app.ai.rag.ingestion.loaders.javascript import (
    JavaScriptLoader,
)


def test_javascript_loader(tmp_path):
    file = tmp_path / "app.ts"

    file.write_text(
        """
        function hello(name:string){
            return "hello " + name;
        }
        """,
        encoding="utf-8",
    )

    loader = JavaScriptLoader()

    doc = loader.load(str(file))

    assert "function hello" in doc.page_content

    assert doc.metadata["language"] == "typescript"

    assert doc.metadata["extension"] == ".ts"
