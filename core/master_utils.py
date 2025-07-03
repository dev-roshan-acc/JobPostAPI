from application.models import Application
from django.core.exceptions import ObjectDoesNotExist,PermissionDenied

class MasterApplicationUtils:
    @staticmethod
    def update_application_status(application_id,user,status):
        try:
            application = Application.objects.get(id=application_id)
            # check if user is the owner of this application
            if application.user != user:
                raise PermissionDenied(
                    "You do not have permission to update this application."
                )
            if application.status !='applied':
                raise PermissionDenied('You can not modify this application')


            # now update status

            application.status = 'withdrawn'
            application.save()
        except ObjectDoesNotExist as odne:
            raise ValueError(
                f"Application with ID {application_id} does not exist."
            ) from odne

        except Exception as e:
            raise e