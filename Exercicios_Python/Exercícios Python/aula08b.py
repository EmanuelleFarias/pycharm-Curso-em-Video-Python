# pra importar alguma biblioteca que não tenho, clica na luz vermelha>install package
import emoji
from emoji import demojize

print(emoji.emojize('Estou aprendendo:face_holding_back_tears:',variant='emoji_type'))
print(emoji.emojize('está sendo divertido :eyes:'))
print(emoji.emojize('olha eu :woman_curly_hair:'))

#sempre colocar o emoji em inglês ou especificar a language
print(emoji.emojize('atenta:olho::boca::olho:', language='pt'))
print(emoji.is_emoji("👍"))
print(demojize('oi 🙋‍♀️ 🐝', language='es')) #se colocar a função demojize ele escreve o nome do emoji