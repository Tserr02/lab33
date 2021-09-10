from flask import render_template, request

from model import *

db.create_all()


@app.route('/')
def index():
    return show_main()


@app.route('/main')
def show_main():
    results = db.session.query(Result).all()
    return render_template('index.html', results=results)


@app.route('/addText', methods=['POST'])
def add_text():
    from PIL import Image, ImageDraw, ImageFont
    x = request.form.get('x')
    y = request.form.get('y')
    text = request.form.get('text')

    image = Image.open("static/img/5790.jpg")
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    drawer.text((int(x), int(y)), text, font=font, fill='black')

    results = db.session.query(Result).all()

    path = "static/img/result" + str(len(results) + 1) + ".jpeg"

    result = Result(image_path=path, x=int(x), y=int(y),
                    text=text)
    db.session.add(result)
    db.session.commit()

    image.save(path)

    return show_main()


if __name__ == '__main__':
    app.run()
