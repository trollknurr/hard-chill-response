from application.port.output.vector_db import VectorPort


class VectorDBAdapter(VectorPort):
    def __init__(self, config):
        # ToDo: create something like this after
        # self.vector_db = load_vector_db(config)
        pass

    def save_vector(self, vector_model):
        # self.vector_db.insert(*)
        pass

    def get_vector_by_id(self, id):
        # return self.vector_db.get_by_id(id)
        pass

    def query_vectors(self, vector_query_model):
        # return self.vector_db.query(*)
        pass
