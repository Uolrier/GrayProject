from .schema import IndexAction


class IndexUpdateManager:
    """
    Manage incremental index update operations.
    """

    def __init__(
        self,
        index_pipeline=None,
        metadata_manager=None,
        vector_store=None,
        loader_adapter=None,
    ):
        self.index_pipeline = index_pipeline

        self.metadata_manager = metadata_manager

        self.vector_store = vector_store

        self.loader_adapter = loader_adapter

    def execute(
        self,
        task,
    ):
        """
        Execute index update task.
        """

        if task.action == IndexAction.ADD:
            return self._add(task)

        if task.action == IndexAction.UPDATE:
            return self._update(task)

        if task.action == IndexAction.DELETE:
            return self._delete(task)

        raise ValueError(f"Unsupported action: {task.action}")

    def _add(
        self,
        task,
    ):
        if self.index_pipeline is None:
            return None

        if self.loader_adapter is None:
            return None

        documents = self.loader_adapter.load(task.path)

        return self.index_pipeline.run(documents)

    def add(
        self,
        document,
    ):
        if self.index_pipeline is None:
            return None

        return self.index_pipeline.add_document(document)

    def _update(
        self,
        task,
    ):
        if self.vector_store is not None:
            self.vector_store.delete(ids=[task.document_id])

        return self._add(task)

    def update(
        self,
        document,
    ):
        if self.index_pipeline is None:
            return None

        return self.index_pipeline.update_document(document)

    def _delete(
        self,
        task,
    ):
        if self.vector_store is not None:
            self.vector_store.delete(ids=[task.document_id])

        if self.metadata_manager is not None:
            self.metadata_manager.delete(task.document_id)

        return True

    def delete(
        self,
        document_id,
    ):
        if self.index_pipeline is None:
            return None

        return self.index_pipeline.delete_document(document_id)
