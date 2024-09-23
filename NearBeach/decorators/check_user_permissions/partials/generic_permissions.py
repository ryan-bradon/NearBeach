from django.core.exceptions import PermissionDenied
from django.db.models import Max, Q
from functools import wraps

from NearBeach.models import Group, ObjectAssignment, UserGroup


def generic_permissions(request, object_lookup, kwargs, extra_permissions):
    # Default user level is 0
    user_group_results = UserGroup.objects.filter(
        is_deleted=False,
        username=request.user,
    )

    # If we are passing the object_lookup through, we will use a different function
    if len(kwargs) > 0:
        # Determine if there are any cross over with user groups and object_lookup groups
        group_results = Group.objects.filter(
            Q(
                is_deleted=False,
                # The object_lookup groups
                group_id__in=ObjectAssignment.objects.filter(
                    is_deleted=False,
                    **{object_lookup: kwargs["location_id"]},
                ).values("group_id"),
            )
            & Q(group_id__in=user_group_results.values("group_id"))
        )

        # Check to make sure the user groups intersect
        if len(group_results) == 0:
            # There are no matching groups - i.e. the user does not have any permission
            return False, 0, False

    # Get the max permission value from user_group_results
    user_level = user_group_results.aggregate(
        Max(f"permission_set__{object_lookup.replace('_id', '')}")
    )[f"permission_set__{object_lookup.replace('_id', '')}__max"]

    extra_level = False
    if extra_permissions == "document":
        extra_level = user_group_results.filter(
            permission_set__document=1,
        ).count() > 0

    # TODO: Implement a more generic version, so we can include other objects like requirements, organisations, customers etc.
    if object_lookup in ["project", "task"]:
        if extra_permissions == "history":
            extra_level = user_group_results.filter(
                **{F"permission_set__{object_lookup}_history": 1}
            ).count() > 0

    return True, user_level, extra_level
