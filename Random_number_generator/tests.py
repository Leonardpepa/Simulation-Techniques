from RNGenerator import RNGererator
import math

def print_n_random_numbers(seed: int, n: int):
    """
    seed: seed for the random number generator
    n: sample size \n
    prints the n random numbers generated with the current seed
    """
    random = RNGererator(seed)
    for _ in range(n):
        print(random.next_random())

def mean(seed: int, n: int):
    """
    seed: seed for the random number generator
    n: sample size \n
    calculate and return the mean for n random numbers with the current seed
    """
    random = RNGererator(seed)
    mean = 0
    for _ in range(n):
        mean += random.next_random() / n
    
    return mean

def standard_deviation(seed: int, n: int):
    """
    seed: seed for the random number generator
    n: sample size \n
    calculate and return the standard deviation for n random numbers with the current seed
    """
    random = RNGererator(seed)
    ssq = 0
    sqs = 0
    for _ in range(n):
        random_number = random.next_random()
        ssq += math.pow(random_number, 2)
        sqs += random_number
    
    standard_deviation = math.sqrt(ssq / n - math.pow(sqs / n, 2))
    return standard_deviation

def runs_test(seed: int, n: int):
    """
    seed: seed for the random number generator
    n: sample size \n
    calculate and return runs tests from 1 - 10 with the current seed
    """
    random = RNGererator(seed)
    runs = [0 for i in range(10)]

    isAbove = random.next_random() >= 0.5
    curr_run = 1

    for _ in range(n):
        if isAbove and random.next_random() >= 0.5:
            curr_run += 1
        elif not isAbove and random.next_random() < 0.5:
            curr_run += 1
        else:
            runs[(curr_run - 1) % 10] += 1
            curr_run = 1
            isAbove = not isAbove
    return runs


def region_test(seed: int, n: int):
    """
    seed: seed for the random number generator
    n: sample size \n
    calculate and return region tests from 0-1, ...,9-10 with the current seed
    """
    random = RNGererator(seed)
    regions = [0 for i in range(10)]
    for _ in range(n):
        random_number = math.floor(random.next_random() * len(regions))
        regions[random_number] += 1
    
    return regions


def main():
    TESTING_SEED = 0
    TESTING_SAMPLE = 100

    print("First 100 random numbers")
    
    print_n_random_numbers(TESTING_SEED, TESTING_SAMPLE)

    print("mean for ", TESTING_SAMPLE, "random numbers", mean(TESTING_SEED, TESTING_SAMPLE))

    print("standard deviation for ", TESTING_SAMPLE, "random numbers", standard_deviation(TESTING_SEED, TESTING_SAMPLE))
    
    TESTING_SAMPLE = 1_000_000


    print("mean for ", TESTING_SAMPLE, "random numbers", mean(TESTING_SEED, TESTING_SAMPLE))

    print("standard deviation for ", TESTING_SAMPLE, "random numbers", standard_deviation(TESTING_SEED, TESTING_SAMPLE))
    

    print("runs test 1-10")
    print(runs_test(TESTING_SEED, TESTING_SAMPLE))

    print("region test")
    print(region_test(TESTING_SEED, TESTING_SAMPLE))



if __name__ == "__main__":
    main()