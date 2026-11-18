from django.db import models
from django.conf import settings


class Project(models.Model):
    """
    Needed fields
    - members (m2m field to CustomUser; create through table and enforce unique constraint for user and project)
    - name (max_length=100)
    - max_members (positive int)
    - status (choice field integer type :- 0(To be started)/1(In progress)/2(Completed), with default value been 0)

    Add string representation for this model with project name.
    """

    TO_BE_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

    STATUS_CHOICES = [
        (TO_BE_STARTED, "To be started"),
        (IN_PROGRESS, "In progress"),
        (COMPLETED, "Completed"),
    ]
    name = models.CharField(max_length=100)
    max_members = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=TO_BE_STARTED)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through="ProjectMember")

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    """
    Needed fields
    - project (fk to Project model)
    - member (fk to User model - use AUTH_USER_MODEL from settings)
    - Add unique constraints

    Add string representation for this model with project name and user email/first name.
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "member"], name="unique_project_member"
            )
        ]

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name}-{self.project.name}"
