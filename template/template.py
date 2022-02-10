from abc import ABC, abstractmethod
import time

class Record(ABC):

    def save_record(self):
        print("generating ID...")
        time.sleep(2)
        self.before_save()
        print("saving to database")
        saved = True
        time.sleep(2)
        if saved:
            self.after_save()
        else:
            print("something went wrong")
        print("finished")

    @abstractmethod
    def before_save(self):
        pass

    @abstractmethod
    def after_save(self):
        pass

class User(Record):

    def before_save(self):
        print("validating input..")
        time.sleep(2)
        print("checking if username exists..")
        time.sleep(2)

    def after_save(self):
        print("user succesfully saved")
        time.sleep(2)

class Post(Record):

    def before_save(self):
        print("validating input..")
        time.sleep(2)
                
    def after_save(self):
        print("post succesfully saved")
        time.sleep(2)

user_saver1 = User()
user_saver1.save_record()

post_saver2 = Post()
post_saver2.save_record()