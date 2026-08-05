class UpdateStrategy:
    """
    Base strategy for deciding whether index should update.
    """

    def should_update(
        self,
        old_metadata,
        new_metadata,
    ) -> bool:
        """
        Decide whether update is required.
        """

        if old_metadata is None:
            return True

        if new_metadata is None:
            return False

        return old_metadata != new_metadata
