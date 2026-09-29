# 🏦 Sistema Bancário Orientado a Objetos (POO) em Python

Um sistema bancário robusto desenvolvido em Python puro, aplicando os princípios fundamentais da **Programação Orientada a Objetos (POO)**, **tratamento de exceções personalizadas** e uso eficiente de **estruturas de dados** (`List`, `Set` e `Dict`) para garantir integridade e performance nas operações.

---

## 🚀 Funcionalidades

- **Cadastro de Contas**: Suporte a criação de contas com validação de duplicidade por CPF e por número de conta.
- **Operações Bancárias**:
  - Depósitos com validação de valores positivos.
  - Saques com verificação de saldo e limites.
  - Transferências entre contas cadastradas.
- **Tratamento de Exceções**: Sistema defensivo com erros customizados para regras de negócio bancárias.
- **Estruturas de Dados Otimizadas**:
  - `List`: Mantém a ordenação do histórico/cadastro das contas.
  - `Set`: Garante consultas instantâneas e impede CPFs duplicados.
  - `Dict (Map)`: Permite busca de contas por número com complexidade $O(1)$.

---

## ⚙️ Regras de Negócio e Exceções

O projeto implementa exceções customizadas para tratar falhas e regras bancárias sem interromper a execução do programa:

- `ValorInferiorException`: Lançada ao tentar depositar ou sacar valores menores ou iguais a zero.
- `SaldoInsuficienteException`: Lançada ao tentar sacar ou transferir um valor superior ao saldo disponível.
- `ContaInexistenteException`: Lançada ao tentar realizar operações em contas não cadastradas no sistema.
- `CpfduplicadoException`: Lançada ao tentar cadastrar uma nova conta com um CPF que já possui registro no banco.

---

## 💻 Tecnologias Utilizadas

- **Python 3.x** (sem dependências externas)
- Paradigma de **Programação Orientada a Objetos (POO)**
- Estilo de código e convenções conforme a **PEP 8**

---

## 📁 Estrutura das Classes

```text
├── ContaBancaria
│   ├── Atributos: numero_conta, cpf, titular, saldo
│   └── Métodos: depositar(), sacar(), transferir()
│
└── Banco
    ├── Atributos: contas_lista (List), cpf_set (Set), contas_map (Dict)
    └── Métodos: cadastrar_conta(), buscar_conta(), depositar(), sacar(), transferir()