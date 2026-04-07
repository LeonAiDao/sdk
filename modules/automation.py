from src.core.engine import LeonEngine

class AutomationModule:
    def __init__(self):
        self.engine = LeonEngine()

    def run_task(self, task_name):
        result = self.engine.process(task_name)
        return f"Automation result: {result}"
