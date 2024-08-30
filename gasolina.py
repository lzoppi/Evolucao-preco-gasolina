df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df, x='dia', y='venda', marker='o')
  grafico.set(title='EVOLUÇÃO PREÇO GASOLINA', xlabel='Dia', ylabel='Preço')

grafico.figure.savefig('gasolina.png')