from models import User, Contact, Role
from db import db
from sqlalchemy.exc import NoSuchTableError
user_count = ''

initial_users = [
    {'id': 1,
  'first_name': 'Jessica',
  'last_name': 'Bailey',
  'active': True,
  'company': 'Data Analytics',
  'sex': 'M'},
 {'id': 2,
  'first_name': 'Joseph',
  'last_name': 'Young',
  'active': False,
  'company': 'Tech Innovations',
  'sex': 'M'},
 {'id': 3,
  'first_name': 'Elizabeth',
  'last_name': 'Lamb',
  'active': False,
  'company': 'Pathfinders',
  'sex': 'F'},
 {'id': 4,
  'first_name': 'Shawn',
  'last_name': 'Green',
  'active': True,
  'company': 'Tech Innovations',
  'sex': 'F'},
 {'id': 5,
  'first_name': 'Robert',
  'last_name': 'Miller',
  'active': False,
  'company': 'Global Corp',
  'sex': 'F'},
 {'id': 6,
  'first_name': 'Kristen',
  'last_name': 'Snyder',
  'active': True,
  'company': 'Pathfinders',
  'sex': 'F'},
 {'id': 7,
  'first_name': 'Linda',
  'last_name': 'Mayer',
  'active': False,
  'company': 'Data Analytics',
  'sex': 'F'},
 {'id': 8,
  'first_name': 'Stephen',
  'last_name': 'Bush',
  'active': True,
  'company': 'NextGen',
  'sex': 'F'},
 {'id': 9,
  'first_name': 'Kyle',
  'last_name': 'Salinas',
  'active': True,
  'company': 'Kasablanca',
  'sex': 'M'},
 {'id': 10,
  'first_name': 'Frances',
  'last_name': 'Aguilar',
  'active': False,
  'company': 'NextGen',
  'sex': 'M'}
]

user_contacts = [
{'id': 1,
  'phone': '+8801878568625',
  'address': '0250 Diane Alley\nSouth Michael, IA 06331',
  'city': 'Sylhet',
  'country': 'Bangladesh'},
 {'id': 2,
  'phone': '+8801825757177',
  'address': '79593 Miller Cove\nLake Brittanychester, NV 11031',
  'city': 'Comilla',
  'country': 'Bangladesh'},
 {'id': 3,
  'phone': '+8801857615814',
  'address': '44814 Cooper Mall\nLake Karen, IA 14398',
  'city': 'Dhaka',
  'country': 'Bangladesh'},
 {'id': 4,
  'phone': '+8801971738813',
  'address': '6818 Sara Island Apt. 412\nBrettchester, NY 28751',
  'city': 'Dhaka',
  'country': 'Bangladesh'},
 {'id': 5,
  'phone': '+8801923888906',
  'address': '8407 Helen Lock\nStephenberg, KY 77556',
  'city': 'Khulna',
  'country': 'Bangladesh'},
 {'id': 6,
  'phone': '+8801959952974',
  'address': '45536 Shannon Street Apt. 028\nNew Johnland, CO 55240',
  'city': 'Chittagong',
  'country': 'Bangladesh'},
 {'id': 7,
  'phone': '+8801984576756',
  'address': '65313 Kenneth Springs\nArellanoshire, VA 08510',
  'city': 'Sylhet',
  'country': 'Bangladesh'},
 {'id': 8,
  'phone': '+8801701081440',
  'address': '565 Castillo Isle\nWest Scott, ND 54988',
  'city': 'Sylhet',
  'country': 'Bangladesh'},
 {'id': 9,
  'phone': '+8801781137713',
  'address': '63798 Hahn Manor Suite 958\nLewisborough, GA 99922',
  'city': 'Sylhet',
  'country': 'Bangladesh'},
 {'id': 10,
  'phone': '+8801894665223',
  'address': '023 Rita Spring Suite 950\nLake Kristina, MI 50539',
  'city': 'Rajshahi',
  'country': 'Bangladesh'}



]

roles=[
{'id': 1, 'name': 'Manager', 'user_id': 4},
 {'id': 2, 'name': 'Team Lead', 'user_id': 9},
 {'id': 3, 'name': 'Software Engineer', 'user_id': 10},
 {'id': 4, 'name': 'Quality Assurance Analyst', 'user_id': 7},
 {'id': 5, 'name': 'Product Manager', 'user_id': 5},
 {'id': 6, 'name': 'Sales Representative', 'user_id': 3},
 {'id': 7, 'name': 'Human Resources Specialist', 'user_id': 8},
 {'id': 8, 'name': 'Financial Analyst', 'user_id': 2},
 {'id': 9, 'name': 'Marketing Coordinator', 'user_id': 6},
 {'id': 10, 'name': 'Customer Service Representative', 'user_id': 1}
 ]




try:
    user_count = db.session.query(User).count()
except NoSuchTableError:
    user_count = 0

if user_count == 0:
    for user in initial_users:
      new_user = User(**user)
      db.session.add(new_user)
      db.session.commit()

    for contact in user_contacts:
      new_contact = Contact(**contact)
      db.session.add(new_contact)
      db.session.commit()

    for role in roles:
      new_role = Role(**role)
      db.session.add(new_role)
      db.session.commit()

