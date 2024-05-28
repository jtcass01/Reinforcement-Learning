/**
 * @author Jacob Taylor Cassady
*/

#include "../inc/k_armed_bandit.hpp"

// 3rd Party Libraries
#include <gtest/gtest.h>

TEST(KArmedBanditTest, ConstructorTest) {
    kArmedBandit bandit(10);
    for (int i = 0; i < 10; ++i) {
        // Check that the initial values are within the expected range for a normal distribution
        EXPECT_GE(bandit.getQStar(i), -3.0f);
        EXPECT_LE(bandit.getQStar(i), 3.0f);
    }
}

TEST(KArmedBanditTest, GetRewardTest) {
    kArmedBandit bandit(10);
    for (int i = 0; i < 10; ++i) {
        // Check that the rewards are within the expected range for a normal distribution
        float reward = bandit.getReward(i);
        EXPECT_GE(reward, bandit.getQStar(i) - 3.0f);
        EXPECT_LE(reward, bandit.getQStar(i) + 3.0f);
    }
}