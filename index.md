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
ways to select 8 couples. To make communicating easier, I will be calling each set of 8 couples a solution. The purpose of this project is twofold:

1. Select and apply a mathematical model to this problem in order minimize the set of possible solutions.
2. Attempt to approximate the correct solution using probabalistic models.

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

## The Probabalistic Model

### The Base Model

When making predictions, it is often useful to have a model that can estimate the probability that your prediction is correct. Let's see what a probabalistic model would look like if the show had only one matching ceremony with zero visits to the truth booth.

In a matching ceremony, 8 couples are formed out of the 120 possible couples. It is then revealed that {% raw %}$$\dfrac{x}{8}$${% endraw %} couples are perfect matches.

This means that the 8 couples from the matching ceremony collectively have a {% raw %}$$\dfrac{x}{8}$${% endraw %} probability of being perfect matches *and* that the remaining 112 possible couples collectively have a {% raw %}$$\dfrac{8-x}{8}$${% endraw %} chance of being perfect matches.

In the real-world first matching ceremony, x=2. Therefore, we can assign a probability of {% raw %}$$\dfrac{\dfrac{2}{8}}{8} = 3.125\%$${% endraw %} to each couple in the solution and {% raw %}$$\dfrac{\dfrac{6}{8}}{112} = 0.670\%$${% endraw %} to the other 112 possible matches.

### Incorporating The Truth Booth

Results from the truth booth can be used to refine this model. If a non-match is revealed, we can set the probability for that couple to zero and exclude it from the probability calculations. Conversely, a perfect match should receive the maximum probability, {% raw %}$$\dfrac{1}{8} = 12.5\%$${% endraw %}. Perfect matches also affect probability calculations:

{% raw %}$$\dfrac{\dfrac{x - p}{8 - p}}{8 - p} = \dfrac{x - p}{(8 - p)^2}$${% endraw %}

Where x is the number of perfect matches revealed in a matching ceremony and p is the number of known perfect matches from the truth booth.
