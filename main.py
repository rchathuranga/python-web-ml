from flask import Flask
from flask import request
from nic_parser.parser import Parser

app = Flask(__name__)


@app.route("/")
def end_point():
    name = f"{request.args['name']}"
    nic = f"{request.args['nic']}"

    np = Parser(nic)
    dob = np.birth_date.strftime("%m/%d/%Y")
    gender = np.gender

    response = {'name': name, 'nic': nic, 'dob': dob, 'gender': f"{gender}"}

    return f"{response}"

if __name__ == '__main__':
    app.run(port=8081)
