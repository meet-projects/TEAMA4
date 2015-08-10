from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#SQLAlchemy stuff
from mydea_database import Base, User, Status #<--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def main():
    return render_template('main_page.html')

@app.route('/wall')
def wall():
    return render_template('mydeas_wall.html')

#user
@app.route('/register_user', methods =['GET', 'POST'])
def add_user():
	if request.method == 'GET':
		return render_template('sign_up_page.html')
	else:
		new_user = User(
		name = request.form['name'],
		email = request.form ['email'],
		password = request.form['password'])
		session.add(new_user)
		session.commit()
		return redirect(url_for('main'))


@app.route('/delete/<int:user_id>', methods = ['GET', 'POST'])
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if request.method == 'GET':
        return render_template('delete_user.html', user=user)
    else: 
        session.delete(user)
        return redirect(url_for('wall'))

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
    	return redirect(url_for('wall'))
#Status
@app.route('/add', methods = ['GET', 'POST'])
def add_status():
	if request.method == 'GET':
		return render_template('add_mydeas_page.html')
	else:
		if request.form['category']== 'entrepreneurship':
			bc='b'
		else:
			bc='c'
		new_status = Status(
		status = request.form['status'],
		likes = 0,
		dop = request.form['dop'],
		user_posted = request.form[user_id],
		bc=bc)
		
		
		session.add(new_status)
		session.commit()
        	return redirect(url_for('wall'))

@app.route('/delete/<int:status_id>', methods = ['GET', 'POST'])
def delete_status(user_id):
    status = session.query(Status).filter_by(id=Status_id).first()
    if request.method == 'GET':
        return render_template('mydeas_wall.html', status=status)
    else: 
        session.delete(status)
        return redirect(url_for('wall'))

@app.route('/edit/<int:status_id>', methods=['GET', 'POST'])
def edit_status(user_id):
    status = session.query(Status).filter_by(id=status_id).first()
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
    	return redirect(url_for('wall'))





@app.route('/likes/<int:status_id>', methods=['POST'])
def like_button (status_id):
	if request.method == 'POST':
		Status.filter_by(id=status_id).likes += 1
	return redirect(url_for('wall'))



if __name__ == '__main__':
	app.run(debug=True)
