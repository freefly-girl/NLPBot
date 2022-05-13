# Simple telegram chatbot

## Start bot 
0. create file `bot_token` in project **/root** directory, generate bot_token
fill file `bot_token` as an example
```angular2html
API_TOKEN = "YOUR_BOT_TOKEN"
```
1. Run `flask_run.sh`. It will start flask server on port 6969
2. Run `main.py`

### `flask_run.sh` output with generated params
```angular2html
===> Text input: |0|1|Любишь путешествовать?|1|2|
127.0.0.1 - - [13/May/2022 14:55:28] "POST /get_answer HTTP/1.1" 200 -

===> Params generate: {'max_length': 256, 'no_repeat_ngram_size': 3, 'do_sample': True, 'top_k': 100, 'top_p': 0.9, 'temperature': 0.6, 'num_return_sequences': 1, 'device': 'cpu', 'is_always_use_length': True, 'length_generate': '-'}
===> Text input: |0|1|Какой город запомнился больше всего?|1|-|
127.0.0.1 - - [13/May/2022 14:55:50] "POST /get_answer HTTP/1.1" 200 -

===> Params generate: {'max_length': 256, 'no_repeat_ngram_size': 3, 'do_sample': True, 'top_k': 100, 'top_p': 0.9, 'temperature': 0.6, 'num_return_sequences': 1, 'device': 'cpu', 'is_always_use_length': True, 'length_generate': '2'}
```
### `main.py` output will show all user's dialog 
(including questions-**input** and answers-**output**)
```angular2html
==> Text input: Расскажи о себе
==> Text output: Живу в Германии.
==> Text input: Любишь путешествовать?
==> Text output: Нет, просто хочется посмотреть мир, побывать в разных странах, пожить в разных городах.
==> Text input: Какой город запомнился больше всего?
==> Text output: Днепропетровск
==> Text input: И что же в нем удивило больше всего?
==> Text output: Подумал, что это какой-то китайский аналог нашего "Ералаша".
```
