class Produto:
  def __init__(self, id: int, name: str, price: float, stock: float): # Inicia valores para os Produtos - Função construtora
    self.id = id
    self.name = name
    self.price = price
    self.stock = stock

  def update(self): # Função para atualizar a classe Produto
    new_stock = input('Insira o novo estoque: ')
    if new_stock != '': # atualiza o Estoque
      print(f'[Produto #{self.id} ({self.name}) Atualizado: Estoque {self.stock} -> {float(new_stock)}]')
      self.stock = float(new_stock)
    
    new_price = input('Insira o novo preço:')
    if new_price != '': # atualiza o Preço
      print(f'[Produto #{self.id} ({self.name}) Atualizado: Preço {self.price} -> {float(new_price)}]')
      self.price = float(new_price)


  # Função que mostra como o Objeto deve ser printado
  def __repr__(self): # Função representativa
    return f'Produto #{self.id} :: {self.name} :: R$ {self.price:.2f} :: {self.stock:.3f} un.'


# Registro de informações sobre                                               
# a compra de UM produto                                              

class Compra:
  def __init__(self): # Inicia os valores da Compra
    self.produtosComprados = []
    self.total = 0.0
  
  def adicionaProduto(self, produto: Produto, quantidade): # Insere um produto cadastrado na lista de compras
    total_produto = quantidade * produto.price #Calcula preço em quantidade de um produto específico
    self.produtosComprados.append([produto, quantidade, total_produto])
    self.total += total_produto

  def geraNF(self): # Gera a Nota Fiscal
    print('\n\tNota Fiscal:')
    for linha in self.produtosComprados:
      print(f'Código: {linha[0].id}\tNome: {linha[0].name}\tQuant: {linha[1]}\tPreço: {linha[2]}')
    print(f'\nTotal da compra: {self.total}')

def cadastro(): # Cadastro de produtos
  print("\nCadastro de produtos")
  produtos_temp = []
  produtos_quant = int(input("Quantos produtos deseja cadastrar? "))
  for i in range(produtos_quant):
    # coletando informações
    id = int(input('\nDigite o código do produto: '))
    name = input('Digite o nome do produto: ')
    price = float(input('Digite o preço unitário do produto: '))
    stock = float(input('Digite a quantidade em estoque: '))

    # instanciando Produto
    produto = Produto(id, name, price, stock)
    produtos_temp.append(produto)
    print(f'[Produtos Cadastrados: \t{produtos_temp}]')
  return produtos_temp

def consulta(produtos, id): # Busca produtos pelo Código
  for p in produtos:
    if p.id == id:
      print('Produto Cadastrado')
      return p
    print('Produto Não Cadastrado')
  return None

def atualiza(produtos): # Atualiza produtos pelo Código
  print('\nAtualizar produtos')
  print('Para não atualizar uma categoria aperte Enter')
  print(produtos)
  if len(produtos) != 0:
    prod_id = int(input('Digite o Código do Produto: '))
    prod = consulta(produtos, prod_id) # Chama função de consulta
    if prod is not None:
      prod.update() # Chama função de atualização da classe Produtos
  else:
    print('Não há cadastros')

def registrarCompra(produtos): # Registra a compra
  print('\nRegistro de Compras')
  compra = Compra() # Chama a classe Compra
  ativo = 'S'
  while ativo == 'S':
    codigo = int(input('Informe o Código do Produto: '))
    produto = consulta(produtos, codigo) # Consulta se existe
    if produto != None:
      print(f'Produto encontrado: {produto.name}')
      verifica = input('Gostaria de registrar esse produto? S ou N: ')
      if verifica == 'S':
        quant = int(input('Quantidade comprada: '))
        while quant > produto.stock:
          print('Quantidade insuficiente')
          quant = int(input('Informe quantidade comprada dentro do estoque: '))
        produto.stock = produto.stock - quant
        compra.adicionaProduto(produto, quant) # Insere na classe Compras
        print('Registrado com sucesso')
    else:
      print('Produto não cadastrado')
    ativo = input('Deseja continuar? S ou N: ')
  compra.geraNF() # gera a Nota Fiscal

def relatorioCadastro(produtos): # Faz um relatório sobre todos produtos inseridos
  for produto in produtos:
    print(produto)

produtos = []
print('Bem vindo ao SuperCC!\n')
print('1 - Cadastro de produtos\n2 - Atualizar Estoque/Preço\n3 - Registrar compras\n4 - Consultar produtos cadastrados\n5 - Relatório de Cadastro\n6 - Sair\n')
option = int(input('Escolha a opção: '))

while option != 6:
  if option == 1:
    registrados = cadastro()
    for reg in registrados: # Adiciona os elementos recebidos a lista produtos
      produtos.append(reg)
    option = int(input('\nEscolha a opção: '))
  if option == 2:
    atualiza(produtos)
    option = int(input('\nEscolha a opção: '))
  if option == 3:
    registrarCompra(produtos)
    option = int(input('\nEscolha a opção: '))
  if option == 4:
    codigo = int(input('Qual Código deseja verificar? '))
    print(consulta(produtos, codigo))
    option = int(input('\nEscolha a opção: '))
  if option == 5:
    relatorioCadastro(produtos)
    option = int(input('\nEscolha a opção: '))
  if option == 6:
    break
  if option > 6 or option < 1:
    option = int(input('\nEscolha a opção correta: '))
print('\nSistema finalizado')
