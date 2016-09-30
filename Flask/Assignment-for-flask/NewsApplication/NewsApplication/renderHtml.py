from flask import Flask,render_template,request,redirect,url_for,make_response,session
newsItems={
    1:['Sports','India v New Zealand, 1st Test, Kanpur, Day 5: India beat New Zealand by 197 runs'],
    2:['Global','Airstrikes pound rebel-held Aleppo districts overnight'],
    3:['Technology','Xiaomi Mi Air Purifier 2: Its usefulness depends on you and your concern for your family'],
    4:['Sports','Priceless to have Ashwin in Test team: Virat Kohli'],
    5:['Technology','Reliance Jio Mobiles: Top-Rated VoLTE Phones'],
    6:['Global','Debate night: Hillary, Trump set for high-stakes showdown'],
    7:['Sports','A Test win that ticks many boxes'],
    8:['Technology','Android-Chrome OS Merger "Andromeda" Will Be Teased at Google"s October 4 Event: Reports'],
    9:['Global','China buys record North Korean coal as sanctions ignored: Data'],
}
users={
    'radhika':'radhika',
    'abc':'abc',
    'def':'def'
}
newsCategory=['Sports','Global','Technology']

newsApp=Flask(__name__)
newsApp.secret_key='xoriant123#'

@newsApp.route('/')
def goToHome():
    return render_template('Home.html')


@newsApp.route('/admin/<user>')
def goToAdmin(user):
    session['username']=user
    return render_template('Admin.html', news=newsItems)

@newsApp.route('/user/<user>')
def goToUser(user):
    session['username'] = user
    return render_template('User.html', news=newsItems)

@newsApp.route('/admin/addnews',methods=['POST','GET'])
def addNews():
    if request.method == 'POST':
        selectcategory=request.form['selectcategory']
        news=request.form['newsitem']
    return render_template('Addnews.html',category=newsCategory)

@newsApp.route('/admin/modifynews',methods=['POST','GET'])
def modifynews():
    # if request.method == 'POST':
    #     selectcategory=request.form['selectcategory']
    #     news=request.form['newsitem']
    return render_template('ModifyNews.html',category=newsCategory)

@newsApp.route('/login',methods=['POST','GET'])
def validate():
    if request.method == 'POST':
        getusername=request.form['username']
        getpassword=request.form['password']
        if users[getusername] == getpassword and getusername=='radhika':
           return redirect(url_for('goToAdmin',user=getusername))
        elif getusername == 'abc' or getusername=='def':
            if users[getusername]==getpassword:
                return redirect(url_for('goToUser',user=getusername))
        else:
            return redirect(url_for('goToHome'))
    return render_template('Login.html')

@newsApp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('goToHome'))

if __name__ == '__main__':
    newsApp.run()