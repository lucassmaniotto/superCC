# **SuperCC - Trabalho Final de Algoritmos de Programação - 1º Fase / UFFS**


## **Sistema SuperCC**

Você foi contratado(a) para criar um sistema que simule um caixa de um supermercado virtual utilizando a linguagem Python. 

Nas próximas seções são descritas as informações necessárias para a implementação do sistema.

## **Tarefas**

O objetivo de seu programa é possibilitar que o operador de caixa (usuário do programa) cadastre os produtos do supermercado e também registre as compras de um determinado cliente. Quando a compra finalizar, o sistema mostra o cupom fiscal: código e nome do produto, quantidade comprada e valor. No fim do cupom é apresentado o valor total da compra.


### **1 - Cadastrar novos produtos**

O caixa poderá criar um novo produto informando os seguintes dados cadastrais:

* **Código do produto:** código numérico do produto;
* **Nome do produto:** nome do produto; 
* **Preço do produto:** preço de venda unitário do produto;
* **Quantidade em estoque**: quantidade do produto em estoque para a venda.

### **2 - Atualizar produtos**
Permite que dados dos produtos sejam atualizados. Poderão ser atualizados apenas o **preço unitário** e a **quantidade em estoque**.

### **3 - Registrar compra**

O caixa registrará a compra do cliente, informando o código de cada produto (deverá ser apresentado o nome para o caixa se certificar que digitou o código correto) e quantidade comprada. Caso a quantidade exceda a quantidade em estoque do respectivo produto, o sistema deve informar o problema, apresentando a quantidade atual do estoque e não permitindo aquela entrada.
Se a entrada for confirmada, lembrar de atualizar o estoque do produto.
Deverá existir uma forma de encerrar o registro da compra(dica: pode ser o código -1 , por exemplo).
A forma de pagamento não será controlada.
Ao final, o sistema deverá apresentar um tipo de cupom fiscal. Ex.:

|Código|Nome|Quantidade|Preço|
|:---:|:---:|:---:|:---:|
|12|Creme Colgate|1|4,50|
|4|Sabonete Dove|5|18,70|
|78|Fio Dental|1|21,34|
|||Total|44,54|


### **4 - Consultar produto**

Permite buscar os dados do produto pelo seu código. Caso o produto não exista, exibir a mensagem **Produto não cadastrado**


### **5 - Relatório de produtos**

Exibe a lista de todos produtos cadastrados (código, nome, preço e quantidade em estoque).

&nbsp;

---
