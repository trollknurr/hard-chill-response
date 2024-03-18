from application.port.input.vector_db import VectorInputPort


class VectorService(VectorInputPort):
    def __init__(self, vector_port):
        self.vector_port = vector_port

    def store_vector(self, vector_data):
        pass

    def retrieve_vector(self, vector_id):
        pass

    def find_similar_vectors(self, **kwargs):
        # Think that will be heavily used in future
        pass
