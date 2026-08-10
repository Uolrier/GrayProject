from dataclasses import dataclass
from threading import Lock


@dataclass
class GenerationTask:
    """
    单个生成任务。
    """

    cancelled: bool = False


class GenerationManager:
    """
    管理正在进行中的生成任务。
    """

    def __init__(self) -> None:
        self._tasks: dict[str, GenerationTask] = {}
        self._lock = Lock()

    def create(self, task_id: str) -> None:
        with self._lock:
            self._tasks[task_id] = GenerationTask()

    def cancel(self, task_id: str) -> bool:
        with self._lock:
            task = self._tasks.get(task_id)
            if task is None:
                return False
            task.cancelled = True
            return True

    def is_cancelled(self, task_id: str) -> bool:
        with self._lock:
            task = self._tasks.get(task_id)

            if task is None:
                return False

            return task.cancelled

    def remove(self, task_id: str) -> None:
        with self._lock:
            self._tasks.pop(task_id, None)


generation_manager = GenerationManager()
