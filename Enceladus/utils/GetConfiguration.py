import ast
from configparser import ConfigParser


class GetConfiguration():

    def run(self, path):
        config = ConfigParser()
        config.read(path)
        config.sections()

        pipeline_literals = ['epochs', 'es_patience', 'seed', 'data_size', 'data_split']
        pipeline = self.get_values(config['pipeline'], pipeline_literals)

        model_literals = ['reg_factor_1', 'reg_factor_2']
        model = self.get_values(config['model'], model_literals)

        sweep_literals = ['batch_size', 'learning_rate', 'beta_1', 'beta_2', 'epsilon', 'dropout_1', 'dropout_2']
        sweep = self.get_sweep_values(config['sweep'], sweep_literals)
        return pipeline, model, sweep

    def get_values(self, config, literals):
        out = dict()
        for param, value in config.items():
            if param in literals:
                value = ast.literal_eval(value)
            out[param] = value
        return out

    def get_sweep_values(self, config, literals):
        out = dict()
        for param, value in config.items():
            if param in literals:
                value = ast.literal_eval(value)
            out[param] = dict(values=value)
        
        out = dict(
            method='random',
            metric=dict(
                name='accuracy',
                goal='maximize',
            ),
            parameters=out
        )
        return out