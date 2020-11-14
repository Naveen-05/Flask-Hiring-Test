from flask import Flask,render_template,url_for,redirect,flash,request,jsonify
app = Flask(__name__)
@app.route('/index')
@app.route('/')
def index():
    balance = Balance.query.all()
    exists = bool(Balance.query.all())
    if exists == False:
        flash(f'Add products,locations and make transfers to view', 'info')
    return render_template('index.html',balance=balance)

@app.route('/transfer')
def transfer():
    return render_template('transfer.html')

@app.route('/product', methods = ['GET','POST'])
def product():
    form = addproduct()
    eform = editproduct()
    details = Product.query.all()
    exists = bool(Product.query.all())
    if exists == False and request.method == 'GET':
        flash(f'Add products to view', 'info')
    elif eform.validate_on_submit() and request.method == 'POST':

        p_id = request.form.get("Product_id", "")
        details = Product.query.all()
        prod = Product.query.filter_by(Product_id=p_id).first()
        try:
            db.session.commit()
            flash(f'updated!', 'success')
            return redirect('/product')
        except IntegrityError:
            db.session.rollback()
            flash(f'This product already exists', 'danger')
            return redirect('/product')
        return render_template('product.html', title='Products', details=details, eform=eform)

    return render_template('product.html', title='Products', eform=eform, form=form, details=details)

    return render_template('product.html')
