from flask import Flask, render_template
app = Flask(__name__)

#SQLAlchemy stuff
from mydea_database import Base, User #<--- Import your tables here!!
from mydea_database import Base, StatusC
from mydea_database import Base, StatusB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def main():
    return render_template('main_page.html')

#user
@app.route('/register_user', methods =['GET', 'POST'])
def add_user():
	if request.method == 'GET':
		return render_template('signuppage.html')
	else:
		new_user = User(
		name = request.form['name'],
		email = request.form ['email'],
		password = request.form['password'])
		session.add(new_user)
		session.commit()
		return redirect(url_for('about_mydea.html'))


@app.route('/delete/<int:user_id>', methods = ['GET', 'POST'])
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if request.method == 'GET':
        return render_template('delete_user.html', user=user)
    else: 
        session.delete(user)
        return redirect(url_for('mydea_wall.html'))

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if request.method == 'GET':
    	return render_template('edit_user.html', user=user)
    else:
    	new_name = request.form['name']
    	new_email = request.form['email']
    	new_password = request.form['password']
    	user.name = new_name
    	user.email = new_email
    	user.password = new_password	
    	session.commit()
    	return redirect(url_for('mydea_wall.html'))
#StatusC
def add_status_c():
	if request.method == 'GET':
		return render_template('mydea_wall.html')
	else:
		new_status_c = StatusC(
		status = request.form['status'],
		likes = request.form ['likes'],
		dop = request.form['dop'],
		user_posted = request.form['user_posted'])
		session.add(new_status_c)
		session.commit()
        	return redirect(url_for('mydea_wall.html'))

@app.route('/delete/<int:status_id>', methods = ['GET', 'POST'])
def delete_status_c(user_id):
    status = session.query(StatusC).filter_by(id=StatusC_id).first()
    if request.method == 'GET':
        return render_template('mydea_wall.html', status=status)
    else: 
        session.delete(status)
        return redirect(url_for('mydea_wall.html'))

@app.route('/edit/<int:status_id>', methods=['GET', 'POST'])
def edit_status_c(user_id):
    status = session.query(StatusC).filter_by(id=status_id).first()
    if request.method == 'GET':
    	return render_template('edit_status.html', status=status)
    else:
    	new_status = request.form['status']
    	new_likes = request.form['likes']
    	new_dop = request.form['dop']
	new_user_posted = request.form['user_posted']
    	user.status = new_status
    	user.likes = new_likes
    	user.dop = new_dop	
	user.user_posted = new_user_posted
    	session.commit()
    	return redirect(url_for('mydea_wall.html'))

#StatusB
def add_status_b():
	if request.method == 'GET':
		return render_template('mydea_wall.html')
	else:
		new_status_b = StatusB(
		status = request.form['status'],
		likes = request.form ['likes'],
		dop = request.form['dop'],
		user_posted = request.form['user_posted'])
		session.add(new_status_b)
		session.commit()
        	return redirect(url_for('mydea_wall.html'))

@app.route('/delete/<int:status_id>', methods = ['GET', 'POST'])
def delete_status_b(user_id):
    status = session.query(StatusB).filter_by(id=StatusB_id).first()
    if request.method == 'GET':
        return render_template('mydea_wall.html', status=status)
    else: 
        session.delete(status)
        return redirect(url_for('mydea_wall.html'))

@app.route('/edit/<int:status_id>', methods=['GET', 'POST'])
def edit_status_b(user_id):
    status = session.query(StatusB).filter_by(id=status_id).first()
    if request.method == 'GET':
    	return render_template('edit_status.html', status=status)
    else:
    	new_status = request.form['status']
    	new_likes = request.form['likes']
    	new_dop = request.form['dop']
	new_user_posted = request.form['user_posted']
    	user.status = new_status
    	user.likes = new_likes
    	user.dop = new_dop	
	user.user_posted = new_user_posted
    	session.commit()
    	return redirect(url_for('mydea_wall.html'))

