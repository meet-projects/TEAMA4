from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#SQLAlchemy stuff
from mydea_database import Base, User, Status, Comment #<--- Import your tables here!!
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/', methods =['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('main_page.html')
	else:
		email = request.form['email']
		password = request.form['password']
		user = session.query(User).filter_by(email=email, password=password).first()
		if user == None:
			return redirect (url_for('main'))
		return redirect (url_for('wall',user_id=user.id))

@app.route('/wall/<int:user_id>')
def wall(user_id):
	user = session.query(User).filter_by(id=user_id).first()
	statuses = session.query(Status).order_by(desc(Status.id)).all()
	return render_template('mydeas_wall.html', user=user, statuses=statuses)



#user
@app.route('/register_user', methods =['GET', 'POST'])
def add_user():
	if request.method == 'GET':
		return render_template('sign_up_page.html')
		print ('00000')
	else:
		if 'iagree' in request.form and request.form['iagree'] == 'on':
			print ('1111')
			if request.form['name']== '' or request.form ['email'] == ''or request.form['password']=='':
				return redirect(url_for('add_user')) 
				print ('22222')
			print ('3333')
			new_user = User(
			name = request.form['name'],
			email = request.form ['email'],
			
			password = request.form['password'])
			session.add(new_user)
			session.commit()
			return redirect(url_for('add_mydeas'))
		else:
 			return redirect(url_for('add_user'))
			print ('44444')


@app.route('/delete/<int:user_id>', methods = ['GET', 'POST'])
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if request.method == 'GET':
        return render_template('delete_user.html', user=user)
    else: 
        session.delete(user)
        return redirect(url_for('wall'))

@app.route('/add2', methods = ['GET', 'POST'])
def add_mydeas():
	return render_template('add_mydeas_page.html')

@app.route('/wall', methods = ['GET', 'POST'])
def mydeas_wall():
	statuses = session.query(Status).all()
	user = session.query(User).filter_by(id = 1).first()
	return render_template('mydeas_wall.html', statuses = statuses, user = user)


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
	print "Inside add status"
	user = session.query(User).filter_by(id = 1).first()
	if request.method == 'GET':
		print "inside get method"
		return render_template('add_mydeas_page.html')
	else:
		print "inside post method"
		if request.form['category']== 'entrepreneurship':
			bc='Entrepreneurship'
		else:
			bc='Community'
		new_status = Status(
		status = request.form['status'],
		likes = 0,
		##dop = request.form['dop'],
		##user_posted = request.form[user_id],
		bc=bc)
		
		session.add(new_status)
		session.commit()
		print "commit successful"
		
        	return redirect(url_for('mydeas_wall', user = user))

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
		status = session.query(Status).filter_by(id = status_id).first()
		status.likes += 1
		session.commit()
	return redirect(url_for('mydeas_wall'))

@app.route('/status/<int:status_id>', methods=["GET", 'POST'])
def status_page (status_id):
	if request.method == 'GET':
		status = session.query(Status).filter_by(id = status_id).first()
		comments = session.query(Comment).filter_by(status_id = status_id)
		return render_template('status_page.html', comments=comments, status=status)
	else:
		comment=Comment(content=request.form['content'], status_id = status_id)
		session.add(comment)
		session.commit()
		return redirect(url_for('status_page', status_id=status_id))

if __name__ == '__main__':
	app.run(debug=True)
