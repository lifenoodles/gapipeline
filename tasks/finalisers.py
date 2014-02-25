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
        if not hasattr(message, "description"):
            message.description = description
        else:
            message.description.update(description)
        return message


@pypline.provides("description")
class ResultsBuilder(pypline.Task):
    def process(self, message, pipeline):
        import time
        now = time.time()
        description = {"best": message.best,
                       "best_fitness": message.best.fitness,
                       "generation": message.generation,
                       "end_time": now,
                       "duration": now - message.start_time}
        if not hasattr(message, "description"):
            message.description = description
        else:
            message.description.update(description)
        return message


@pypline.requires("description")
class ResultsPrinter(pypline.Task):
    def process(self, message, pipeline):
        print "-" * 10
        for k, v in message.description.items():
            print "%s: %s" % (k, v)
        print "-" * 10
        return message


@pypline.requires("description")
class MongoDbSaver(pypline.Task):
    def __init__(self, username, password, db, collection,
                 server="localhost", port="27017"):
        self.username = username
        self.password = password
        self.db = db
        self.collection = collection
        self.server = server
        self.port = port

    def process(self, message, pipeline):
        import pymongo
        connection_string = "mongodb://%s:%s@%s:%s/%s" % \
            (self.username, self.password, self.server, self.db, self.port)
        try:
            client = pymongo.MongoClient(
                "mongodb://ga_user:ga_user@lifenoodles.com:27018/ga")
            db = client[self.db]
            results = db[self.collection]
            results.insert(message.description)
        except Exception as e:
            print "Error connecting to db with connection string: %s" % \
                connection_string
            raise e
