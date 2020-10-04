# Caesar cipher solver
from etao import CaesarCipher, NgramFrequencyScorer
from etao.freq import ENGLISH_DIGRAMS

encrypted_text =

scorer = NgramFrequencyScorer(freq=ENGLISH_DIGRAMS)

# Get every Caesar shift of the ciphertext
shifts = [CaesarCipher(n).decrypt(encrypted_text) for n in range(26)]

# Score each shift according to English character frequency.
# Get tuples that pair the score with the text.
scored_shifts = [(scorer.score(shift), shift) for shift in shifts]

# Sort by score, descending order
scored_shifts.sort(reverse=True)

# Print the top 3 results
for result in scored_shifts[0:3]:
    print('"%s" (%02d%%)' % (result[1], int(result[0] * 100)))