from services.class_service import ClassService

class ClassController:

    def __init__(self):
        self.class_service = ClassService()

    def get_all_classes(self):

        classes = self.class_service.get_all_classes()

        return classes

    def add_class(
            self,
            class_name,
            teacher_id
    ):
        return self.class_service.add_class(
            class_name,
            teacher_id
        )
    
    def update_class(
            self,
            class_id,
            class_name,
            teacher_id
    ):
        return self.class_service.update_class(
            class_id,
            class_name,
            teacher_id
        )
    
    def delete_class(
            self,
            class_id
    ):
        return self.class_service.delete_class(
            class_id
        )
    
    