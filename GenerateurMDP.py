import random

MINUSCULES = tuple(map(chr, range(ord('a'), ord('z')+1)))
MAJUSCULES = tuple(map(chr, range(ord('A'), ord('Z')+1)))
DIGITS = tuple(map(str, range(0, 10)))
SPECIALS = ('!', '@', '#', '$', '%', '^', '&', '*')

SEQUENCE = (MINUSCULES,
            MAJUSCULES,
            DIGITS,
            SPECIALS,
            )

def generer_aleatoire_mdp(total, sequences):
    r = _generer_aleatoire_nombre_pour_sequence(total, len(sequences))

    mdp = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            mdp += population[position]
            n += 1
    random.shuffle(mdp)
    
    while _repetition(mdp):
        random.shuffle(mdp)
        
    return ''.join(mdp)

def _generer_aleatoire_nombre_pour_sequence(total, sequence_nombre):
    """ 
        Genere une séquence aleatoire avec des nombres.
        Le nombre d'items égal à sequence_nombre et le nombre total d'item égal à total.
    """
    current_total = 0
    r = []
    for n in range(sequence_nombre-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def _repetition(password):
    """ Check if there is any 2 characters repeating consecutively """
    n = 1
    while(n < len(password)):
        if password[n] == password[n-1]:
            return True
        n += 1
    return False

if __name__ == '__main__':
    print(generer_aleatoire_mdp(random.randint(6, 30), SEQUENCE))