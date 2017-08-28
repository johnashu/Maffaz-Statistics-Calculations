import numpy as np

x = [60, 61, 62, 63, 65]
y = [3.1, 3.6, 3.8, 4.0, 4.1]



######################################################################################################


#random number generator!!!

########################################################################################################


#bernoulli Trials 
def bernoulli_trials(n, p):
    """Perform n Bernoulli trials (success OR failure only). Returns the number of successes out of n Bernoulli trials, each of which has probability p of success."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success

print(bernoulli_trials(45, 23))

def maf_bernoulli_trial(n, k):
    """ 
    P(k successes in n trials)
    """
    p = 0.25
    q = 0.75
    
    nk = n - k
    p2k = p ** k
    q2nk = q ** nk

    r = (n / k) * p2k * q2nk

    return r

print(maf_bernoulli_trial(10, 7))
