import os

from flask import Flask, url_for, request, render_template, redirect, abort
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.news import News
from data.departments import Department
from add_users import insert_users
from add_jobs import insert_jobs
from forms.register_user import RegisterForm
from forms.login_user import LoginForm
from forms.news import NewsForm
from forms.job_form import NewsJob
from forms.departments_form import NewsDepartment
from flask_login import LoginManager, login_user
from flask_login import login_required, logout_user, current_user

db_sess = db_session.create_session()
db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
answers = {
    'title': 'Анкета',
    'surname': 'Watny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': 'True'
}


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/promotion')
def promotion():
    adds_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(adds_list)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/images/MARS.png"/>
                        <figcaption>Вот она какая, красная планета</figcaption>
                      </body>
                    </html>"""


@app.route('/promotion_image', methods=['GET', 'POST'])
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/images/MARS.png"/>
                        <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                        </div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претедента на участие в миссии</h1>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Профессиональное</option>
                                            </select>
                                         </div>
                                         <div class="form-group">
                                            <label for="form-check">Какие у вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof1" value="инженер-исследователь">
                                              <label class="form-check-label" for="prof1">инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof2" value="пилот">
                                              <label class="form-check-label" for="prof2">пилот</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof3" value="строитель">
                                              <label class="form-check-label" for="prof3">строитель</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof4" value="экзобиолог">
                                              <label class="form-check-label" for="prof4">экзобиолог</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof5" value="врач">
                                              <label class="form-check-label" for="prof5">врач</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof6" value="инженер по терраформированию">
                                              <label class="form-check-label" for="prof6">инженер по терраформированию</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof7" value="климатолог">
                                              <label class="form-check-label" for="prof7">климатолог</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof8" value="специалист по радиационной защите">
                                              <label class="form-check-label" for="prof8">специалист по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof9" value="астрогеолог">
                                              <label class="form-check-label" for="prof9">астрогеолог</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="prof10" value="гляциолог">
                                              <label class="form-check-label" for="prof10">гляциолог</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="sex_male" value="male" checked>
                                              <label class="form-check-label" for="sex_male">Мужской</label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="sex_female" value="female">
                                              <label class="form-check-label" for="sex_female">Женский</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>

                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'], '')
        print(request.form['name'], '')
        print(request.form['email'], '')
        print(request.form['class'], '')
        print(', '.join(request.form.getlist('profession')))
        print(request.form['sex'], '')
        print(request.form['about'], '')
        f = request.files['file']
        print(f.read())
        print(request.form['accept'], '')

        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice_planet(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                        <title>Варианты выбора!</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <h2>Эта планета близка к Земле;</h2>
                        <div class="alert alert-primary" role="alert">
                      На ней много необходимых ресурсов;
                        </div>
                        <div class="alert alert-success" role="alert">
                      На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-secondary" role="alert">
                      На ней есть небольшое магнитное поле;
                        </div>
                        <div class="alert alert-warning" role="alert">
                      Наконец, она просто красива!
                        </div>
                      </body>
                    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}:</h2>
                        <div class="alert alert-primary" role="alert">
                      Поздравляем ваш рейтинг после {level} этапа отбора
                        </div>
                        <h3>составляет {rating}!</h3>
                        <div class="alert alert-success" role="alert">
                      Желаем удачи!
                        </div>
                      </body>
                    </html>"""


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        if not os.path.exists('static/uploads'):
            os.makedirs('static/uploads')
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Загрузка фотографии</h1>
                                <h2>Для участия в миссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <img src="/static/uploads/photo.jpg" style="max-width: 300px; height: auto;">
                                        </br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        f.save('static/uploads/photo.jpg')
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Пейзажи Марса</h1>
                        <div id="carouselExample" class="carousel slide">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="/static/images_for_carusel/landscape1.jpg" class="d-block w-100" alt="landscape1" style="width: 1000px; height: 680px;">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/images_for_carusel/landscape2.jpg" class="d-block w-100" alt="landscape2" style="width: 1000px; height: 680px;">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/images_for_carusel/landscape3.jpg" class="d-block w-100" alt="landscape3" style="width: 1000px; height: 680px;">
                            </div>
                          </div>
                          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Предыдущий</span>
                          </button>
                          <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Следующий</span>
                          </button>
                        </div>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
                      </body>
                    </html>"""


@app.route('/')
@app.route('/index')
def index():
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {}
    for user in users:
        names[user.id] = f'{user.surname} {user.name}'
    param = {}
    param['title'] = 'main'
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template('index.html', jobs=jobs, names=names, **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['profession'] = prof
    return render_template('prof.html', **param)


@app.route('/list_prof/<listing>')
def spisok(listing):
    param = {}
    param['how'] = listing
    return render_template('prof_listing.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html', **answers)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    param = {}
    param['gender'] = gender
    param['age'] = age
    return render_template('table.html', **param)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        try:
            user = User(
                email=form.email.data,
                surname=form.surname.data,
                name=form.name.data,
                age=form.age.data,
                position=form.position.data,
                speciality=form.speciality.data,
                address=form.address.data,
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/login')
        except Exception:
            return 'Oops, something dont work'
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/addjob', methods=['GET', 'POST'])
@login_required
def add_job():
    form = NewsJob()
    if form.validate_on_submit():
        jobs = Jobs()
        jobs.job = form.title.data
        jobs.team_leader = form.id.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_job_finished.data
        db_sess.add(jobs)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Adding a Job',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = NewsJob()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                          ).first()
        if jobs:
            form.id.data = jobs.team_leader
            form.title.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_job_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                          ).first()
        if jobs:
            jobs.team_leader = form.id.data
            jobs.job = form.title.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_job_finished.data
            db_sess.merge(jobs)
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('edit_job.html',
                           title='Edit Job',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      (Jobs.team_leader == current_user.id) | (current_user.id == 1)
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departments')
def departments():
    departments = db_sess.query(Department).all()
    users = db_sess.query(User).all()
    names = {}
    for user in users:
        names[user.id] = f'{user.surname} {user.name}'
    param = {}
    param['title'] = 'main'
    return render_template('departments.html', departments=departments, names=names, **param)


@app.route('/add_department', methods=['GET', 'POST'])
@login_required
def add_department():
    form = NewsDepartment()
    if form.validate_on_submit():
        departments = Department()
        departments.title = form.title.data
        departments.chief = form.chief.data
        departments.email = form.email.data
        departments.members = form.members.data
        db_sess.add(departments)
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_department.html', title='Adding a Department',
                           form=form)


@app.route('/departments/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departments(id):
    form = NewsDepartment()
    if request.method == "GET":
        db_sess = db_session.create_session()
        departments = db_sess.query(Department).filter(Department.id == id,
                                                       (Department.chief == current_user.id) | (current_user.id == 1)
                                                       ).first()
        if departments:
            form.chief.data = departments.chief
            form.title.data = departments.title
            form.email.data = departments.email
            form.members.data = departments.members
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departments = db_sess.query(Department).filter(Department.id == id,
                                                       (Department.chief == current_user.id) | (current_user.id == 1)
                                                       ).first()
        if departments:
            departments.chief = form.chief.data
            departments.title = form.title.data
            departments.email = form.email.data
            departments.members = form.members.data
            db_sess.merge(departments)
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('edit_department.html',
                           title='Edit Department',
                           form=form
                           )


@app.route('/departments_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def departments_delete(id):
    db_sess = db_session.create_session()
    departments = db_sess.query(Department).filter(Department.id == id,
                                                   (Department.chief == current_user.id) | (current_user.id == 1)
                                                   ).first()
    if departments:
        db_sess.delete(departments)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
