from repositories.class_repository import ClassRepository

class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository() 

    def get_all_classes(self):
        return self.class_repository.get_all_classes()
    
    def add_class(
            self,
            class_name,
            teacher_id
    ):
        
        return self.class_repository.add_class(
            class_name,
            teacher_id
        )
    
    def update_class(
            self,
            class_id,
            class_name,
            teacher_id
    ):
        
        return self.class_repository.update_class(
            class_id,
            class_name,
            teacher_id
        )
    
    def delete_class(
            self,
            class_id
    ):
        return self.class_repository.delete_class(
            class_id
        )