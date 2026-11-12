import json

# Add code to this util to return all users list in specified format.
# [ {
#   "id": 1,
#   "first_name": "Amal",
#   "last_name": "Raj",
#   "email": "amal.raj@joshtechnologygroup.com"
# },
# {
#   "id": 2,
#   "first_name": "Gurpreet",
#   "last_name": "Singh",
#   "email": "gurpreet.singh@joshtechnologygroup.com"
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.


def fetch_all_users():
    """
    Util to fetch given user's tod list
    :return: list of dicts - List of users data
    """
    # Write your code here
    pass


# Add code to this util to  return all todos list (done/to do) along with user details in specified format.
# [{
#   "id": 1,
#   "name": "Complete Timesheet",
#   "status": "Done",
#   "created_at": "4:30 PM, 12 Dec, 2021"
#   "creator" : {
#       "first_name": "Amal",
#       "last_name": "Raj",
#       "email": "amal.raj@joshtechnologygroup.com",
#   }
# },
# {
#   "id": 2,
#   "name": "Complete Python Assignment",
#   "status": "To Do",
#   "created_at": "5:30 PM, 13 Dec, 2021",
#   "creator" : {
#      "first_name": "Gurpreet",
#       "last_name": "Singh",
#       "email": "gurpreet.singh@joshtechnologygroup.com",
#   }
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_all_todo_list_with_user_details():
    """
    Util to fetch given user's tod list
    :return: list of dicts - List of todos
    """
    # Write your code here
    pass


# Add code to this util to return all projects with following details in specified format.
# [{
#   "id": 1,
#   "name": "Project A",
#   "status": "Done",
#   "existing_member_count": 4,
#   "max_members": 5
# },
# {
#   "id": 2,
#   "name": "Project C",
#   "status": "To Do",
#   "existing_member_count": 2,
#   "max_members": 4
# }]
# Note: use serializer for generating this format. use source for status in serializer field.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_projects_details():
    """
    Util to fetch all project details
    :return: list of dicts - List of project with details
    """
    # Write your code here
    pass


# Add code to this util to  return stats (done & to do count) of all users in specified format.
# [{
#   "id": 1,
#   "first_name": "Amal",
#   "last_name": "Raj",
#   "email": "amal.raj@joshtechnologygroup.com",
#   "completed_count": 3,
#   "pending_count": 4
# },
# {
#   "id": 2,
#   "first_name": "Gurpreet",
#   "last_name": "Singh",
#   "email": "gurpreet.singh@joshtechnologygroup.com",
#   "completed_count": 5,
#   "pending_count": 0
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_users_todo_stats():
    """
    Util to fetch todos list stats of all users on platform
    :return: list of dicts -  List of users with stats
    """
    # Write your code here
    pass


# Add code to this util to return top five users with maximum number of pending todos in specified format.
# [{
#   "id": 1,
#   "first_name": "Nikhil",
#   "last_name": "Khurana",
#   "email": "nikhil.khurana@joshtechnologygroup.com",
#   "pending_count": 10
# },
# {
#   "id": 2,
#   "first_name": "Naveen",
#   "last_name": "Kumar",
#   "email": "naveenk@joshtechnologygroup.com",
#   "pending_count": 4
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_five_users_with_max_pending_todos():
    """
    Util to fetch top five user with maximum number of pending todos
    :return: list of dicts -  List of users
    """
    # Write your code here
    pass


# Add code to this util to return users with given number of pending todos in specified format.
# e.g where n=4
# [{
#   "id": 1,
#   "first_name": "Nikhil",
#   "last_name": "Khurana",
#   "email": "nikhil.khurana@joshtechnologygroup.com",
#   "pending_count": 4
# },
# {
#   "id": 2,
#   "first_name": "Naveen",
#   "last_name": "Kumar",
#   "email": "naveenk@joshtechnologygroup.com",
#   "pending_count": 4
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
# Hint : use annotation and aggregations
def fetch_users_with_n_pending_todos(n):
    """
    Util to fetch top five user with maximum number of pending todos
    :param n: integer - count of pending todos
    :return: list of dicts -  List of users
    """
    # Write your code here
    pass


