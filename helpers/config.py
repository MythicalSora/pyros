import yaml


class Config():
    def __init__(self, file):
        self.file = file

    def read_config(self):
        with open(self.file, 'r') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        return self.config
