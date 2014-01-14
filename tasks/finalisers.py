import pypline


@pypline.provides("description")
class DescriptionBuilder(pypline.Task):
    def process(self, message, pipeline):
        description = {}
        tasklist = pipeline._tasks + [pipeline._controller] \
            + pipeline._initialisers + pipeline._finalisers
        for task in tasklist:
            if hasattr(task, "getDescription"):
                description.update(getattr(task, "getDescription")())
        message.description = description
        print description
        return message
