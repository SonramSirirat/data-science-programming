# Problem Solving

Assume you open your ice cream shop, there are only two types of ice cream, vanilla and strawberry. When a box of ice cream is sold, you will get the benefit for $ 2 for vanilla ice cream and $ 3 for strawberry ice cream. To make the ice cream, the fresh milk is required. To make a box of vanilla ice cream requires 0.5 liter and strawberry ice cream requires 0.2 liter. You daily order 10 liters of fresh milk. To promote your ice cream shop, you give a doll for each ice cream box. The number of dolls, that you can give to customers, is 30 dolls per day. So, how many boxes of vanilla ice cream and strawberry ice cream that you would like to produce to get maximum profit ?

| Favor      | Fresh milk/(Liter) | Profit $/(Box) |
| ---        | ---                | ---            |
| Vanilla    | 0.5                | 2              |
| Strawberry | 0.2                | 3              |

- Order daily 10 liters of fresh milk
- Dolls for each ice cream box. (30 per day)

**Identify Problem**

How many boxes of vanilla ice cream and strawberry ice cream that you would like to produce to get **maximum profit**

**Formulate and Implement Model**

- Decision variables
  
  vanilla_ice: The amount of vanilla ice cream boxes.

  strawberry_ice: The amount of strawberry ice cream boxes.

- Ojective function
  
  Find profit of ice cream

  vanilla_profit = 2 * vanilla_ice: Equal profit of vanilla ice cream.

  strawberry_profit = 3 * strawberry_ice: Equal profit of strawberry ice cream.

  maximun_profit = vanilla_profit + strawberry_profit: Maximum profit to produce.

- Constraints
  - Vanilla ice cream use fresh milk for 0.5 per boxes.
    - 0.5 * vanilla_ice <= 10: Maximum vanilla ice cream boxes can make per day.
  - Strawberry ice cream use fresh milk for 0.2 per boxes.
    - 0.2 * strawberry_ice <= 10: Maximum strawberry ice cream boxes can make per day.
  - Maximum fresh milk is 10 liters per day.
    - (0.5) * vanilla_ice + (0.2) * strawberry_ice <= 10: Maximum both favor ice cream boxes can make per day.
  - Maximum doll is 30 dolls per day 1 doll per boxes.
    - (0.5) * vanilla_ice + (0.2) * strawberry_ice <= 30: Maximun dolls for promotion per day.

**Analyze Model**

**Test Results**

**Implement Solution**