# Django Blog

[![Build Status](https://travis-ci.org/jordanblakey/django-blog.svg?branch=master)](https://travis-ci.org/jordanblakey/django-blog)

Basic Django blog.

You will need to work in a Python virtual environment:

- `./install.sh`
- `source env/bin/activate` or `source env/bin/activate.fish`
- `python djangoproject/manage.py migrate`

### Some assorted commands that may be useful

``` bash
python # ensure you have python installed
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py # get Python Package Manager installation script
python get-pip.py # install pip
pip install -U pip # upgrade pip
pip install virtualenv # basiacally this is npm for Python
virtualenv env # init virtual environment
source env/bin/activate # activate virtual environment
deactivate # To deactivate virtual environment
apt-get update
apt-get install libmysqlclient-dev mysql-server php libapache2-mod-php php-mcrypt php-mysql php-mbstring php-gettext phpmyadmin #install MySQL and dependencies
phpenmod mcrypt; phpenmod mbstring #enable MySQL encryption mod and Mbstring (used to manage non-ASCII strings in PHP).
systemctl restart apache2 # restart apache
mysql # MySQL CLI
mysql -p -u root # MySQL CLI with username arg
mysql --help
mysqladmin -p -u root
mysqladmin -p -u root version
mysql_secure_installation # MySQL CLI setup script
service mysql start
service mysql status
pip3 install mysqlclient

pip install Django # Make sure that virtualenv is activated (source env/bin/activate.fish)
```

---

## Django Commands

``` bash
*args = list of arguments -as positional arguments
**kwargs = dictionary - whose keys become separate keyword arguments and the values become values of these arguments.
python manage.py migrate
python manage.py check # Check for errors in Django
python manage.py shell #open the manage.py shell to create API routes.
python manage.py startapp posts # Create a new app
python manage.py sqlmigrate polls 0001
python manage.py makemigrations polls
python manage.py createsuperuser # Create a new superuser
python manage.py migrate # Run any DB migrations (will warn if unapplied migrations exist)
python manage.py runserver # Start the dev server
```

## Manage.py Shell

``` python
>>> from polls.models import Question, Choice

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

## Migrations

The migrate command looks at the `INSTALLED_APPS` setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), `SHOW TABLES`; (MySQL), .schema (SQLite), or `SELECT TABLE_NAME FROM USER_TABLES`; (Oracle) to display the tables Django created.

Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

``` sql
## THIS IS THE SQL THAT A MIGRATION FILE CREATES
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Add field question to choice
--
ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;

COMMIT;
```
