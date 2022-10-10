f = open('../zadanie3.2txt', 'r', encoding='utf -8')
st = f.read()  # читаем файл
rest = st.lower()
st_1 = rest.replace(',', '')
spisok_polit_slov = st_1.split()
spisok_2 = [x for x in range(1, 1067)]

slov_polit_slov_chek = dict(zip(spisok_2, spisok_polit_slov))
