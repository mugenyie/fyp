# src/models/ProjectModel.py
import datetime, uuid
from marshmallow import fields, Schema
from . import db, BaseModel


class ProjectModel(BaseModel):

    """ Project Model """
    __tablename__ = 'projects'

    name = db.Column(db.String(128), nullable=False)
    git_url = db.Column(db.String(128), nullable=True)
    web_url = db.Column(db.String(128), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    score = db.Column(db.Integer, nullable=False, default=0)
    proposal_file = db.Column(db.String(128), nullable=True)
    documentation_file = db.Column(db.String(128), nullable=True)
    supervisor_id = db.Column(db.String, db.ForeignKey('supervisors.id'), nullable=True)
    group_id = db.Column(db.String, db.ForeignKey('groups.id'), nullable=True)
    created_by = db.Column(db.String(128), nullable=False)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.id = data.get('id')
        self.name = data.get('name')
        self.git_url = data.get('git_url')
        self.web_url = data.get('web_url')
        self.score = data.get('score')
        self.proposal_file = data.get('proposal_file')
        self.documentation_file = data.get('documentation_file')
        self.created_by = data.get('created_by')
        self.description = data.get('description')
        self.supervisor_id = data.get('supervisor_id')
        self.group_id = data.get('group_id')

    def __str__(self):
        return "<id: {}>".format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_project(project_id):
        return ProjectModel.query.get(project_id)

    @staticmethod
    def view_all_projects():
        return ProjectModel.query.all()

    @staticmethod
    def get_by_supervisor(supervisor_id):
        return ProjectModel.query.filter_by(supervisor_id=supervisor_id).order_by(ProjectModel.created_on.desc())
    
    @staticmethod
    def get_by_createdby(student_id):
        return ProjectModel.query.filter_by(created_by=student_id).first()

    @staticmethod
    def get_by_groupid(group_id):
        return ProjectModel.query.filter_by(group_id=group_id).first()


class ProjectSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=True)
    git_url = fields.Str(required=False)
    web_url = fields.Str(required=False)
    score = fields.Int(required=False)
    proposal_file = fields.Str(required=False)
    documentation_file = fields.Str(required=False)
    created_by = fields.Str(required=True)
    description = fields.Str(required=True)
    supervisor_id = fields.Str(required=False)
    group_id = fields.Str(required=False)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)