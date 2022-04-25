from flask import Flask, request
from gpt import GPT, params_default
import random

app = Flask(__name__)
gpt = GPT(path_model='Grossmend/rudialogpt3_medium_based_on_gpt2')


@app.route('/get_answer', methods=['POST'])
def hello():

    inputs = request.json['inputs']

    new_params = params_default
    new_params['length_generate'] = random.choice(['-', '1', '2', '3'])

    resp_text = "".join(gpt.get_responses(inputs=inputs,
                                          params=new_params)['outputs'])

    return {'outputs': resp_text}