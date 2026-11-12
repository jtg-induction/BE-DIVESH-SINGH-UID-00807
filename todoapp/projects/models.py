from django.db import models


class Project(models.Model):
    """
    Needed fields
    - members (m2m field to CustomUser; create through table and enforce unique constraint for user and project)
    - name (max_length=100)
    - max_members (positive int)
    - status (choice field integer type :- 0(To be started)/1(In progress)/2(Completed), with default value been 0)

    Add string representation for this model with project name.
    """


class ProjectMember(models.Model):
    """
    Needed fields
    - project (fk to Project model)
    - member (fk to User model - use AUTH_USER_MODEL from settings)
    - Add unique constraints

    Add string representation for this model with project name and user email/first name.
    """
