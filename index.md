{% include head.html %}

# Are You The One?

## The Show
Are You The One is a matchmaking reality show on MTV. Season 8 features 16 contestants staying in a Big Brother style group house. Relationship experts have sorted the housemates into 8 "perfect matches," which are unknown to the players. At the end of each episode, the contestants pair up. It is then revealed how many of the pairs are perfect matches, but not specifically which pairs are correctly matched. The goal is to construct as many perfect matches as possible by the end of the season. Each episode also features a visit to the Truth Booth, in which the contestants learn definitively whether a specific couple is a perfect match or not.

## The Problem
Let's take an initial look at the math. With 16 players, there are 16 choose 2 possible couples.
{% raw %}
  $${16\choose 2} = 120$$
{% endraw %}

How many ways can we select 8 couples from a pool of 16 people? Choosing the first pair is {% raw %}$${16\choose 2}$${% endraw %}, the second {% raw %}$${14\choose 2}$${% endraw %}, and so on. These pairs can be arranged in 8! ways. So there are
{% raw %}
  $$(\dfrac{{16\choose 2}{14\choose 2}{12\choose 2} ... {2\choose 2}}{8!} = \dfrac{n!}{((n/2)!2^(n/2))} = 2,027,025$$
{% endraw %}
ways to select 8 couples.
