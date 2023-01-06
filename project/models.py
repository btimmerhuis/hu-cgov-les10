from project import db


class todo_item(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    action = db.Column(db.String)

    def __init__(self, action: str):
        self.action = action

    def __repr__(self):
        return f'{self.id}: {self.action}'
