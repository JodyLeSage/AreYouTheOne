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
  $$\dfrac{{16\choose 2}{14\choose 2}{12\choose 2} ... {2\choose 2}}{8!} = \dfrac{16!}{8!\times2^8} = 2,027,025$$
{% endraw %}
ways to select 8 couples. To make communicating easier, I will be calling each set of 8 couples a solution. The purpose of this project is to select and apply a mathematical model to this problem in order minimize the set of possible solutions.

## The Truth Booth
The results from the Truth Booth are extremely valuable in minimizing the space of potential solutions. Each perfect match revealed in the Truth Booth leaves
{% raw %}
  $$\dfrac{(16 - 2p)!}{(8-p)!\times2^{(8-p)}}$$
{% endraw %}
possible solutions, where p is the nth perfect match revealed. The following chart shows the effect on the solution space that each perfect match has.

| Perfect Match Revealed | Maximum Solutions Remaining |
|------------------------|-----------------------------|
| 1st                    | 135,135                     |
| 2nd                    | 10,395                      |
| 3rd                    | 945                         |
| 4th                    | 210                         |
| 5th                    | 15                          |
| 6th                    | 3                           |
| 7th                    | 1                           |

Conversely, revealing a non-match in the Truth Booth is much less effective at minimizing the solution space, as it only eliminates other solutions that also contain that particular match, which is a near-constant rate.

| Non-Match Revealed | Maximum Solutions Remaining |
|--------------------|-----------------------------|
| 1st                | 1,891,890                   |
| 2nd                | 1,756,754                   |
| 3rd                | 1,621,617                   |
| 4th                | 1,486,478                   |
| 5th                | 1,351,348                   |
| 6th                | 1,215,197                   |
| 7th                | 1,081,060                   |

These numbers demonstrate that the mathematically optimal strategy for the Truth Booth is to send couples which are believed to be perfect matches, as opposed to sending in a couple with a rocky relationship in the hopes of breaking them up.
