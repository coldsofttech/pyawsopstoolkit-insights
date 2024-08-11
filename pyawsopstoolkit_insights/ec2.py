from dataclasses import dataclass

from pyawsopstoolkit_insights.__validations__ import _validate_type


@dataclass
class SecurityGroup:
    """
    A class representing insights related with EC2 security groups.
    """
    from pyawsopstoolkit.session import Session

    session: Session

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        from pyawsopstoolkit.session import Session

        field_value = getattr(self, field_name)
        if field_name in ['session']:
            _validate_type(field_value, Session, f'{field_name} should be of Session type.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def unused_security_groups(self) -> list:
        """
        Returns a list of unused EC2 security groups.
        """
        from pyawsopstoolkit_advsearch.ec2 import SecurityGroup

        sg_object = SecurityGroup(self.session)
        security_groups = sg_object.search_security_groups(include_usage=True, in_use=False)

        if security_groups is None:
            return []

        return security_groups