# Add code to this util to return todos that were created in between given dates (add proper order too) and marked as
# done in specified format.
#  e.g. for given range - from 12-01-2021 to 12-02-2021
# [{
#   "id": 1,
#   "creator": "Amal Raj"
#   "email": "amal.raj@joshtechnologygroup.com"
#   "name": "Complete Timesheet",
#   "status": "Done",
#   "created_at": "4:30 PM, 12 Jan, 2021"
# },
# {
#   "id": 2,
#   "creator": "Nikhil Khurana"
#   "email": "nikhil.khurana@joshtechnologygroup.com"
#   "name": "Complete Python Assignment",
#   "status": "Done",
#   "created_at": "5:30 PM, 02 Feb, 2021"
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_completed_todos_with_in_date_range(start, end):
    """
    Util to fetch todos that were created in between given dates and marked as done.
    :param start: string - Start date e.g. (12-01-2021)
    :param end: string - End date e.g. (12-02-2021)
    :return: list of dicts - List of todos
    """
    # Write your code here
    pass


# Add code to this util to return list of projects having members who have name either starting with A or ending with A
# (case-insensitive) in specified format.
# [{
#   "project_name": "Project A"
#   "done": False
#   "max_members": 3
#   },
#   {
#   "project_name": "Project B"
#   "done": False
#   "max_members": 3
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_project_with_member_name_start_or_end_with_a():
    """
    Util to fetch project details having members who have name either starting with A or ending with A.
    :return: list of dicts - List of project data
    """
    # Write your code here
    pass


# Add code to this util to return project wise todos stats per user in specified format.
# [{
#   "project_title": "Project A"
#   "report": [
#       {
#           "first_name": "Amal",
#           "last_name": "Raj",
#           "email": "amal.raj@joshtechnologygroup.com",
#           "pending_count": 1,
#           "completed_count": 1,
#       },
#       {
#           "first_name": "Nikhil",
#           "last_name": "Khurana",
#           "email": "nikhil.khurana@joshtechnologygroup.com",
#           "pending_count": 0,
#           "completed_count": 5,
#       }
#   ]
# },
# {
#   "project_title": "Project B"
#   "report": [
#       {
#           "first_name": "Gurpreet",
#           "last_name": "Singh",
#           "email": "gurpreet.singh@joshtechnologygroup.com",
#           "pending_count": 12,
#           "completed_count": 15,
#       },
#       {
#           "first_name": "Naveen",
#           "last_name": "Kumar",
#           "email": "naveenk@joshtechnologygroup.com",
#           "pending_count": 12,
#           "completed_count": 5,
#       }
#   ]
# }]
# Note: use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
def fetch_project_wise_report():
    """
    Util to fetch project wise todos pending &  count per user.
    :return: list of dicts - List of report data
    """
    # Write your code here
    pass


# Add code to this util to return all users project stats in specified format.
# [{
#   "first_name": "Amal",
#   "last_name": "Raj",
#   "email": "amal.raj@joshtechnologygroup.com",
#   "projects" : {
#       "to_do": ["Project A", "Project C"],
#       "in_progress": ["Project B", "Project E"],
#       "completed": ["Project R", "Project L"],
#   }
# },
# {
#   "first_name": "Nikhil",
#   "last_name": "Khurana",
#   "email": "nikhil.khurana@joshtechnologygroup.com",
#   "projects" : {
#       "to_do": ["Project C"],
#       "in_progress": ["Project B", "Project F"],
#       "completed": ["Project K", "Project L"],
#   }
# }]
# Note: Use serializer for generating this format.
# use json.load(json.dumps(serializer.data)) while returning data from this function for test cases to pass.
# Hint: Use subquery/aggregation for project data.
def fetch_user_wise_project_status():
    """
    Util to fetch user wise project statuses.
    :return: list of dicts - List of user project data
    """
    # Write your code here
    pass
