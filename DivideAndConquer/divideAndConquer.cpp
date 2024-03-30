#include <iostream>
#include <vector>
#include <chrono>
#include "matplotlibcpp.h"

using namespace std;
using namespace std::chrono;
namespace plt = matplotlibcpp;

// Function to calculate binomial coefficient recursively
int binomialCoeff(int n, int k) {
    if (k > n)
        return 0;
    if (k == 0 || k == n)
        return 1;
    // Recursive Call
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k);
}

int main() {
    int n = 30;
    // std::vector<int> x(n), y(n), z(n), w(n,2);
    // for (int k = 1; k < n - 1; ++k) {
    //     x.at(k) = k;
        // auto start = high_resolution_clock::now();
        // binomialCoeff(n, k);
        // auto stop = high_resolution_clock::now();
        // auto duration = duration_cast<std::chrono::nanoseconds>(stop - start);
        // y.at(k) = duration.count();
    // }
    // // Print the values
    // for (int i = 0; i < x.size(); ++i) {
    //     cout << "For k = " << x[i] << ", Time taken: " << y[i] << " nanoseconds" << endl;
    // }
    // Prepare data.
    std::vector<double> x(n), y(n), z(n), w(n,2);
    for(int i=1; i<n-1; ++i) {
        x.at(i) = i;
        auto start = high_resolution_clock::now();
        binomialCoeff(n, i);
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<std::chrono::nanoseconds>(stop - start);
        y.at(i) = duration.count();
        // z.at(i) = log(i);
    }

    // Set the size of output image to 1200x780 pixels
    plt::figure_size(2000, 2000);
    // Plot line from given x and y data. Color is selected automatically.
    plt::plot(x, y);
    // Plot a red dashed line from given x and y data.
    // plt::plot(x, w,"r--");
    // Plot a line whose name will show up as "log(x)" in the legend.
    // plt::named_plot("log(x)", x, z);
    // Set x-axis to interval [0,1000000]
    plt::ylim(0, 1000*1000);
    // Add graph title
    plt::title("Divide And Conquer");
    // Enable legend.
    plt::legend();
    // Save the image (file format is determined by the extension)
    plt::save("./basic.png");

    
    return 0;
}
