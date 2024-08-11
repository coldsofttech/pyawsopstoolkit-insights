# pyawsopstoolkit_insights

The **pyawsopstoolkit_insights** package offers a comprehensive array of features designed to clean up and maintain
hygiene within AWS (Amazon Web Services). It includes tools for identifying unused IAM roles, EC2 Security Groups, and
more. Meticulously engineered, these features are finely tuned to meet the unique demands of the expansive AWS
ecosystem, encompassing a diverse spectrum of aspects.

## Getting Started

Ready to supercharge your AWS operations? Let's get started with **pyawsopstoolkit_insights**!

### Installation

Install **pyawsopstoolkit_insights** via pip:

```bash
pip install pyawsopstoolkit_insights
```

## Documentation

- [iam](#iam)

### iam

This **pyawsopstoolkit_insights.iam** subpackage offers sophisticated insights specifically designed for AWS (Amazon Web
Services) Identity and Access Management (IAM). It provides tools to analyze and manage IAM roles and users, ensuring
efficient and secure AWS operations.

#### Role

The **Role** class represents insights related to IAM roles.

##### Constructors

- `Role(session: Session) -> None`: Initializes a new **Role** object with the provided session.

##### Methods

- `unused_roles(no_of_days: Optional[int] = 90, include_newly_created: Optional[bool] = False) -> list`: Returns a list
  of unused IAM roles based on the specified parameters.

##### Properties

- `session`: An `pyawsopstoolkit.session.Session` object providing access to AWS services.

##### Usage

```python
from pyawsopstoolkit.session import Session
from pyawsopstoolkit_insights.iam import Role

# Create a session using the default profile
session = Session(profile_name='default')

# Initialize the IAM Role object
role_object = Role(session=session)

# Retrieve IAM roles unused for the last 90 days
unused_roles = role_object.unused_roles()

# Print the list of unused roles
print(unused_roles)
```

#### User

The **User** class represents insights related to IAM users.

##### Constructors

- `User(session: Session) -> None`: Initializes a new **User** object with the provided session

##### Methods

- `unused_users(no_of_days: Optional[int] = 90, include_newly_created: Optional[bool] = False) -> list`: Returns a list
  of unused IAM users based on the specified parameters.

##### Properties

- `session`: An `pyawsopstoolkit.session.Session` object providing access to AWS services.

##### Usage

```python
from pyawsopstoolkit.session import Session
from pyawsopstoolkit_insights.iam import User

# Create a session using the default profile
session = Session(profile_name='default')

# Initialize the IAM User object
user_object = User(session=session)

# Retrieve IAM users unused for the last 90 days
unused_users = user_object.unused_users()

# Print the list of unused users
print(unused_users)
```

# License

Please refer to the [MIT License](LICENSE) within the project for more information.

# Contributing

We welcome contributions from the community! Whether you have ideas for new features, bug fixes, or enhancements, feel
free to open an issue or submit a pull request on [GitHub](https://github.com/coldsofttech/pyawsopstoolkit-insights).