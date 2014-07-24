import pypline


@pypline.requires("trials")
class BoundsConstrainer(pypline.Task):
    def process(self, message, pipeline):
        for trial in message.trials:
            for i, gene in enumerate(trial.genes):
                if gene < message.lower:
                    trial.genes[i] = message.lower
                elif gene > message.upper:
                    trial.genes[i] = message.upper
        return message

    def getDescription(self):
        return {"constrainer": "Bounds"}
