import pypline


class KeyPressWaiter(pypline.Task):
    def process(self, message, pipeline):
        raw_input()
        return message
