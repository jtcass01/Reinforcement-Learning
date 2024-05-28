#ifndef __K_ARMED_BANDIT_HPP__
#define __K_ARMED_BANDIT_HPP__

#include <vector>

class kArmedBandit
{
public:
    kArmedBandit(int k);
    ~kArmedBandit();

    float getReward(int action);
    float getQStar(int action) { return _q_star[action]; }

private:
    std::vector<float> _q_star;
};

#endif // __K_ARMED_BANDIT_HPP__
