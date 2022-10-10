slovar = {
    'slovo': 'говно',
    'slovo_2': 'хуйня',
    'slovo_3': 'блять',
    'slovo_4': 'ебем',
    'slovo_5': 'дрочим',
    'slovo_6': 'тварь',
    'slovo 7': 'пидорас'

}

f = open('../zadanie3.3txt', 'r', encoding='utf -8')
st = f.read()  # читаем файл
st_1 = st.replace(',', '')

gh = st_1.split(' ')  # разбиваем по пробелам

sp = []
for i in range(1, 674):
    sp.append(i)

slovar_res = dict(zip(sp, gh))
# print(slovar_res)
# print(slovar)
slovar_itog = slovar | slovar_res
