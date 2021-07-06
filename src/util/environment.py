from dotenv import dotenv_values


class Env:

    @staticmethod
    def get_env_variable(key):
        return dotenv_values('.env')[key]
