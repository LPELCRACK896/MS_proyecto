import numpy as np
import scipy.stats as stats


def inverse_transform(distribution, num_samples=1):
    """
    Generates samples from a given distribution using the inverse transform method.

    :param distribution: A scipy.stats distribution object.
    :param num_samples: Number of samples to generate.
    :return: An array of generated samples.
    """
    u = np.random.uniform(0, 1, num_samples)
    return distribution.ppf(u)


def acceptance_rejection(distribution, auxiliary_distribution, c, num_samples=1):
    """
    Generates samples from a distribution using the acceptance-rejection method.

    :param distribution: Density function of the target distribution.
    :param auxiliary_distribution: Density function of the auxiliary distribution.
    :param c: Constant such that c * auxiliary_distribution >= distribution over its domain.
    :param num_samples: Number of samples to generate.
    :return: An array of generated samples.
    """
    samples = []
    while len(samples) < num_samples:
        y = auxiliary_distribution.rvs()
        u = np.random.uniform(0, 1)
        if u <= distribution(y) / (c * auxiliary_distribution.pdf(y)):
            samples.append(y)
    return np.array(samples)


if __name__ == "__main__":
    # Example usage with the exponential distribution
    exponential_distribution = stats.expon()
    result_samples = inverse_transform(exponential_distribution, 1000)

    # Example usage
    def target_distribution(x):
        return stats.norm.pdf(x)  # For example, a normal distribution

    auxiliary_distribution = stats.uniform(-4, 8)  # Uniform distribution as auxiliary
    c = 1  # In this case, c = 1 might be sufficient

    samples_ar = acceptance_rejection(target_distribution, auxiliary_distribution, c, 1000)
