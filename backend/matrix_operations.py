import numpy as np
from logger_config import logger

class MatrixCalculator:

    @staticmethod
    def add_matrices(matrix_a, matrix_b):
        try:
            result = np.add(matrix_a, matrix_b)
            logger.info("Matrices added successfully.")
            return result.tolist()
        except ValueError as ve:
            logger.error(f"ValueError in add_matrices: {str(ve)}")
            raise
        except Exception as e:
            logger.error(f"Exception in add_matrices: {str(e)}")
            raise
    