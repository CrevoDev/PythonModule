from python_module import Inject, Module

class Provider:
    _log = "Provider Injetado"

    @classmethod
    def set_log(cls, log):
        cls._log = log
        return cls

    def get(self):
        return self._log

@Inject(module_name="ModuleExemple")
class ServiceBase:
    def __init__(self, provider: Provider):
        self.provider = provider

    def get_log(self):
        return self.provider.get()

class Service(ServiceBase):
    def __init__(self):
        super().__init__()

    def process(self):
        print(self.get_log())
        return 'Service processed'


@Module(
    module_name="ModuleExemple",
    instances=[Provider.set_log("Log alterado!")]
)
class ModuleExemple:
    def run(self):
        service = Service()
        return service.process()


if __name__ == '__main__':
    module_exemple = ModuleExemple()
    print(module_exemple.run())