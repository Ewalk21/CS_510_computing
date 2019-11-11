#include <stdio.h>
#include "minunit.h"
#include "../src/fibonacci.h"

/* Note: structure of test file taken from minunit example at
 *   http://www.jera.com/techinfo/jtns/jtn002.html
 */

// Needed for minunit to function properly
int tests_run = 0;

/* Set of tests to run
 */
static char * test_fib_1() {
    mu_assert("error, fibonacci(1) != 1", fibonacci(1) == 1);
    return 0;
}

static char * test_fib_4() {
    mu_assert("error, fibonacci(4) != 3", fibonacci(4) == 3);
    return 0;
}

static char * test_fib_7() {
    mu_assert("error, fibonacci(7) != 13", fibonacci(7) == 13);
    return 0;
}

static char * test_fib_8() {
    mu_assert("error, fibonacci(8) != 21", fibonacci(8) == 21);
    return 0;
}

/* all_tests collects a set of tests defined above, and runs them
 */
static char * all_tests() {
    mu_run_test(test_fib_1);
    mu_run_test(test_fib_4);
    mu_run_test(test_fib_7);
    mu_run_test(test_fib_8);
    return 0;
}

/* A test file should be executable, so has a main function
 * Note that it runs all the tests above, and prints output accordingly
 */
int main(int argc, char **argv) {
    // String to store all test results
    char *result = all_tests();
    
    // If the result is not null, there is at least one error
    if (result != 0) {
        // print the errors
        printf("%s\n", result);
    }
    else {
        // or inform user that tests passed
        printf("ALL TESTS PASSED\n");
    }
    // Show count of run tests
    printf("Tests run: %d\n", tests_run);
    
    // The return code is the boolean of whether all tests passed
    return result != 0;
}
