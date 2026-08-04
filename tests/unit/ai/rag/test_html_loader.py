from pathlib import Path

from backend.app.ai.rag.ingestion.loaders.html import HTMLLoader


def test_html_loader(tmp_path: Path):
    html_file = tmp_path / "test.html"

    html_file.write_text(
        """
        <html>
            <head>
                <style>
                    body {color:red;}
                </style>
                <script>
                    alert("test");
                </script>
            </head>

            <body>
                <h1>GrayProject</h1>
                <p>
                    RAG HTML Loader Test
                </p>
            </body>
        </html>
        """,
        encoding="utf-8",
    )

    loader = HTMLLoader(str(html_file))

    docs = loader.load()

    assert len(docs) == 1

    document = docs[0]

    assert "GrayProject" in document.page_content

    assert "RAG HTML Loader Test" in document.page_content

    assert "alert" not in document.page_content

    assert document.metadata["type"] == "html"
