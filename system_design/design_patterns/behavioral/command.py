class DeploymentHandler:

    def execute(self):
        self.build_package()
        self.test()
        self.check_coverage()
        self.save_artifacts()
        self.store_package()
        self.deploy()

    def undo(self):
        print("deploy 2nd oldest package in the store")

    def build_package(self):
        print('install/set up dependenices')

    def test(self):
        print('run unit tests')

    def check_coverage(self):
        print('run coversage and check percentage')

    def save_artifacts(self):
        print('save build artificats')

    def store_package(self):
        print("store build package")

    def deploy(self):
        print("deploy package to server")

deployment_handler = DeploymentHandler()
deployment_handler.execute()