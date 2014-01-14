import pypline


@pypline.provides("description")
class DescriptionBuilder(pypline.Task):
    def process(self, message, pipeline):
        description = {}
        tasklist = pipeline._tasks
        for task in tasklist:
            if hasattr(task, "getDescription"):
                description.update(getattr(task, "getDescription")())
        print description
