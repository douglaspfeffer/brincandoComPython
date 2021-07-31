from speedtest import Speedtest

st=Speedtest()

print(f'Sua velocidade de Download é: {st.download()}')
print(f'Sua velocidade de Upload é: {st.upload()}')

