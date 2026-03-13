from project.category import Category
from project.document import Document
from project.topic import Topic

class Storage:

    def __init__(self):
        self.categories: list = []
        self.topics: list = []
        self.documents: list = []

    def add_category(self, category: Category):
        curr_category = next((x for x in self.categories if x.name == category.name), None)
        if curr_category is None:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        curr_category = next((x for x in self.categories if x.id == category_id), None)
        category_index = self.categories.index(curr_category)
        self.categories[category_index].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        curr_topic = next((x for x in self.topics if x.id == topic_id), None)
        topic_index = self.topics.index(curr_topic)
        self.topics[topic_index].topic, self.topics[topic_index].storage_folder = new_topic, new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        curr_document = next((x for x in self.documents if x.id == document_id), None)
        document_index = self.documents.index(curr_document)
        self.documents[document_index].file_name = new_file_name

    def delete_category(self, category_id: int):
        curr_category = next((x for x in self.categories if x.id == category_id), None)
        self.categories.remove(curr_category)

    def delete_topic(self, topic_id: int):
        curr_topic = next((x for x in self.topics if x.id == topic_id), None)
        self.topics.remove(curr_topic)

    def delete_document(self, document_id: int):
        curr_document = next((x for x in self.documents if x.id == document_id), None)
        self.documents.remove(curr_document)

    def get_document(self, document_id):

        return ' '.join([str(x) for x in self.documents if x.id == document_id])

    def __repr__(self):
        documents = [x for x in self.documents]
        final_result = []
        final_result.extend(documents)
        return '\n'.join(map(str, final_result))