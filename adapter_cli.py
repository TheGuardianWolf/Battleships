from adapter import Adapter


class AdapterCLI(Adapter):
    def get_grid(self, prompt):
        return int(input(prompt))

    def get_bool(self, prompt):
        return int(input(prompt)) > 0
