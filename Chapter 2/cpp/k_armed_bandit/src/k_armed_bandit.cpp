#include "../inc/k_armed_bandit.hpp"

#include <random>
#include <vector>

kArmedBandit::kArmedBandit(int k)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<float> distribution(0.0f, 1.0f);

    // Constructor
    _q_star.resize(k);
    for (std::vector<float>::iterator it = _q_star.begin(); it != _q_star.end(); ++it)
    {
        // Set q*(a) to a random value from a normal distribution with mean 0 and variance 1
        *it = distribution(gen);
    }
}

kArmedBandit::~kArmedBandit()
{
    // Destructor
}

float kArmedBandit::getReward(int action)
{
    static std::random_device rd;
    static std::mt19937 gen(rd());

    std::normal_distribution<float> distribution(_q_star[action], 1.0f);

    return distribution(gen);
}

