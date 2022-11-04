from Enceladus.jobs import TrainingPipeline
from Enceladus.utils import GetConfiguration

pipeline, model, sweep = GetConfiguration().run('config.ini')
worker = TrainingPipeline(
    config=pipeline,
    model_config=model,
    sweep_config=sweep,
    no_sweep=True,
)
worker.run()