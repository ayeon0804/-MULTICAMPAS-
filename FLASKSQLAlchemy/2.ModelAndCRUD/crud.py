from model import db, Puppy

# insert
'''
my_puppy = Puppy('dully',5)
db.session.add(my_puppy)
db.session.commit()
'''

# read
all_puppies = Puppy.query.all()
print(all_puppies)

puppy_one = Puppy.query.get(1)
print(puppy_one.name, puppy_one.age)
print('='*3)
puppy_sam = Puppy.query.filter_by(name='Sammy')
print(puppy_sam)

# update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# delete
third_puppy = Puppy.query.get(3)
db.session.delete(third_puppy)
db.session.commit()