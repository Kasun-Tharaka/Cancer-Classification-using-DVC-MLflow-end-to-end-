from cnnClassifier import logger
from cnnClassifier.pipeline.st_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.st_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.st_03_model_trainer import ModelTrainigPipeline
from cnnClassifier.pipeline.st_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingedestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"

try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training"

try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    trainig = ModelTrainigPipeline()
    trainig.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'Evaluation'

try:
    logger.info(f">>>>>>>>>>>>>>>Stage {STAGE_NAME} started successfully<<<<<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>Stage {STAGE_NAME} completed successfully<<<<<<<<\n\n********************\n")
except Exception as e:
        logger.exception(e)
        raise e