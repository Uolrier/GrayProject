from reportlab.pdfgen import canvas

from backend.app.ai.rag.ingestion.loaders.pdf import PDFLoader


def create_pdf(path):
    c = canvas.Canvas(str(path))

    c.drawString(
        100,
        750,
        "GrayProject PDF Loader Test",
    )

    c.save()


def test_pdf_loader(tmp_path):
    pdf = tmp_path / "test.pdf"

    create_pdf(pdf)

    loader = PDFLoader(str(pdf))

    docs = loader.load()

    assert len(docs) == 1
    assert "GrayProject" in docs[0].page_content
    assert docs[0].metadata["page"] == 1
    assert docs[0].metadata["type"] == "pdf"
