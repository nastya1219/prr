from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def instruction():
    return render_template('index.html')


@app.route("/questionnaire")
def quest():
    return render_template('flask1_form.html', )


@app.route("/flask1_stats.html", methods=['GET', 'POST'])
def flask1_stats():
    if request.method == 'POST':
        # Обработка данных формы после её отправки
        last_name = request.form['last_name']
        name = request.form['name']
        gender = request.form['gender']
        mobilephone = request.form['mobilephone']
        email = request.form['email']
        user_date = request.form['user_date']
        contact = request.form['contact']
        sent = request.form['sent']

        with open('survey_results.txt', 'a') as f:
            f.write(f'Фамилия: {last_name}, Имя: {name}, Телефон: {mobilephone}, , Гендер: {gender}, Email: {email}, '
                    f'Дата: {user_date}, Образование: {contact}, Нужно/не нужно показатель начала {sent}\n')
    with open('survey_results.txt', 'r') as f:
        data = f.readlines()

    num_responses = len(data)

    return render_template('flask1_stats.html', num_responses=num_responses)


if __name__ == "__main__":
    app.run(debug=True)
