import os


COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

import sys
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment, UserLog
\
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment, UserLog=UserLog)


@app.cli.command()
@click.option('--coverage/--no-coverage', default=False,
              help='Run tests under code coverage.')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()

@app.cli.command()
@click.option('--length', default=25,
              help='Number of functions to include in the profiler report.')
@click.option('--profile-dir', default=None,
              help='Directory where profiler data files are saved.')
def profile(length, profile_dir):
    """Start the application under the code profiler."""
    from werkzeug.middleware.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run(debug=False)


@app.cli.command()
def deploy():

    # migrate database to latest revision
    upgrade()

    # create or update user roles
    Role.insert_roles()

    # ensure all users are following their own posts
    User.add_self_follows()
    
@app.cli.command()
def forge():
    """Generate fake data (dev only)."""
    from app.models import User, Post, Comment, Role
    from app import db
    import click
    
    db.create_all()

    if Role.query.count() == 0:
        click.echo('Inserting roles...')
        Role.insert_roles()

    if User.query.count() == 0:
        click.echo('Generating users...')
        User.generate_fake(10)

    if Post.query.count() == 0:
        click.echo('Generating posts...')
        Post.generate_fake(50)

    if Comment.query.count() == 0:
        click.echo('Generating comments...')
        Comment.generate_fake_comments(100)

    if UserLog.query.count() == 0:
        click.echo('Generating user logs...')
        UserLog.generate_fake_logs(100)

    click.echo('Done.')