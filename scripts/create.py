def init_db(db, User, Blog):
    user = User(username="psdon", email="psdon@mail.com", password="psdon")
    db.session.add(user)
    db.session.commit()

    user = User.query.first()

    data = [
        {
            "title": "First Blog",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rutrum, enim vel condimentum rhoncus, est eros sollicitudin justo, at semper nisi nisl id urna. Aenean tincidunt hendrerit sollicitudin. Etiam ac convallis tortor. Aliquam tempus nunc eget lacus tristique facilisis. Cras non nulla suscipit, aliquet felis vitae, cursus risus. Nulla facilisi. Integer ante arcu, egestas a tellus id, egestas ullamcorper turpis. Maecenas libero augue, posuere et tellus ut, rutrum tincidunt leo. Cras mollis lectus et quam tempus, ac ullamcorper lacus lacinia. Quisque porttitor arcu ut ante aliquam, id sodales arcu varius. Vivamus ullamcorper dolor quis dui euismod sollicitudin. Donec molestie dolor ut arcu congue sollicitudin. Integer nec elit euismod, viverra turpis eu, sodales elit. Etiam a eros et sem semper pulvinar vitae a enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
            "title": "2nd Blog",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rutrum, enim vel condimentum rhoncus, est eros sollicitudin justo, at semper nisi nisl id urna. Aenean tincidunt hendrerit sollicitudin. Etiam ac convallis tortor. Aliquam tempus nunc eget lacus tristique facilisis. Cras non nulla suscipit, aliquet felis vitae, cursus risus. Nulla facilisi. Integer ante arcu, egestas a tellus id, egestas ullamcorper turpis. Maecenas libero augue, posuere et tellus ut, rutrum tincidunt leo. Cras mollis lectus et quam tempus, ac ullamcorper lacus lacinia. Quisque porttitor arcu ut ante aliquam, id sodales arcu varius. Vivamus ullamcorper dolor quis dui euismod sollicitudin. Donec molestie dolor ut arcu congue sollicitudin. Integer nec elit euismod, viverra turpis eu, sodales elit. Etiam a eros et sem semper pulvinar vitae a enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
        {
            "title": "Something Interesting",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rutrum, enim vel condimentum rhoncus, est eros sollicitudin justo, at semper nisi nisl id urna. Aenean tincidunt hendrerit sollicitudin. Etiam ac convallis tortor. Aliquam tempus nunc eget lacus tristique facilisis. Cras non nulla suscipit, aliquet felis vitae, cursus risus. Nulla facilisi. Integer ante arcu, egestas a tellus id, egestas ullamcorper turpis. Maecenas libero augue, posuere et tellus ut, rutrum tincidunt leo. Cras mollis lectus et quam tempus, ac ullamcorper lacus lacinia. Quisque porttitor arcu ut ante aliquam, id sodales arcu varius. Vivamus ullamcorper dolor quis dui euismod sollicitudin. Donec molestie dolor ut arcu congue sollicitudin. Integer nec elit euismod, viverra turpis eu, sodales elit. Etiam a eros et sem semper pulvinar vitae a enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
    ]

    for entry in data:
        # author = user :: Via backref
        # author_id=1 is also good
        blog = Blog(author=user, title=entry['title'], content=entry['content'])

        db.session.add(blog)
        try:
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            print("Failure occured")
            print(err)

def create_many(db, User, Blog):
    user = User.query.first()

    data = []
    for i in range(100):
        entry = {
            "title": i,
            "content": i,
        }
        data.append(entry)

    for entry in data:
        # author = user :: Via backref
        # author_id=1 is also good
        blog = Blog(author=user, title=entry['title'], content=entry['content'])

        db.session.add(blog)
        try:
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            print("Failure occured")
            print(err)


# from dswd_blog.extensions import db
# from dswd_blog.models import User, Blog
# from scripts.create import init_db, create_many
# init_db(db, User, Blog)
# create_many(db, User, Blog)