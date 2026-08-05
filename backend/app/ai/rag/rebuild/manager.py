from .schema import RebuildRequest


class RebuildManager:
    """
    Manage full index rebuild.
    """

    def __init__(
        self,
        collection_manager=None,
        metadata_manager=None,
        tracker=None,
        scanner=None,
        document_loader=None,
        pipeline=None,
    ):
        self.collection_manager = collection_manager

        self.metadata_manager = metadata_manager

        self.tracker = tracker

        self.scanner = scanner

        self.document_loader = document_loader

        self.pipeline = pipeline

    def rebuild(
        self,
        request: RebuildRequest,
    ):
        """
        Delete old index and rebuild.
        """

        if request.drop_collection and self.collection_manager:
            self.collection_manager.delete(request.collection)

        if self.metadata_manager:
            self.metadata_manager.clear_collection(request.collection)

        if self.tracker:
            self.tracker.reset()

        documents = []

        if self.scanner and self.document_loader:
            files = self.scanner.scan(request.source_path)

            for file in files:
                documents.extend(self.document_loader(file))

        if self.pipeline:
            return self.pipeline.run(documents)

        return {
            "documents": len(documents),
        }
