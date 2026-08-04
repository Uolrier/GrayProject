from backend.app.ai.rag.ingestion.loaders.cpp import CppLoader


def test_cpp_loader(tmp_path):
    cpp_file = tmp_path / "main.cpp"

    cpp_file.write_text(
        """
        #include <iostream>

        int main()
        {
            return 0;
        }
        """,
        encoding="utf-8",
    )

    loader = CppLoader()

    doc = loader.load(str(cpp_file))

    assert "iostream" in doc.page_content

    assert doc.metadata["language"] == "cpp"
