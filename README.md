# Validação de CEP/Cidade

Este código em Python implementa uma função chamada is_cep_valid que verifica se um CEP (Código de Endereçamento Postal) é válido. A função recebe uma lista de CEPs como parâmetro e retorna uma lista de resultados indicando se cada CEP é válido ou não, juntamente com o nome da cidade correspondente, se disponível.

## Autor

<a href="https://github.com/lyipef"><img src="https://avatars.githubusercontent.com/u/120730541?v=4" width="100px;" alt="Filipe José"/></a>

## Como usar?

O código percorre cada CEP na lista fornecida e executa as seguintes etapas:

Remove caracteres não numéricos do CEP.
Verifica se o CEP possui exatamente 8 dígitos. Se não tiver, o CEP é considerado inválido.
Faz uma solicitação à API do ViaCEP usando o CEP como parâmetro.
Analisa a resposta da API para determinar se o CEP é válido.
Se o CEP for válido e não houver erros na resposta, o nome da cidade correspondente é adicionado à lista de resultados.
Se o CEP não for válido ou ocorrer algum erro na solicitação, é adicionado um valor nulo à lista de resultados.

Ao final, a função retorna a lista de resultados contendo cada CEP validado juntamente com o nome da cidade, se disponível.

![image](https://github.com/lyipef/valid_cep_city/assets/120730541/9766e36e-cd86-4ff1-a998-fee55dfbd4d2)
